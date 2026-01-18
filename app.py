import streamlit as st
import leafmap.foliumap as leafmap

# عنوان التطبيق
st.title("خريطة تجريبية")

# إنشاء الخريطة
m = leafmap.Map(center=[40, -100], zoom=4)

# هنا نضيف ملف الـ GeoJSON
m.add_geojson("D:/streamlit_projects/project of python attractive/us_regions.geojson", layer_name="US Regions")

m.add_points_from_xy(
    "D:/streamlit_projects/project of python attractive/cities.csv",
    x="longitude",  # العمود اللي فيه خط الطول
    y="latitude",   # العمود اللي فيه خط العرض
    color_column="region",  # لو عايزين نلون النقاط حسب المنطقة
    add_legend=True  # عشان يظهر مفتاح الألوان
)


m.add_basemap("SATELLITE")

# عرض الخريطة في Streamlit
m.to_streamlit(height=600)
