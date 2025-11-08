# LIVESTOCK-BEAHVIOR-AND-HEALTH-ANAMOLY-DETECTION
AI-based livestock health monitoring system using time-series sensor data (temperature, movement, GPS). Detects abnormal behavior patterns to identify early signs of illness, stress, or calving using anomaly detection models.
# 🐄 Livestock Behavior & Health Anomaly Detection

This project focuses on detecting **abnormal behavior and early health issues in livestock** using **IoT sensor data** and **Machine Learning-based Anomaly Detection**. By continuously analyzing time-series data such as **body temperature, movement activity, and GPS patterns**, the system identifies unusual behaviors that may indicate:

- Early-stage illnesses
- Stress or discomfort
- Reduced movement or lameness
- Calving events or reproductive changes
- Theft or roaming outside boundary areas

---

## 🔍 Problem Statement

Farmers often notice health issues in animals **after symptoms become severe**. Early diagnosis is difficult and manual monitoring is time-consuming.  
This system provides **real-time monitoring with automated alerts**, helping farmers take preventive action to improve livestock welfare and reduce losses.

---

## 🎯 Objectives

- Collect continuous livestock sensor data (time-series format)
- Preprocess and clean the data
- Train an **Anomaly Detection Model** to learn normal behavior
- Detect abnormal deviations in real-time
- Trigger **alerts for possible disease or stress**

---

## 📊 Dataset Used

Type of Data:
| Sensor | Parameter | Purpose |
|--------|-----------|---------|
| Temperature Sensor | Body Temperature | Detect fever/infection |
| Accelerometer / Step Counter | Movement Activity | Detect stress, lameness, lethargy |
| GPS Tracker | Location Movement | Detect roaming behavior or escape |
| Heart Rate Sensor (optional) | BPM | Detect stress response |

If dataset is from external source, mention:

## DATASET SOURCE
-<a href="https://github.com/SibaniPJ/LIVESTOCK-BEAHVIOR-AND-HEALTH-ANAMOLY-DETECTION/blob/main/livestock_behavior_50000.csv">Dataset</a>

#Image of webpage
![Project Screenshot](https://raw.githubusercontent.com/SibaniPJ/LIVESTOCK-BEAHVIOR-AND-HEALTH-ANAMOLY-DETECTION/main/Screenshot%20(180).png)

## 📦 Technologies Used
Python
NumPy / Pandas / Matplotlib
Scikit-Learn
TensorFlow / Keras (for LSTM Autoencoder)
IoT Sensor Devices (Temperature, GPS, Accelerometer)

## 📣 Output
Graphs of anomaly scores
Alerts highlighting abnormal behavior
Comparison of normal vs abnormal activity trends

## 🐾 Future Enhancements
Live dashboard (Streamlit / Web App)
Real-time edge computing on mobile / Raspberry Pi
Integration with veterinary alert system

