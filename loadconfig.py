import json
import base64
import os
from PIL import Image, ImageTk
from io import BytesIO
import base64
import cv2
import numpy as np

def ListAllProfile():
    folder = os.getcwd()
    template_path = os.path.join(folder, "profile")

    filelist = []

    if(os.path.exists(template_path)):
        filelist = []
        for fname in os.listdir(template_path):
            if fname.endswith('.prf'):
                name,ext = os.path.splitext(fname)
                filelist.append(name)  
            
    return filelist

def loadProfile(filename):
    print("loadProfile : " + filename)
    try:
        folder = os.getcwd()
        template_path = os.path.join(folder, "profile")
       
        f = open(template_path + "/" + filename + ".prf")
        data = json.load(f)
        f.close()
        if ("template" in data): 
            if (data["template"] != ""):
                base64_bytes = data["template"].encode("ascii")
                nparr = np.fromstring(base64.b64decode(base64_bytes), np.uint8)
                img = cv2.imdecode(nparr, flags=1)
                data["template"] = img
        if "contour" in data:
            if (data["contour"] != ""):
                data["contour"] = np.asarray(data["contour"])
        return data
    except:
        return {}

def saveProfile(filename,data):
    print("saveProfile : " + filename)
    #try:
    retval, buffer = cv2.imencode('.jpg', data["template"])
    base64_bytes = base64.b64encode(buffer)
    base64_string = base64_bytes.decode("ascii")
    data["template"] = base64_string
    if "contour" in data:
        data["contour"] = data["contour"].tolist()
    with open("profile/" + filename + ".prf", "w") as outfile:
        json.dump(data, outfile)

    if (data["template"] != ""):
        base64_bytes = data["template"].encode("ascii")
        nparr = np.fromstring(base64.b64decode(base64_bytes), np.uint8)
        img = cv2.imdecode(nparr, flags=1)
        data["template"] = img
    if ("contour" in data):
        data["contour"] = np.asarray(data["contour"])
    return True
    #except:
    #    return False

def deleteProfile(filename):
    path = "profile/" + filename + ".prf"
    if os.path.exists(path):
        try:
            os.remove(path)
            return True
        except:
            return False
    else:
        return False

def loadConfig(filename):
  print("loadConfig : " + filename)
  try:
    f = open("settings/" + filename + ".dat")
    data = json.load(f)
    f.close()
    return data
  except:
    return {}

def saveConfig(filename,config):
  print("saveConfig : " + filename)
  try:
    with open("settings/" + filename + ".dat", "w") as outfile:
      json.dump(config, outfile)
    return True
  except:
    return False


#import cv2
#import base64

#cap = cv2.VideoCapture(0)
#retval, image = cap.read()
#cap.release()

## Convert captured image to JPG
#retval, buffer = cv2.imencode('.jpg', image)

## Convert to base64 encoding and show start of data
#jpg_as_text = base64.b64encode(buffer)
#print(jpg_as_text[:80])

## Convert back to binary
#jpg_original = base64.b64decode(jpg_as_text)

## Write to a file to show conversion worked
#with open('test.jpg', 'wb') as f_output:
#    f_output.write(jpg_original)