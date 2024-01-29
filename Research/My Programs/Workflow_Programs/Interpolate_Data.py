# Program 2: Interpolating Data from CSV

import numpy as np
import pandas as pd

from Configuration_Variables import *


# Define a function to interpolate Instron data
def interpolate_instron_data(instron_data):
    instron_data['Time [s]'] = pd.to_numeric(instron_data['Time [s]'])
    instron_data.set_index('Time [s]', inplace=True)

    max_time = instron_data.index.max()
    new_time_index = pd.Index(np.arange(0, max_time + 0.02, 0.02), name='Time [s]')

    interpolated_df = instron_data.reindex(new_time_index).interpolate(method='linear')
    interpolated_df = interpolated_df.reset_index()
    interpolated_df = interpolated_df.round({'Time [s]': 2, 'Displacement [mm]': 4, 'Force [N]': 4})

    return interpolated_df


# Function to process and interpolate data from CSV, then save back to CSV
def interpolate_and_save_csv(read_filename, write_filename):
    data = pd.read_csv(read_filename)
    interpolated_data = interpolate_instron_data(data)
    interpolated_data.to_csv(write_filename, index=False)
    print(f"Interpolated data saved to {write_filename}")


# Main execution to process all sensors
def interpolate_all_sensors():
    for sensor_num in range(1, NUM_SENSORS + 1):
        read_filename = get_data_filepath(PARSED_INSTRON_DIR, sensor_num)
        write_filename = get_data_filepath(PARSED_INSTRON_DIR, sensor_num)  # INTERPOLATED_INSTRON_DIR
        interpolate_and_save_csv(read_filename, write_filename)
