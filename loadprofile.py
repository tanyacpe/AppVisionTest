import json
import base64
import os
import base64
import cv2
import numpy as np

class loadprofile:
    def ListAllProfile(profilecat): 
        print("ListAllProfile : " + profilecat)
        folder = os.getcwd()
        profile_path = os.path.join(folder, "pallet_info",profilecat)

        filelist = []
        names_list = []

        if(os.path.exists(profile_path)):
            filelist = []
            for filename in os.listdir(profile_path):
                if filename.endswith('.dat'):
                    name,ext = os.path.splitext(filename)
                    filelist.append(name)
                    file_path = os.path.join(profile_path, filename)
                    try:
                        with open(file_path, 'r') as file:
                            data = json.load(file)
                            # Add the 'name' value to the list
                            names_list.append([data['name'], data['index']])
                
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from file {file_path}")
                    except FileNotFoundError:
                        print(f"File {file_path} not found")
                    except Exception as e:
                        print(f"An error occurred with file {file_path}: {e}")
            output = sorted(names_list, key=lambda x: x[1])
        return output
    
    def LoadProfileData(profilecat,filename):
        print("LoadProfileData : " + filename)
        folder = os.getcwd()
        profile_path = os.path.join(folder, "pallet_info",profilecat,filename +'.dat')
        if(os.path.exists(profile_path)):
            try:
                with open(profile_path, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file {profile_path}")
            except FileNotFoundError:
                print(f"File {profile_path} not found")
            except Exception as e:
                print(f"An error occurred with file {profile_path}: {e}")
        return data
    
    def SaveProfileData(profilecat,profilename,data,index=None):
        print("SaveProfileData : " + profilename)
        folder = os.getcwd()
        profile_path = os.path.join(folder, "pallet_info",profilecat)
        if not os.path.exists(profile_path):
            os.makedirs(profile_path)
        max_idx = 0
        if index is None:
            names_list=[]
            for filename in os.listdir(profile_path):
                if filename.endswith('.dat'):
                    file_path = os.path.join(profile_path, filename)
                    try:
                        with open(file_path, 'r') as file:
                            data = json.load(file)
                            # Add the 'name' value to the list
                            names_list.append([data['name'], data['index']])
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from file {file_path}")
                    except FileNotFoundError:
                        print(f"File {file_path} not found")
                    except Exception as e:
                        print(f"An error occurred with file {file_path}: {e}")
            # Find the maximum value based on the second element (numeric value)
            max_value = max(names_list, key=lambda x: x[1])
            # Extract the numeric value from the max_value
            max_idx = max_value[1]
            # Print the result
            print(f"Maximum idx: {max_idx}")
            index = max_idx + 1
        else:
            index = int(index)
        
        try:
            save_file_path = os.path.join(profile_path, f'{index}.dat')
            with open(save_file_path, 'r') as file:
                json.dump(data, file, indent=4)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {file_path}")
        except FileNotFoundError:
            print(f"File {file_path} not found")
        except Exception as e:
            print(f"An error occurred with file {file_path}: {e}")