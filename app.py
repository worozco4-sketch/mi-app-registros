import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📋 Mi App de Registros")
st.write("Registra y mira tus datos aqui")

if "registros" not in st.session_state:
    st.session_state.registros = []

with st.form("form_registro"):
    nombre = st.text_input("Nombre")
    detalle = st.text_input("Detalle / Motivo")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    guardar = st.form_submit_button("Guardar Registro")

if guardar:
    if nombre and detalle:
        nuevo = {
            "Fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "Nombre": nombre,
            "Detalle": detalle,
            "Cantidad": cantidad
        }
        st.session_state.registros.append(nuevo)
        st.success(f"Guardado: {nombre} - {detalle} - {cantidad}")
    else:
        st.warning("Escribe Nombre y Detalle")

st.subheader("Registros guardados")
if len(st.session_state.registros) == 0:
    st.info("Aqui van a aparecer tus registros cuando los guardes.")
else:
    df = pd.DataFrame(st.session_state.registros)
    st.dataframe(df, use_container_width=True)
    st.write(f"Total registros: {len(df)}")
