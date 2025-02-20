import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Crear gráficos con streamlit y plotly') # crear un header
build_hist = st.checkbox('Construir histograma') # crear un botón
build_scatter = st.checkbox('Construir gráfico dispersion') #crear otro botón
        
if build_hist: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter: 
    st.write('Creación de un gráfico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
    

