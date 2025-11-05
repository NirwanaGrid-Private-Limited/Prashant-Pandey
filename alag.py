import segregation
from segregation import identify_device
import pandas as pd
import os
import time 

file_path = "data_today_heavy_device.csv"
last_size = 0

while True:
    if os.path.exists(file_path):
        current_size = os.path.getsize(file_path)

        if current_size != last_size:
            df = pd.read_csv(file_path)

            
            print("\n🆕 New row added:")
            print(df.tail(1).to_string(index=False))
            last_row = df.tail(1)
            power_value = last_row['power'].values[0]
            
            dict = identify_device(power_value)
            print(dict)


            last_size = current_size
    else:
        print("⚠️ File not found. Waiting for file creation...")

    time.sleep(3)


