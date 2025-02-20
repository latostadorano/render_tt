import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Lanzar una moneda') # crear un header
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico disperción') #crear otro botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: 
    st.write('Creación de un gráfico de disperción para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de disperción
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
    

