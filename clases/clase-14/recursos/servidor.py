import asyncio

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

oyentes: list[asyncio.Future] = []


class Mensaje(BaseModel):
    usuario: str
    texto: str


@app.get("/mensaje")
async def obtener_mensaje():
    loop = asyncio.get_running_loop()
    futuro = loop.create_future()

    oyentes.append(futuro)

    try:
        return await asyncio.wait_for(futuro, timeout=30)
    except asyncio.TimeoutError:
        return None
    finally:
        if futuro in oyentes:
            oyentes.remove(futuro)


@app.post("/mensaje")
async def enviar_mensaje(mensaje: Mensaje):
    datos = mensaje.model_dump()

    if mensaje.usuario.count("_") != 1:
        raise HTTPException(status_code=400, detail="El usuario no es valido, debe contener Nombre_Apellido")

    nombre, apellido = mensaje.usuario.split("_")
    if not (nombre and apellido and nombre[0].isupper() and apellido[0].isupper()):
        raise HTTPException(status_code=400, detail="El usuario no es valido, debe contener Nombre_Apellido")

    for oyente in oyentes.copy():
        if not oyente.done():
            oyente.set_result(datos)

    return {
        "entregado_a": len(oyentes),
        "mensaje": datos,
    }
