import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


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
      icons=["file-earmark-arrow-up", "bar-chart", "file-text"],  # Iconos de Bootstrap
      menu_icon="cast",
      default_index=0,
  )

st.markdown("---")

# --- CONTENIDO DINÁMICO SEGÚN LA OPCIÓN SELECCIONADA ---

if selected == "Modificación de archivos":
  st.title("Cargar y Descargar Archivo")
  st.subheader("🛠️ Sección de Modificación de archivos")
  
  file = st.file_uploader("Sube tu archivo", type=["csv"])

  if file is not None:
    # Aquí puedes leer tu CSV con pandas para modificarlo en el futuro
    df = pd.read_csv(file)
    st.write("Vista previa del archivo original:", df.head(3))

    st.download_button(
        label="Descargar archivo modificado",
        data=file,
        file_name="archivo_modificado.csv",
        mime="text/csv",
    )
  else:
    st.info("Por favor, sube un archivo CSV para habilitar la descarga.")

elif selected == "Análisis de Datos":
  st.subheader("📊 Sección de Análisis de Datos")
  st.write("Aquí podrás realizar cálculos, agrupaciones y resúmenes estadísticos de tus datasets próximamente.")
  
  # Ejemplo sencillo para escalar
  data_ejemplo = {"Columna1": [1, 2, 3], "Columna2": [4, 5, 6]}
  st.dataframe(pd.DataFrame(data_ejemplo))

elif selected == "Reportes":
  st.subheader("📑 Sección de Reportes")
  st.write("Espacio reservado para generar gráficos interactivos o exportar informes ejecutivos.")
  st.success("¡El menú lateral funciona correctamente!")
