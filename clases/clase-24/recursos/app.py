import streamlit as st

st.title("Mi primera aplicación")
st.header("Subtitle")
st.write("Hola mundo")
st.markdown("""

### Lista de palabras

- Hola
- Mundo
- Cruel
""")
print("Hola mundo")

nombre = st.text_input("Nombre")
descripcion = st.text_area("Descripcion")
unidades = st.number_input("Unidades", 1)
color = st.selectbox("Color", ["Rojo", "Azul"])
urgente = st.checkbox("Es urgente")

st.write(nombre)
st.write(descripcion)
st.write(unidades)
st.write(color)
st.write(urgente)

sumador = 10
if st.button("Saludar"):
    sumador += 1
print(sumador)


st.write(42)
st.write(["Resistencia", "LED", "Pulsador"])
st.write({"componente": "LED", "cantidad": 12})

import pandas as pd

df = pd.DataFrame({
    "componente": ["LED", "Pulsador"],
    "cantidad": [12, 8]
})

print(df)
st.write(df)
st.dataframe(df)

st.info("El catálogo se actualiza cada semana.")
st.warning("Quedan pocas unidades disponibles.")
st.error("No se pudo abrir el archivo.")
st.success("La reserva quedó registrada.")

st.image(
    "sixseven.png",
    caption="Sixseven sixseven"
)

import streamlit as st

on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")