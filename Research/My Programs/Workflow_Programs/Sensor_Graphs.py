import matplotlib.pyplot as plt
import pandas as pd

from Configuration_Variables import *


def graph_sensor_data():
    """
    Generate and save plots comparing Instron and Arduino sensor data for each sensor.
    """
    for sensor_num in range(1, NUM_SENSORS + 1):
        # Load data from CSV files
        instron_data = pd.read_csv(get_data_filepath(PARSED_INSTRON_DIR, sensor_num))
        updated_arduino_data = pd.read_csv(get_data_filepath(CALIBRATED_ARDUINO_DIR, sensor_num))

        # Extract time and force data
        instron_time, instron_force = instron_data["Time [s]"], instron_data["Force [N]"]
        updated_arduino_time = updated_arduino_data["Time [s]"]
        updated_arduino_force = updated_arduino_data["Force [N]" if SIMPLIFY else f"Force{sensor_num} [N]"]

        # Setup plot
        plt.figure(figsize=(10, 6))
        plt.plot(updated_arduino_time, updated_arduino_force, label="Updated Arduino Data", color="red")
        plt.plot(instron_time, instron_force, label="Instron Data", color="blue")

        # Calculate and plot the difference
        difference = instron_force - updated_arduino_force
        plt.plot(instron_time, difference, label="Difference (Instron - Updated Arduino)", color="green",
                 linestyle="--")

        # Set plot labels and title
        plt.xlabel("Time [s]")
        plt.ylabel("Force [N]")
        plt.legend()
        plt.title(f"Comparison of Force Data for {SENSOR_SET_DIR}, Sensor {sensor_num}, Test {TEST_NUM}")
        plt.grid(True)

        # Save and show the plot
        plot_filename = get_data_filepath(PLOTS_DIR, sensor_num)
        plt.savefig(plot_filename, dpi=300)
        plt.show()
