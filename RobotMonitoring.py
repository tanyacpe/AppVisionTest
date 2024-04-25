# import loadconfig
import Utilities
import loadconfig
import time

from pyModbusTCP.client import ModbusClient
from pyModbusTCP.utils import encode_ieee, decode_ieee, long_list_to_word, word_list_to_long

from PySide6.QtCore import QThread

class Robot_update_thread(QThread):
    exit_robot_thread = False

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def exit_thread(self):
        self.exit_robot_thread = True

    def run(self):
        # init modbus client'
        robot_connect_fail_count = 4
        controller_config = loadconfig.loadConfig("controller")
        robot_config = loadconfig.loadConfig("robot")
        robot_address = "10.0.0.100" #controller_config["address"]
        robot_port = 502 #int(controller_config["port"])
        c = ModbusClient(host=robot_address, port=robot_port, auto_open=True, debug=False)
        c.timeout = 2
        # main read loop
        Utilities.RobotIsIdle = False
        Utilities.RobotPos = [0,217,170,180,0,0]
        
        while not self.exit_robot_thread:
            print(Utilities.RobotPos)
            # read 10 bits (= coils) at address 0, store result in coils list
            #coils_l = c.read_discrete_inputs(8, 5)
            try:
                robot_status = c.read_discrete_inputs(8, 3)
                Utilities.RobotPalletButton = c.read_discrete_inputs(18, 10)
                

                if robot_status is not None:
                    for idx in range(10):
                        c.write_single_coil((idx + 50), Utilities.RobotPalletLamp[idx]) #Pallet 1 Lamp
                    Utilities.RobotIsRunning = robot_status[2]
                    Utilities.RobotIsIdle = robot_status[0]
                    if "ROBOT_ON_OK" in Utilities.ControllerReadBuffer:
                        Utilities.ControllerReadBuffer = ""
                    Utilities.RobotIsConnected = True
                else:
                    Utilities.RobotIsConnected = False
                    robot_connect_fail_count += 1
                    Utilities.RobotIsIdle = False

                if robot_connect_fail_count>5:
                    Utilities.ControllerSendBuffer = "ROBOT_ON"
                    robot_connect_fail_count = 0

                robot_pos = c.read_input_registers(406,12)
                
                if robot_pos is not None:
                    tmpPos = [decode_ieee(f) for f in word_list_to_long(robot_pos)]
                    robot_tcp = c.read_input_registers(430,12)
                    if robot_tcp is not None:
                        
                        tmpTCP = [decode_ieee(f) for f in word_list_to_long(robot_tcp)]
                        
                        Utilities.RobotPos = tmpPos
                        
                        if Utilities.ReloadTCP: #Need reload new from setting TCP
                            print("robot_monitoring: reload TCP")
                            robot_config = loadconfig.loadConfig("robot")
                            Utilities.ReloadTCP = False
                    
                        app_tcp = [float(robot_config["tcp_gripper_x"]),float(robot_config["tcp_gripper_y"]),float(robot_config["tcp_gripper_z"]),
                                float(robot_config["tcp_gripper_rx"]),float(robot_config["tcp_gripper_ry"]),float(robot_config["tcp_gripper_rz"])]
                        
                        if abs(app_tcp[0] - tmpTCP[0]) > 0.01 or abs(app_tcp[1] - tmpTCP[1]) > 0.01 or abs(app_tcp[2] - tmpTCP[2]) > 0.01 \
                            or abs(app_tcp[3] - tmpTCP[3]) > 0.01 or abs(app_tcp[4] - tmpTCP[4]) > 0.01 or abs(app_tcp[5] - tmpTCP[5]) > 0.01:
                            Utilities.TCPNotMatch = True
                        else:
                            Utilities.TCPNotMatch = False
            except:
                print("Robot not connect")
            time.sleep(0.2)