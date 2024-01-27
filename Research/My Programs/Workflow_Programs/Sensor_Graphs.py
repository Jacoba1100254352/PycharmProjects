import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Configuration_Variables import *

def graph_sensor_data():
    """
    Generate and save plots comparing Instron and Arduino sensor data for each sensor.
    """
    for sensor_num in range(1, NUM_SENSORS + 1):
        # Load data from CSV files
        instron_data = pd.read_csv(INSTRON_DIR / f"Parsed Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv")
        updated_arduino_data = pd.read_csv(CALIBRATED_DIR / f"Updated Calibration Test {TEST_NUM} Sensor {sensor_num} Data.csv")

        # Extract time and force data
        instron_time, instron_force = instron_data["Time [s]"], abs(instron_data["Force [N]"])
        updated_arduino_time = updated_arduino_data["Time [s]"]
        updated_arduino_force = updated_arduino_data["Force [N]" if SIMPLIFY else f"Force{sensor_num} [N]"]

        # Setup plot
        plt.figure(figsize=(10, 6))
        plt.plot(updated_arduino_time, updated_arduino_force, label="Updated Arduino Data", color="red")
        plt.plot(instron_time, instron_force, label="Instron Data", color="blue")

        # Calculate and plot the difference
        min_length = min(len(instron_force), len(updated_arduino_force))
        difference = instron_force[:min_length] - updated_arduino_force[:min_length]
        plt.plot(instron_time[:min_length], difference, label="Difference (Instron - Updated Arduino)", color="green", linestyle="--")

        # Set plot labels and title
        plt.xlabel("Time [s]")
        plt.ylabel("Force [N]")
        plt.legend()
        plt.title(f"Comparison of Force Data for Sensor Set {SENSOR_SET}, Sensor {sensor_num}, Test {TEST_NUM}")
        plt.grid(True)

        # Save and show the plot
        plot_filename = PLOT_DIR / f"Calibration Test {TEST_NUM} Sensor {sensor_num} plot.png"
        plt.savefig(plot_filename, dpi=300)
        plt.show()
