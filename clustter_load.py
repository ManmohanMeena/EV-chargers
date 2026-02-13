import matplotlib.pyplot as plt
import seaborn as sns 

station_load = df['cluster'].value_counts().sort_index()

print(station_load)

station_labels = [f"Station {i+1}" for i in station_load.index]

plt.figure(figsize=(10,6))

colors = sns.color_palette('pastel', n_colors=len(station_load))

plt.bar(
    station_labels,
    station_load.values,
    color=colors 
)

plt.title("Number of Vehicles Charging per Station")
plt.xlabel("Charging Station ID")
plt.ylabel("Number of Vehicles")

plt.xticks(rotation=45)

plt.show()