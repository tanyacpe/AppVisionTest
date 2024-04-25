import json
import os
class Dojson: 
    def save_pallet_profile(name, size, index=None):
    # Create data structure for JSON
        data = {
            "name": name,
            "size": size
        }

        # Check and create the folder if it does not exist
        folder = os.getcwd()
        folder_path = os.path.join(folder, "pallet_info","pallet") #"D:\Cobo_AppVision\AppVisionTest\pallet_info\pallet"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if index is None:
            # If index is None, find the next available index
            max_index = 0
            for filename in os.listdir(folder_path):
                if filename.endswith('.dat'):
                    try:
                        file_index = int(filename.split('.')[0])
                        if file_index > max_index:
                            max_index = file_index
                    except ValueError:
                        continue
            # Increment the max index for new file creation
            index = max_index + 1
        else:
            # Ensure index is an integer
            index = int(index)

        # Set index in data dictionary
        data['index'] = index

        # Define the file path using the index
        file_path = os.path.join(folder_path, f"{index}.dat")

        # Save the data to a file, overwriting any existing file with the same index
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Saved {name} with index {index} to {file_path}")
    def delete_specific_dat_file(directory, filename_to_delete ):
    # ตรวจสอบว่าไฟล์ที่ต้องการลบมีนามสกุล .dat หรือไม่
        # if filename_to_delete.endswith('.dat'):
            # สร้างเส้นทางเต็มไปยังไฟล์
        ck=False
        file_path = os.path.join(directory,  f"{filename_to_delete}.dat")
            
            # ตรวจสอบว่าไฟล์มีอยู่จริง
        if os.path.exists(file_path):
                # ลบไฟล์
            os.remove(file_path)
            print(f"Deleted {file_path}")
            ck=True
        else:
            print(f"No file found at {file_path}")
        return ck
        # else:
            # print("Please provide a '.dat' file name.")
    def ListNameInfolder():
        directory_path = 'pallet_info/pallet/'

    # List to hold the names from all files
        names_list = []

        # Loop through all files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith('.dat'):
                # Full path to the .dat file
                file_path = os.path.join(directory_path, filename)
                
                # Reading the file and converting it to a Python dictionary
                try:
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        # Add the 'name' value to the list
                        names_list.append((data['name'], data['index']))
                
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file {filename}")
                except FileNotFoundError:
                    print(f"File {filename} not found")
                except Exception as e:
                    print(f"An error occurred with file {filename}: {e}")

        # At this point, names_list contains all the 'name' values from the .dat files
        # print(names_list)
        return names_list
    
    def find_pallet_profile(index):
        folder_path = "D:\Cobo_AppVision\AppVisionTest\pallet_info\pallet"
        folder = os.getcwd()
        folder_path = os.path.join(folder, "pallet_info","pallet")
        # ตรวจสอบว่าไฟล์ที่ต้องการค้นหามีอยู่จริงหรือไม่
        full_file_path = os.path.join(folder_path, f"{index}.dat")
        if os.path.exists(full_file_path):
            with open(full_file_path, 'r') as file:
                data = json.load(file)
                return data
        return None
    def on_button_clicked():
    # ตัวอย่างชื่อที่ต้องการค้นหา
        name_to_search = "Pallet Test"
        pallet_data = Dojson.find_pallet_profile(name_to_search)
        
        if pallet_data:
            print("พบข้อมูล:", pallet_data)
            # ใส่ข้อมูลลงในตัวแปรต่างๆ
            pallet_name = pallet_data['name']
            pallet_size = pallet_data['size']
            pallet_index = pallet_data['index']
            print(f"Name: {pallet_name}, Size: {pallet_size}, Index: {pallet_index}")
        else:
            print("ไม่พบข้อมูล")
        return pallet_data