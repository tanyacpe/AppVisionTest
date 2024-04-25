from ast import Return
import sys
import os
from PIL import Image as Img
from PySide6 import QtGui

# this is a pointer to the module object instance itself.
this = sys.modules[__name__]

# we can explicitly make assignments on it 
this.RobotPalletButton = None
this.RobotPalletLamp = None
this.RobotSendBuffer = None
this.RobotReadBuffer = None
this.RobotPos = None
this.RobotIsRunning = None
this.RobotIsIdle = None
this.RobotIsConnected = None
this.ControllerSendBuffer = None
this.ControllerReadBuffer = None

this.ReloadTCP = None
this.TCPNotMatch = None

this.ShowKeyboard = None

def initialize_RobotPalletButton(value):
    if (this.RobotPalletButton is None):
        this.RobotPalletButton = value
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.RobotPalletButton))

def initialize_RobotPalletLamp(value):
    if (this.RobotPalletLamp is None):
        this.RobotPalletLamp = value
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.RobotPalletLamp))

def initialize_RobotSendBuffer(value):
    if (this.RobotSendBuffer is None):
        this.RobotSendBuffer = value
        RobotSendBuffer = "Locally scoped RobotSendBuffer variable. Doesn't do anything here."
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.RobotSendBuffer))

def initialize_RobotReadBuffer(value):
    if (this.RobotReadBuffer is None):
        this.RobotReadBuffer = value
        RobotReadBuffer = "Locally scoped RobotSendBuffer variable. Doesn't do anything here."
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.RobotReadBuffer))

def initialize_RobotPos(value):
    if (this.RobotPos is None):
        this.RobotPos = value
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.RobotPos))

def initialize_RobotIsRunning():
    if (this.RobotIsRunning is None):
        this.RobotIsRunning = False
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.RobotIsRunning))

def initialize_RobotIsIdle():
    if (this.RobotIsIdle is None):
        this.RobotIsIdle = False
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.RobotIsIdle))

def initialize_RobotIsConnected():
    if (this.RobotIsConnected is None):
        this.RobotIsConnected = False
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.RobotIsConnected))

def initialize_ControllerSendBuffer():
    if (this.ControllerSendBuffer is None):
        this.ControllerSendBuffer = ""
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.ControllerSendBuffer))

def initialize_ControllerReadBuffer():
    if (this.ControllerReadBuffer is None):
        this.ControllerReadBuffer = ""
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.ControllerReadBuffer))

def initialize_ReloadTCP():
    if (this.ReloadTCP is None):
        this.ReloadTCP = False
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.ReloadTCP))
    
def initialize_TCPNotMatch():
    if (this.TCPNotMatch is None):
        this.TCPNotMatch = False
    else:
        msg = "Buff is already initialized to {0}."
        raise RuntimeError(msg.format(this.TCPNotMatch))
    
def initialize_ShowKeyboard():
    if (this.ShowKeyboard is None):
        this.ShowKeyboard = False
    else:
        msg = "ShowKeyboard is already initialized to {0}."
        raise RuntimeError(msg.format(this.ShowKeyboard))

def getIndexByString(value,strList) :
  l = len(strList)
  for i in range(l):
    if (value == strList[i]):
      return i
  return -1

def ListAllTemplateFile():
    global selectedTemplate
    folder = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(folder, "Template")
    filelist = []
    if(os.path.exists(template_path)):
        filelist = [
            fname for fname in os.listdir(template_path) if fname.endswith('.jpg') or fname.endswith('.jpeg') or fname.endswith('.png')
        ]
    return filelist

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)


def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def text_rgb(code):
    rgb = get_rgb_from_hex(code)
    return "rgb(" + str(rgb[0]) + ", " + str(rgb[1]) + ", " + str(rgb[2]) + ")"

def pil2pixmap(file_path,size):
    im = Img.open(fp = file_path).resize(size)
    if im.mode == "RGB":
        pass
    elif im.mode == "L":
        im = im.convert("RGBA")
    data = im.tostring('raw', "RGBA")
    qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap
