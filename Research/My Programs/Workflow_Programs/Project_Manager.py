from Align_Data import align_data
from Apply_Calibrations_for_Graphing import apply_calibration_coefficients
from Calculate_Linear_Fit_Sensor_Calibrations import calculate_coefficients
from Raw_to_CSV import write_raw_data_to_csv
from Sensor_Graphs import graph_sensor_data

# Convert new data to CSV # Raw_to_CSV.py
write_raw_data_to_csv()

# Align data along the x (time) axis # Align_Data.py
align_data()

# Calculate new calibration coefficients # Calculate_Linear_Fit_Sensor_Calibrations.py
calculate_coefficients()

# Apply new calibration coefficients to the data for graphing and verification # Apply_Calibrations_for_Graphing.py
apply_calibration_coefficients()

# Graph the "new" calibrated data created from the previous step # Sensor_Graphs.py
graph_sensor_data()
