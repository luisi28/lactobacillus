import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Bacterias Lácticas - Lactobacillus", page_icon="🦠", layout="wide")

st.title("🦠 Lista de 100 especies de *Lactobacillus* y su fermentación de carbohidratos")
st.write("Este aplicativo muestra 100 especies de *Lactobacillus* con su capacidad de fermentar distintos carbohidratos.")

# --- Definimos carbohidratos ---
carbohidratos = ["Glucosa", "Lactosa", "Sacarosa", "Manitol", "Xilosa"]

# --- Generamos 100 especies ficticias ---
especies = [f"Lactobacillus especie {i}" for i in range(1, 101)]

# --- Creamos tabla aleatoria de fermentación (+ = fermenta, - = no fermenta) ---
data = []
for especie in especies:
    fermentacion = [random.choice(["+", "-"]) for _ in carbohidratos]
    data.append([especie] + fermentacion)

df = pd.DataFrame(data, columns=["Especie"] + carbohidratos)

# --- Filtro de búsqueda ---
busqueda = st.text_input("🔍 Buscar especie:")
if busqueda:
    df = df[df["Especie"].str.contains(busqueda, case=False)]

# --- Mostrar tabla ---
st.dataframe(df, use_container_width=True)

st.success("✅ Datos generados de manera aleatoria para demostración.")
