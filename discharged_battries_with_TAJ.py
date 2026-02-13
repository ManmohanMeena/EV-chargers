import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("out_final.csv")

surat_map = gpd.read_file("TAJ234.geojson")

surat_map = surat_map.to_crs("EPSG:4326")

fig, ax = plt.subplots(figsize=(12,10))

surat_map.plot(ax=ax, color='none', edgecolor='black')

ax.scatter(
    df['longitude'],
    df['latitude'],
    color='red',
    s=3,
    label='10% Battery Location'
)

plt.title("Locations Where EV Battery Dropped to 10%")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()

plt.show()
ax.set_aspect('equal')

