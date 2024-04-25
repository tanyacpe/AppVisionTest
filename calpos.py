import numpy as np
import matplotlib.pyplot as plt
import math
from math import atan2, cos, sin, sqrt, pi

def get3dDistance(startCoords, endCoords):
        dx = math.pow((startCoords[0] - endCoords[0]), 2)
        dy = math.pow((startCoords[1] - endCoords[1]), 2)
        dz = math.pow((startCoords[2] - endCoords[2]), 2)
        return math.sqrt(dx + dy + dz)

def normalizeVec(x,y):
    distance = np.sqrt(x*x+y*y)
    return x/distance, y/distance

def makeOffsetPoly(oldX, oldY, offset, outer_ccw = 1):
    num_points = len(oldX)
    newX = []
    newY = []
    for curr in range(num_points):
        prev = (curr + num_points - 1) % num_points
        next = (curr + 1) % num_points

        vnX =  oldX[next] - oldX[curr]
        vnY =  oldY[next] - oldY[curr]
        vnnX, vnnY = normalizeVec(vnX,vnY)
        nnnX = vnnY
        nnnY = -vnnX

        vpX =  oldX[curr] - oldX[prev]
        vpY =  oldY[curr] - oldY[prev]
        vpnX, vpnY = normalizeVec(vpX,vpY)
        npnX = vpnY * outer_ccw
        npnY = -vpnX * outer_ccw

        bisX = (nnnX + npnX) * outer_ccw
        bisY = (nnnY + npnY) * outer_ccw

        bisnX, bisnY = normalizeVec(bisX,  bisY)

        bislen = offset /  np.sqrt((1 + nnnX*npnX + nnnY*npnY)/2)

        newX.append(oldX[curr] + bislen * bisnX)
        newY.append(oldY[curr] + bislen * bisnY)
    return newX,newY

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def cal_pos_arrange_box_pat0(pallet_pos,bx,by,bz,max_layer,box_qty,gap):
    # base = pallet_pos
    # xN1 = [base[0][0],base[1][0],base[2][0],base[3][0]]
    # yN1 = [base[0][1],base[1][1],base[2][1],base[3][1]]
    # xN1.append(xN1[0])
    # yN1.append(yN1[0])
    # plt.plot(xN1, yN1)

    xN = [pallet_pos[0][0],pallet_pos[1][0],pallet_pos[2][0],pallet_pos[3][0]]
    yN = [pallet_pos[0][1],pallet_pos[1][1],pallet_pos[2][1],pallet_pos[3][1]]
    width, length, height = bx,by,bz
    num_box=box_qty
    gap_mm=gap
    num_layer = max_layer #จำนวนสูงสุดของชั้นที่เรียง
    idx_pattern = 0
    pallet_pos_list = pallet_pos
    result_center_points = []

    pos_a = pallet_pos_list[0]
    pos_b = pallet_pos_list[1]
    pos_c = pallet_pos_list[2]
    pos_d = pallet_pos_list[3]
    pallet_distY = get3dDistance(pos_a,pos_b) # Row
    pallet_distX = get3dDistance(pos_b,pos_c) # Column
    print("Return distX .mm: ", pallet_distY)
    print("Return distY .mm: ", pallet_distX)

    if(idx_pattern == 0):
        count_box = num_box
        count_row=0
        #count_col=0
        count_layer=0
        count_boxrow=0
        count_boxcol=0
        count_boxlayer=0
        distance_X = pallet_distX
        distance_Y = pallet_distY
        remain_box = 0
        while(count_box>0):
            if(count_boxlayer>0 and count_box>0):
                count_boxlayer+=1
                amout_boxperlayer = count_boxrow*count_boxcol
                count_layer = count_box//amout_boxperlayer
                remain_box = count_box%amout_boxperlayer
                count_box = count_box - (count_layer*amout_boxperlayer) - remain_box
                count_boxlayer+=count_layer
                if(count_layer >0 and count_box%amout_boxperlayer > 0):#ชั้นที่มีเศษ
                    count_boxlayer+=1

            if(distance_Y >= length and distance_X >= width):
                while(distance_Y-length >= 0 and distance_X - width >=0 and count_box > 0):
                    count_boxrow+=1
                    count_box-=1
                    if(distance_Y-length-gap_mm >= 0):
                        distance_Y = distance_Y-length-gap_mm
                    elif(distance_Y-length >= 0):
                        distance_Y = distance_Y-length
                else:
                    if(count_box > 0 and distance_X - width >=0):
                        while(distance_X - width >=0 and count_box > 0):
                            count_boxcol+=1
                            if(count_row >= 1):
                                count_box = count_box-count_boxrow
                            count_row+=1
                            if(distance_X-width-gap_mm >= 0):
                                distance_X = distance_X-width-gap_mm
                            elif(distance_Y-length >= 0):
                                distance_X = distance_X-width
                        else:
                            count_boxlayer+=1
        print("Return count_boxrow: ", count_boxrow, ", count_boxcol: ",count_boxcol, " count_boxlayer: ",count_boxlayer)
        print("Return remain_box: ",remain_box)
        print("Return Remain distance_X: ", distance_X, ", Remain distance_Y: ",distance_Y)
        
        delta_x = xN[-1] - xN[0]
        delta_y = yN[-1] - yN[0]

        # ตรวจสอบค่า offset_x
        if delta_x > 0:
            offset_x = 1
        else: 
            offset_x = -1

        if(num_layer>=count_boxlayer):
            count_box = 0
            for l in range(count_boxlayer):
                b_distX = pallet_distX - distance_X/2
                b_distY = pallet_distY - distance_Y/2
                for c in range(count_boxcol):
                    for r in range(count_boxrow):
                        if(count_box<num_box):
                            if(r==0 and c==0):
                                newDisX = (distance_X/2) + ((width)/2)
                                newDisY = (distance_Y/2) + ((length)/2)
                            elif(r>0 and c==0):
                                newDisX = (distance_X/2) + ((width)/2)
                                newDisY = (distance_Y/2) + ((length)/2) + (length*(r)) + gap_mm
                            elif(r==0 and c>0):
                                newDisX = (distance_X/2) + ((width)/2) + (width*(c)) + gap_mm
                                newDisY = (distance_Y/2) + ((length)/2)
                            elif(r>0 and c>0):
                                newDisX = (distance_X/2) + ((width)/2) + (width*(c)) + gap_mm
                                newDisY = (distance_Y/2) + ((length)/2) + (length*(r)) + gap_mm
                            newDisZ = height * (l+1)
                            count_box+=1

                            top_buttom_X = []
                            top_buttom_Y = []
                            left_right_X = []
                            left_right_Y = []
                            top_buttom_X,top_buttom_Y = makeOffsetPoly(xN, yN, newDisX*offset_x)#newDisX*offset_x)
                            left_right_X,left_right_Y = makeOffsetPoly(xN, yN, newDisY*offset_x)#newDisY*offset_y)
                            # point_0 = line_intersection(([[top_buttom_X[0], top_buttom_Y[0]],[top_buttom_X[1], top_buttom_Y[1]]]), ([[left_right_X[1], left_right_Y[1]],[left_right_X[2], left_right_Y[2]]]))
                            point_1 = line_intersection(([[top_buttom_X[2], top_buttom_Y[2]],[top_buttom_X[3], top_buttom_Y[3]]]), ([[left_right_X[1], left_right_Y[1]],[left_right_X[2], left_right_Y[2]]]))
                            # point_2 = line_intersection(([[top_buttom_X[0], top_buttom_Y[0]],[top_buttom_X[1], top_buttom_Y[1]]]), ([[left_right_X[3], left_right_Y[3]],[left_right_X[0], left_right_Y[0]]]))
                            # point_3 = line_intersection(([[top_buttom_X[2], top_buttom_Y[2]],[top_buttom_X[3], top_buttom_Y[3]]]), ([[left_right_X[3], left_right_Y[3]],[left_right_X[0], left_right_Y[0]]]))
                            point_Z=pallet_pos[0][2]+newDisZ
                            # plt.plot(point_1[0], point_1[1], 'o')
                            result_center_points.append([point_1[0], point_1[1],point_Z,pallet_pos[0][3],pallet_pos[0][4],pallet_pos[0][5]])
            # plt.show()
            return result_center_points
        else:
            print("Error, that over max layer")
            return None


def test(self):
    # base = [[464.0, -500.0, 100.0, 0.0, 0.0, 90.0],[464.0, 500.0, 100.0, 0.0, 0.0, 90.0], [-736.0, 500.0, 100.0, 0.0, 0.0, 90.0], [-736.0, -500.0, 100.0, 0.0, 0.0, 90.0]]
    base = pallet_pos = [[-678.68, -616.83, 100.0, 0.0, 0.0, 90.0], [-559.03, 375.98, 100.0, 0.0, 0.0, 90.0], [632.35, 232.41, 100.0, 0.0, 0.0, 90.0],[512.7, -760.41, 100.0, 0.0, 0.0, 90.0]]
    xN1 = [base[0][0],base[1][0],base[2][0],base[3][0]]
    yN1 = [base[0][1],base[1][1],base[2][1],base[3][1]]

    xN1.append(xN1[0])
    yN1.append(yN1[0])
    plt.plot(xN1, yN1)

    # pallet_pos = [[464.0, -500.0, 100.0, 0.0, 0.0, 90.0],[464.0, 500.0, 100.0, 0.0, 0.0, 90.0], [-736.0, 500.0, 100.0, 0.0, 0.0, 90.0], [-736.0, -500.0, 100.0, 0.0, 0.0, 90.0]]
    pallet_pos = [[-678.68, -616.83, 100.0, 0.0, 0.0, 90.0], [-559.03, 375.98, 100.0, 0.0, 0.0, 90.0], [632.35, 232.41, 100.0, 0.0, 0.0, 90.0],[512.7, -760.41, 100.0, 0.0, 0.0, 90.0]]
    xN = [pallet_pos[0][0],pallet_pos[1][0],pallet_pos[2][0],pallet_pos[3][0]]
    yN = [pallet_pos[0][1],pallet_pos[1][1],pallet_pos[2][1],pallet_pos[3][1]]




    # offset_top_buttom = 270/2
    # offset_left_right = 180/2

    # top_buttom_X = []
    # top_buttom_Y = []
    # left_right_X = []
    # left_right_Y = []
    # top_buttom_X,top_buttom_Y = makeOffsetPoly(xN, yN, offset_top_buttom)
    # left_right_X,left_right_Y = makeOffsetPoly(xN, yN, offset_left_right)

    # xN.append(xN[0])
    # yN.append(yN[0])
    # plt.plot(xN, yN)

    # point_0 = line_intersection(([[top_buttom_X[0], top_buttom_Y[0]],[top_buttom_X[1], top_buttom_Y[1]]]), ([[left_right_X[1], left_right_Y[1]],[left_right_X[2], left_right_Y[2]]]))
    # point_1 = line_intersection(([[top_buttom_X[2], top_buttom_Y[2]],[top_buttom_X[3], top_buttom_Y[3]]]), ([[left_right_X[1], left_right_Y[1]],[left_right_X[2], left_right_Y[2]]]))
    # point_2 = line_intersection(([[top_buttom_X[0], top_buttom_Y[0]],[top_buttom_X[1], top_buttom_Y[1]]]), ([[left_right_X[3], left_right_Y[3]],[left_right_X[0], left_right_Y[0]]]))
    # point_3 = line_intersection(([[top_buttom_X[2], top_buttom_Y[2]],[top_buttom_X[3], top_buttom_Y[3]]]), ([[left_right_X[3], left_right_Y[3]],[left_right_X[0], left_right_Y[0]]]))
    # plt.plot(point_0[0], point_0[1], 'o')
    # plt.plot(point_1[0], point_1[1], 'o')
    # plt.plot(point_2[0], point_2[1], 'o')
    # plt.plot(point_3[0], point_3[1], 'o')
    # plt.plot([point_0[0],point_1[0],point_3[0],point_2[0],point_0[0]], [point_0[1],point_1[1],point_3[1],point_2[1],point_0[1]])

    # plt.show()

    width, length, height = 300.00,400.00,150.00
    #   X,      Y,      Z
    num_box=10
    gap_mm=10
    num_layer = 5 #จำนวนสูงสุดของชั้นที่เรียง
    idx_pattern = 0
    pallet_pos_list = pallet_pos
    result_center_points = []

    pos_a = pallet_pos_list[0]
    pos_b = pallet_pos_list[1]
    pos_c = pallet_pos_list[2]
    pos_d = pallet_pos_list[3]
    pallet_distY = get3dDistance(pos_a,pos_b) # Row
    pallet_distX = get3dDistance(pos_b,pos_c) # Column
    print("Return distX .mm: ", pallet_distY)
    print("Return distY .mm: ", pallet_distX)

    if(idx_pattern == 0):
        count_box = num_box
        count_row=0
        #count_col=0
        count_layer=0
        count_boxrow=0
        count_boxcol=0
        count_boxlayer=0
        distance_X = pallet_distX
        distance_Y = pallet_distY
        remain_box = 0
        while(count_box>0):
            if(count_boxlayer>0 and count_box>0):
                count_boxlayer+=1
                amout_boxperlayer = count_boxrow*count_boxcol
                count_layer = count_box//amout_boxperlayer
                remain_box = count_box%amout_boxperlayer
                count_box = count_box - (count_layer*amout_boxperlayer) - remain_box
                count_boxlayer+=count_layer
                if(count_layer >0 and count_box%amout_boxperlayer > 0):#ชั้นที่มีเศษ
                    count_boxlayer+=1

            if(distance_Y >= length and distance_X >= width):
                while(distance_Y-length >= 0 and distance_X - width >=0 and count_box > 0):
                    count_boxrow+=1
                    count_box-=1
                    if(distance_Y-length-gap_mm >= 0):
                        distance_Y = distance_Y-length-gap_mm
                    elif(distance_Y-length >= 0):
                        distance_Y = distance_Y-length
                else:
                    if(count_box > 0 and distance_X - width >=0):
                        while(distance_X - width >=0 and count_box > 0):
                            count_boxcol+=1
                            if(count_row >= 1):
                                count_box = count_box-count_boxrow
                            count_row+=1
                            if(distance_X-width-gap_mm >= 0):
                                distance_X = distance_X-width-gap_mm
                            elif(distance_Y-length >= 0):
                                distance_X = distance_X-width
                        else:
                            count_boxlayer+=1
        print("Return count_boxrow: ", count_boxrow, ", count_boxcol: ",count_boxcol, " count_boxlayer: ",count_boxlayer)
        print("Return remain_box: ",remain_box)
        print("Return Remain distance_X: ", distance_X, ", Remain distance_Y: ",distance_Y)

        # # หาจำนวนจุดของรูปร่าง
        # num_points = len(xN)
        # # หาผลรวมของทุกจุดของ x และ y
        # sum_x = sum(xN)
        # sum_y = sum(yN)

        # # หาค่าเฉลี่ยของ x และ y
        # avg_x = sum_x / num_points
        # avg_y = sum_y / num_points

        # # ตรวจสอบค่า offset_x โดยการตรวจสอบว่าเฉลี่ยของ xN มากกว่า 0 หรือน้อยกว่า 0
        # if avg_x > 0:
        #     offset_x = 1
        # else:
        #     offset_x = -1

        # # ตรวจสอบค่า offset_y โดยการตรวจสอบว่าเฉลี่ยของ yN มากกว่า 0 หรือน้อยกว่า 0
        # if avg_y > 0:
        #     offset_y = 1
        # else:
        #     offset_y = -1

        count_box = 0
        # num_box=6
        for l in range(count_boxlayer):
            b_distX = pallet_distX - distance_X/2
            b_distY = pallet_distY - distance_Y/2
            for c in range(count_boxcol):
                for r in range(count_boxrow):
                    if(count_box<num_box):
                        if(r==0 and c==0):
                            newDisX = (distance_X/2) + ((width)/2)
                            newDisY = (distance_Y/2) + ((length)/2)
                        elif(r>0 and c==0):
                            newDisX = (distance_X/2) + ((width)/2)
                            newDisY = (distance_Y/2) + ((length)/2) + (length*(r)) + gap_mm
                        elif(r==0 and c>0):
                            newDisX = (distance_X/2) + ((width)/2) + (width*(c)) + gap_mm
                            newDisY = (distance_Y/2) + ((length)/2)
                        elif(r>0 and c>0):
                            newDisX = (distance_X/2) + ((width)/2) + (width*(c)) + gap_mm
                            newDisY = (distance_Y/2) + ((length)/2) + (length*(r)) + gap_mm
                        newDisZ = height * (l+1)
                        count_box+=1

                        top_buttom_X = []
                        top_buttom_Y = []
                        left_right_X = []
                        left_right_Y = []
                        top_buttom_X,top_buttom_Y = makeOffsetPoly(xN, yN, newDisX)#newDisX*offset_x)
                        left_right_X,left_right_Y = makeOffsetPoly(xN, yN, newDisY)#newDisY*offset_y)
                        point_0 = line_intersection(([[top_buttom_X[0], top_buttom_Y[0]],[top_buttom_X[1], top_buttom_Y[1]]]), ([[left_right_X[1], left_right_Y[1]],[left_right_X[2], left_right_Y[2]]]))
                        point_1 = line_intersection(([[top_buttom_X[2], top_buttom_Y[2]],[top_buttom_X[3], top_buttom_Y[3]]]), ([[left_right_X[1], left_right_Y[1]],[left_right_X[2], left_right_Y[2]]]))
                        point_2 = line_intersection(([[top_buttom_X[0], top_buttom_Y[0]],[top_buttom_X[1], top_buttom_Y[1]]]), ([[left_right_X[3], left_right_Y[3]],[left_right_X[0], left_right_Y[0]]]))
                        point_3 = line_intersection(([[top_buttom_X[2], top_buttom_Y[2]],[top_buttom_X[3], top_buttom_Y[3]]]), ([[left_right_X[3], left_right_Y[3]],[left_right_X[0], left_right_Y[0]]]))
                        point_Z=pallet_pos[0][0]+newDisZ
                        plt.plot(point_1[0], point_1[1], 'o')
                        result_center_points.append([point_1[0], point_1[1],point_Z,pallet_pos[0][3],pallet_pos[0][4],pallet_pos[0][5]])
        plt.show()
        

        if(num_layer<count_boxlayer):
            print("Error, that over max layer")
            #return
    



    

