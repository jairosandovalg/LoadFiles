import streamlit as st
from streamlit_option_menu import option_menu

st.title("Cargar y Descargar Archivo")
st.sidebar.header("Panel de Control")

with st.sidebar:
  st.header("Panel de Control")

  # Menú con iconos y selector de fondo activo
  selected = option_menu(
      menu_title="Navegacion",  # Título del menú
      options=[
          "Modificación de archivos",
          "Análisis de Datos",
          "Reportes",
      ],  # Tus 3 opciones
      icons=["file-earmark-arrow-up", "bar-chart", "file-text"],  # Iconos opcionales de Bootstrap
      menu_icon="cast",
      default_index=0,
  )
  
st.markdown("---")

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
