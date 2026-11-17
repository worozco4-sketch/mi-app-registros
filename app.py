import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mi App Registros", page_icon="📋")
st.title("📋 Mi App de Registros")
st.write("Registra y mira tus datos aquí")

# Formulario
with st.form("formulario"):
    nombre = st.text_input("Nombre")
    detalle = st.text_input("Detalle / Motivo")
    cantidad = st.number_input("Cantidad", min_value=1, value=1)
    enviar = st.form_submit_button("Guardar Registro")

    if enviar:
        if nombre == "":
            st.warning("Escribe un nombre primero")
        else:
            st.success(f"Guardado: {nombre} - {detalle} - {cantidad}")

st.divider()
st.subheader("Registros guardados")
st.info("Aquí van a aparecer tus registros cuando los guardes.")

# Tabla de ejemplo
datos = {
    "Nombre": ["Ejemplo 1", "Ejemplo 2"],
    "Detalle": ["Prueba", "Prueba"],
    "Cantidad": [1, 2]
}
st.dataframe(pd.DataFrame(datos), use_container_width=True)
