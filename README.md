Perfect 👍 — I will write you a **professional, industry-level README.md** that:

✅ clearly explains the workflow
✅ looks strong on GitHub (recruiter + BPCL friendly)
✅ highlights simulation + data science + transport planning skills
✅ structured like real research/project repos.

You can directly copy-paste this.

---

# 🚀 **README.md (Professional Version)**

```md
# 🚗 Modelling Electric Vehicle (EV) Charging Infrastructure using Microscopic Traffic Simulation (SUMO)

## 📌 Overview

This project focuses on modelling and optimizing Electric Vehicle (EV) charging infrastructure for Surat city using microscopic traffic simulation. The workflow integrates transportation demand modelling, GIS analysis, clustering algorithms, and SUMO-based EV simulations to identify optimal charging station locations.

The main objective is to:

- Analyze EV travel demand using Origin–Destination (OD) matrices.
- Simulate EV battery behaviour in realistic traffic conditions.
- Identify locations where EV batteries frequently drop below critical levels.
- Apply clustering techniques to determine optimal charging station placement.
- Validate charging infrastructure effectiveness through simulation.

---

## 🎯 Key Features

- Creation of Traffic Analysis Zones (TAZs) using land-use and demographic data.
- OD Matrix generation for travel demand modelling.
- SUMO microscopic traffic simulation with EV battery models.
- Extraction of low battery vehicle locations using TraCI.
- K-Means clustering to identify optimal charging station sites.
- Comparison between optimized and unoptimized charging infrastructure.
- Visualization using GIS and Python.

---

## 🗺️ Study Area

The study focuses on Surat city, India.

Inputs include:

- Land-use datasets
- TAZ boundaries
- Population and employment data
- Road network converted to SUMO format

Example TAZ visualization:

![TAZ Map](Images/TAZes.png)

---

## ⚙️ Methodology

### 1️⃣ Data Preparation

- Created TAZs using land-use and spatial datasets.
- Generated centroids for zones.
- Estimated travel demand using household and employment data.

---

### 2️⃣ OD Matrix Generation

Trips were estimated using:

- Population distribution
- Employment data
- Land-use characteristics

OD matrix used as input for vehicle route generation.

---

### 3️⃣ SUMO Simulation Setup

Components:

- Road network (`.net.xml`)
- Vehicle routes (`.rou.xml`)
- Battery device configuration (`.add.xml`)

EV battery behaviour simulated during trips.

---

### 4️⃣ Extracting Discharged EV Locations

Using TraCI:

- Monitored battery percentage during simulation.
- Recorded locations where battery dropped below 10%.

Example output:

![Discharged EVs](Images/Discharge_unoptimized.png)

---

### 5️⃣ Charging Station Optimization

Applied K-Means clustering on low battery locations:

- Identified high-demand charging regions.
- Generated optimal station locations.

Example:

![Optimized Charging Stations](Images/clustter_optimized.png)

---

### 6️⃣ Validation Through Simulation

Charging stations deployed into SUMO:

- Created charging station XML.
- Re-ran simulation.
- Compared system performance.

---

## Results

### Discharged EV Locations (Unoptimized)

![Unoptimized](Images/Discharge_unoptimized.png)

### Optimized Charging Station Deployment

![Optimized](Images/clustter_optimized.png)

### Charging Load Distribution

Optimized:

![Optimized Load](Images/clustter_load_optimized.png)

Unoptimized:

![Unoptimized Load](Images/clustter_load_unoptimized.png)

---

## Tools & Technologies

- SUMO (Simulation of Urban Mobility)
- Python
- TraCI API
- GeoPandas
- QGIS

---

## Project Structure

```

├── 2345net.net.xml
├── routes_electric_1500.rou.xml
├── battery_devices_1500_final1.add.xml
├── TAJ234.geojson
├── cluster_making.py
├── cluster_load.py
├── discharged_batteries_with_TAJ.py
├── config_optimized.sumo.cfg
├── README.md

```



## Key Insights

- Charging demand clusters align with dense travel corridors.
- Optimized station placement reduces battery depletion risk.
- Spatial clustering improves infrastructure efficiency.

---

## Future Improvements

- Capacity constraints modelling.
- Queue analysis at charging stations.
- Dynamic charging demand forecasting.
- Real-world traffic calibration.

---

## Author

Manmohan Meena  
B.Tech Civil Engineering  
IIT Gandhinagar

---

