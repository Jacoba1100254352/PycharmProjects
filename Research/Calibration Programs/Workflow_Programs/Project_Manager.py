from Align_Data import align_data
from Apply_Calibrations_for_Graphing import apply_calibration_coefficients
from Calculate_Linear_Fit_Sensor_Calibrations import calculate_coefficients

# Convert new data to CSV # Raw_to_CSV.py
# write_raw_data_to_csv()

# Interpolate the data # Interpolate_Data.py # NOTE: Ignore this for now
# interpolate_all_sensors()

# Align data along the x (time) axis # Align_Data.py
align_data()

# Calculate new calibration coefficients # Calculate_Linear_Fit_Sensor_Calibrations.py
calculate_coefficients()

# Apply new calibration coefficients to the data for graphing and verification # Apply_Calibrations_for_Graphing.py
apply_calibration_coefficients()
