from sklearn.cluster import KMeans
import numpy as np

coords = df[['longitude','latitude']].values

k = 8

kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(coords)

centroids = kmeans.cluster_centers_


fig, ax = plt.subplots(figsize=(12,10))

surat_map.plot(ax=ax, color='none', edgecolor='black')

scatter = ax.scatter(
    df['longitude'],
    df['latitude'],
    c=df['cluster'],   
    cmap='tab10',
    s=5,
    alpha=0.7
)

ax.scatter(
    centroids[:,0],   
    centroids[:,1],   
    color='black',
    marker='X',
    s=150,
    label='Optimal Charging Station'
)

plt.title("Optimal EV Charging Station Locations using K-Means (10 clusters)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()

plt.show()
