# Efficient Data Stream Anomaly Detection

## Project Description:
Developed a Python script capable of detecting anomalies in a continuous data stream. This stream, simulating real-time sequences of floating-point numbers, could represent various metrics such as financial transactions or system metrics. Focus is on identifying unusual patterns, such as exceptionally high values or deviations from the norm.

## Objectives:
1. Algorithm Selection: Identify and implement a suitable algorithm for anomaly detection, capable of adapting to concept drift and seasonal variations.
2. Data Stream Simulation: Design a function to emulate a data stream, incorporating regular patterns, seasonal elements, and random noise.
3. Anomaly Detection: Develop a real-time mechanism to accurately flag anomalies as the data is streamed.
4. Optimization: Ensure the algorithm is optimized for both speed and efficiency.
5. Visualization: Create a straightforward real-time visualization tool to display both the data stream and any detected anomalies

## Requirements:
numpy==1.21.5<br>
scikit_learn==1.0.2<br>
joblib==1.2.0<br>
matplotlib==3.8.1

## Working
We have [main.py](https://github.com/ParagGawai/Efficient_Data_Stream_Anomaly_Detection/blob/main/main.py) file which is the main driver code of the project. It requires [model_prod.py]
