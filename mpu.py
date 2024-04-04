import smbus
import time
import json

# I2C address of the MPU9250
MPU9250_ADDRESS = 0x68

# Register addresses for the accelerometer data
ACCEL_XOUT_H = 0x3B

# Initialize the I2C bus
bus = smbus.SMBus(1)  # Use bus 1 for Raspberry Pi 3, 4, or 400

# Wake up the MPU9250
bus.write_byte_data(MPU9250_ADDRESS, 0x6B, 0)

# Initial calibration: Read and discard initial values
calibration_values = bus.read_i2c_block_data(MPU9250_ADDRESS, ACCEL_XOUT_H, 6)
# print("Calibration Values:", calibration_values)

def mpu_data():
    # Read accelerometer data
    accel_data = bus.read_i2c_block_data(MPU9250_ADDRESS, ACCEL_XOUT_H, 6)

    # Combine high and low bytes for each axis
    AcX = accel_data[0] << 8 | accel_data[1]
    AcY = accel_data[2] << 8 | accel_data[3]
    AcZ = accel_data[4] << 8 | accel_data[5]

    # Subtract the calibration values
    AcX -= calibration_values[0] << 8 | calibration_values[1]
    AcY -= calibration_values[2] << 8 | calibration_values[3]
    AcZ -= calibration_values[4] << 8 | calibration_values[5]

    # Scale the accelerometer data based on the full-scale range (�2g)
    scale_factor = 2.0 / 32768.0  # 32768 is the maximum value for a 16-bit signed integer
    AcX = AcX * scale_factor
    AcY = AcY * scale_factor
    AcZ = AcZ * scale_factor

    # Print the raw accelerometer data and scaled values
    # print(f"Raw Acceleration - X: {accel_data[0]}, Y: {accel_data[2]}, Z: {accel_data[4]}")
    # print(f"Scaled Acceleration - X: {AcX:.2f} g, Y: {AcY:.2f} g, Z: {AcZ:.2f} g")
    return f"{AcX:.2f}/{AcY:.2f}/{AcZ:.2f}"

