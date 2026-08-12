import streamlit as st

st.title("Cargar y Descargar Archivo")

# 1. Botón de carga
file = st.file_uploader("Sube tu archivo", type=["csv"])

# 2. Botón de descarga condicional (solo aparece si hay un archivo cargado)
if file is not None:
  st.download_button(
      label="Descargar archivo modificado",
      data=file,
      file_name="archivo_modificado.csv",
      mime="text/csv",
  )
else:
  st.info("Por favor, sube un archivo CSV para habilitar la descarga.")
