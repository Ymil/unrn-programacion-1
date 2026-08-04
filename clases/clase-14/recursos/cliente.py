import requests

# Este modulo se encarga de hablar con el servidor de mensajes.
# Los otros programas lo importan para enviar o recibir mensajes sin repetir
# la parte de conexion.

# Direccion del servidor.
SERVIDOR = "http://localhost:8000"


def enviar_mensaje(usuario: str, texto: str):
    """Envia un mensaje y devuelve la respuesta; relanza errores."""
    try:
        respuesta = requests.post(
            f"{SERVIDOR}/mensaje",
            json={
                "usuario": usuario,
                "texto": texto,
            },
            timeout=10,
        )
    except requests.RequestException as error:
        print(f"No se pudo hablar con el servidor: {error}")
        raise

    # Si el servidor responde con un error, Python lo avisa aca.
    try:
        respuesta.raise_for_status()
    except requests.HTTPError:
        print(f"Error del servidor: {respuesta.json()['detail']}")
        raise

    # Convertimos la respuesta del servidor a datos faciles de usar en Python.
    return respuesta.json()


def obtener_mensaje():
    """Pide el proximo mensaje; relanza errores."""
    respuesta = requests.get(
        f"{SERVIDOR}/mensaje",
        timeout=35,
    )

    respuesta.raise_for_status()

    # Convertimos la respuesta del servidor a datos faciles de usar en Python.
    return respuesta.json()
