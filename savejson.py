import json
import os

def save_pallet_profile(name, size, index):
    # สร้างโครงสร้างข้อมูลสำหรับ JSON
    data = {
        "name": name,
        "size": size,
        "index": index
    }

    # ตรวจสอบและสร้างโฟลเดอร์ถ้ายังไม่มี
    folder_path = r"C:\\Users\\tanyawan\\Documents\\GitHub\\AppVisionTest\\pallet_info\\pallet" #"D:\Cobo_AppVision\AppVisionTest\pallet_info\pallet"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # สร้างชื่อไฟล์ตาม running number
    # หาไฟล์ที่มี running number สูงสุดในโฟลเดอร์ เพิ่ม 1 และใช้เป็น running number ใหม่
    running_number = 1
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if files:
        running_numbers = [int(f.split('.')[0]) for f in files if f.endswith('.json')]
        if running_numbers:
            running_number = max(running_numbers) + 1

    file_path = f"{folder_path}/{running_number}.dat"

    # บันทึกข้อมูลลงไฟล์ JSON
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Saved {name} to {file_path}")