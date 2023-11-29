import serial
import time

# Set up the serial line
port = 'COM5'
ser = serial.Serial(port, 115200)  
ser.flushInput()

# Open a file for writing

with open('serial_data.txt', 'w') as file:
    while True:
        try:
            # Read a line from the serial port
            ser_bytes = ser.readline()

            # Decode bytes to string
            decoded_bytes = ser_bytes.decode('utf-8').rstrip()

            # Write to the file
            file.write(decoded_bytes + '\n')
            file.flush()  # Ensure data is written to the file

            # Optional: print to console
            print(decoded_bytes)

        except KeyboardInterrupt:
            print("Keyboard Interrupt: Exiting...")
            break
        except Exception as e:
            print("Error:", e)
            break

# Close the serial connection
ser.close()
