'''This code defines a function anomaly_dect that performs anomaly detection using an Isolation Forest model'''

'''
1. The code sets up logging to write information to a file named 'anomaly.log'.
2. The function anomaly_dect continuously generates random data points and checks for anomalies using a pre-trained Isolation Forest model.
3. Visualization is optional and controlled by the VISUALIZATION constant given in settings.py
4. If an anomaly is detected, it is logged, and the data point is marked in the visualization (if enabled).
5. The function pauses for a specified delay (DELAY) between iterations for visualization updates.
6. The loop runs indefinitely until a model file is not found or an explicit interruption occurs.
'''


# Importing necessary libraries
import os
import random
import time
from datetime import datetime
from joblib import load
import logging
import matplotlib.pyplot as plt
import numpy as np

# Importing constants from a settings module
from settings import DELAY, OUTLIERS_GENERATION_PROBABILITY, VISUALIZATION

# Configuring logging to write to a file named 'anomaly.log'
logging.basicConfig(filename='anomaly.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


# List to store incoming real time data
data_ls = []

def anomaly_dect():
    _id = 0

    # Visualization setup
    if VISUALIZATION:
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set_facecolor("black")
        fig.show()
    
    while True:
        # Generating some abnormal observations based on a given probability in the settings.py
        if random.random() <= OUTLIERS_GENERATION_PROBABILITY:
            X_test = np.random.uniform(low=-4, high=4, size=(1, 1))
        else:
            X = 0.3 * np.random.randn(1, 1)
            X_test = (X + np.random.choice(a=[2, -2], size=1, p=[0.5, 0.5]))

        X_test = np.round(X_test, 3).tolist()

        current_time = datetime.utcnow().isoformat()

        # Creating a record for the incoming data
        record = {"id": _id, "data": X_test, "current_time": current_time}
        print(f"Incoming: {record}")


        # Loading the Isolation Forest model from the file if exists
        try:
            model_path = os.path.abspath("isolation_forest.joblib")
            clf = load(model_path)
        except:
            logging.warning(f"Model file not found")
            print(f'Model file not available')
            break

        data = record['data']        
        data_ls.append(data[0][0])
        prediction = clf.predict(data)

        # Visualization update
        if VISUALIZATION:
            ax.plot(data_ls,color='b')
            fig.canvas.draw()
            ax.set_xlim(left=0, right=_id+2)
        
        # Checking if an anomaly is detected
        if prediction[0] == -1:
            score = clf.score_samples(data)
            record["score"] = np.round(score, 3).tolist()
            if VISUALIZATION:
                plt.scatter(_id,data_ls[_id],color='r',linewidth=2)
            logging.info(f"Anomaly Detected : {record}")
            print(f'Anamoly Detected : {record}')
            
        _id += 1
        plt.pause(DELAY)
        # time.sleep(DELAY)
    plt.show()