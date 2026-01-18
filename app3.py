import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MeasureControl

st.title("خريطة - العين السخنة مع قياس المساحات")

# إنشاء الخريطة
m = folium.Map(location=[29.9, 32.3], zoom_start=10, tiles="Stamen Terrain")

# إضافة أداة القياس
m.add_child(MeasureControl())

# عرض الخريطة
st_data = st_folium(m, width=700, height=500)
