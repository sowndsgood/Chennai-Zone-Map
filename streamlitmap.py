import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from PIL import Image

# Initialize map centered around Chennai
chennai_map = folium.Map(location=[13.0827, 80.2707], zoom_start=12)

# Coordinates for each area (approximate)
areas = {
    "North Zone": {
        "Tondiarpet": [13.1231, 80.2943],
        "Royapuram": [13.1055, 80.2932],
        "Thiru-Vi-Ka Nagar": [13.1092, 80.2271],
        "Manali": [13.1738, 80.2596],
        "Washermanpet": [13.1146, 80.2898],
        "Choolai": [13.0954, 80.2614],
        "Madhavaram": [13.1424, 80.2302],
        "Sembium": [13.1133, 80.2340],
        "Retteri": [13.1306, 80.2154]
    },
    "Central Zone": {
        "George Town": [13.0913, 80.2820],
        "Sowcarpet": [13.0997, 80.2784],
        "Triplicane": [13.0557, 80.2783],
        "Mylapore": [13.0338, 80.2680],
        "Egmore": [13.0732, 80.2597],
        "Nungambakkam": [13.0609, 80.2435],
        "Purasawalkam": [13.0908, 80.2536],
        "Chintadripet": [13.0703, 80.2724],
        "Vepery": [13.0908, 80.2565]
    },
    "West Zone": {
        "Anna Nagar": [13.0860, 80.2122],
        "Kilpauk": [13.0865, 80.2426],
        "Mogappair": [13.0906, 80.1689],
        "Ambattur": [13.1140, 80.1474],
        "Virugambakkam": [13.0525, 80.1918],
        "Koyambedu": [13.0695, 80.2013],
        "Valasaravakkam": [13.0411, 80.1778],
        "Avadi": [13.1147, 80.1098],
        "Ayyapakkam": [13.0972, 80.1373],
        "Maduravoyal": [13.0668, 80.1700],
        "Nolambur": [13.0803, 80.1732]
    },
    "South Zone": {
        "Adyar": [13.0067, 80.2570],
        "Besant Nagar": [12.9981, 80.2660],
        "Thiruvanmiyur": [12.9805, 80.2598],
        "Velachery": [12.9796, 80.2183],
        "Guindy": [13.0109, 80.2206],
        "Kotturpuram": [13.0178, 80.2417],
        "Madipakkam": [12.9698, 80.2087],
        "Pallikaranai": [12.9427, 80.2073],
        "Perungudi": [12.9652, 80.2413],
        "Sholinganallur": [12.8996, 80.2271],
        "Karapakkam": [12.9140, 80.2295],
        "Neelankarai": [12.9483, 80.2590]
    },
    "Southwest Zone": {
        "Saidapet": [13.0213, 80.2204],
        "T. Nagar": [13.0406, 80.2337],
        "Kodambakkam": [13.0524, 80.2217],
        "Teynampet": [13.0415, 80.2525],
        "West Mambalam": [13.0341, 80.2225],
        "Ashok Nagar": [13.0365, 80.2124],
        "Alwarpet": [13.0353, 80.2502],
        "Nandanam": [13.0298, 80.2408]
    },
    "Southeast Zone": {
        "Sholinganallur": [12.8996, 80.2271],
        "Perungudi": [12.9652, 80.2413],
        "Thoraipakkam": [12.9249, 80.2303],
        "Neelankarai": [12.9483, 80.2590],
        "Palavakkam": [12.9617, 80.2580],
        "Kottivakkam": [12.9601, 80.2555],
        "Injambakkam": [12.9344, 80.2435],
        "Tambaram": [12.9260, 80.1024],
        "Velachery": [12.9796, 80.2183],
        "Medavakkam": [12.9250, 80.1757],
        "Perumbakkam": [12.8897, 80.1900]
    },
    "Northwest Zone": {
        "Madhavaram": [13.1424, 80.2302],
        "Perambur": [13.1172, 80.2337],
        "Kolathur": [13.1266, 80.2173],
        "Puzhal": [13.1584, 80.2139],
        "Sembium": [13.1133, 80.2340],
        "Retteri": [13.1306, 80.2154],
        "Villivakkam": [13.1040, 80.2015],
        "Ayanavaram": [13.1098, 80.2350],
        "Korattur": [13.1097, 80.1808]
    }
}

# Colors for each zone
zone_colors = {
    "North Zone": "blue",
    "Central Zone": "green",
    "West Zone": "red",
    "South Zone": "purple",
    "Southwest Zone": "orange",
    "Southeast Zone": "yellow",
    "Northwest Zone": "pink"
}


# Plotting areas on the map
for zone, areas_dict in areas.items():
    for area, coordinates in areas_dict.items():
        folium.CircleMarker(
            location=coordinates,
            radius=5,
            color=zone_colors[zone],
            fill=True,
            fill_color=zone_colors[zone],
            fill_opacity=0.6,
            popup=f"{area}, {zone}"
        ).add_to(chennai_map)

# Display the map using Streamlit
st.title("Chennai Metropolitan Area")
folium_static(chennai_map)

image = Image.open('water.png')
st.image(image)