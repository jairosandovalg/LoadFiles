import streamlit as st

st.title("Cargar y Descargar Archivo")
st.sidebar.header("Panel de Control")
st.markdown("-")

file = st.file_uploader("Sube tu archivo", type=["csv"])

if file is not None:
  st.download_button(
      label="Descargar archivo modificado",
      data=file,
      file_name="archivo_modificado.csv",
      mime="text/csv",
  )
else:
  st.info("Por favor, sube un archivo CSV para habilitar la descarga.")
