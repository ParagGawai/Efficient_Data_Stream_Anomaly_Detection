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
#### [main.py](https://github.com/ParagGawai/Efficient_Data_Stream_Anomaly_Detection/blob/main/main.py)
This file is the main driver code of the project. It requires-
1. [model_prod.py](https://github.com/ParagGawai/Efficient_Data_Stream_Anomaly_Detection/blob/main/model_prod.py)
2. [settings.py](https://github.com/ParagGawai/Efficient_Data_Stream_Anomaly_Detection/blob/main/settings.py)
3. [anomaly.py](https://github.com/ParagGawai/Efficient_Data_Stream_Anomaly_Detection/blob/main/anomaly.py)

#### [settings.py](https://github.com/ParagGawai/Efficient_Data_Stream_Anomaly_Detection/blob/main/settings.py)
It contain the parameters to drive the code. If the parameters changes, output will change accordingly. It has 3 parameters:
1. Delay : time interval for generation of new data point
2. Outliers generation probability : if outliers generation probability is 0.2 then, probability that the generated point is anomaly is 0.2
3. Visualization : to display the run-time figure.

#### [model_prod.py](https://github.com/ParagGawai/Efficient_Data_Stream_Anomaly_Detection/blob/main/model_prod.py)
We are using isolation forest for the anomaly detection.
We generate the random numbers for the real-time data generation and fit the data into the isolation forest.
This code defines and trains an Isolation Forest model using scikit-learn's and store the model in the _isolation_forest.joblib_

#### [anomaly.py](https://github.com/ParagGawai/Efficient_Data_Stream_Anomaly_Detection/blob/main/anomaly.py)
This code defines a function anomaly_dect that performs anomaly detection using an Isolation Forest model previously stored.
1. The code sets up logging to write information to a file named _anomaly.log_.
2. The function anomaly_dect continuously generates random data points and checks for anomalies using a pre-trained Isolation Forest model.
3. Visualization is optional and controlled by the VISUALIZATION constant given in settings.py
4. If an anomaly is detected, it is logged, and the data point is marked in the visualization (if enabled).
5. The function pauses for a specified delay (DELAY) between iterations for visualization updates.
6. The loop runs indefinitely until a model file is not found or an explicit interruption occurs.

