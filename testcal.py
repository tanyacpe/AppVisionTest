import numpy as np
import matplotlib.pyplot as plt

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

pallet_pos = [[512.7, -760.41, 100.0, 0.0, 0.0, 90.0], [-678.68, -616.83, 100.0, 0.0, 0.0, 90.0], [-559.03, 375.98, 100.0, 0.0, 0.0, 90.0], [632.35, 232.41, 100.0, 0.0, 0.0, 90.0]]
xN = [pallet_pos[0][0],pallet_pos[1][0],pallet_pos[2][0],pallet_pos[3][0]]
yN = [pallet_pos[0][1],pallet_pos[1][1],pallet_pos[2][1],pallet_pos[3][1]]

#x=270
#y=180

offset_top_buttom = 270/2
offset_left_right = 180/2

top_buttom_X = []
top_buttom_Y = []
left_right_X = []
left_right_Y = []
top_buttom_X,top_buttom_Y = makeOffsetPoly(xN, yN, offset_top_buttom)
left_right_X,left_right_Y = makeOffsetPoly(xN, yN, offset_left_right)

xN.append(xN[0])
yN.append(yN[0])
plt.plot(xN, yN)
# plt.plot(top_buttom_X, top_buttom_Y)
# plt.plot(left_right_X, left_right_Y)

point_0 = line_intersection(([[top_buttom_X[0], top_buttom_Y[0]],[top_buttom_X[1], top_buttom_Y[1]]]), ([[left_right_X[1], left_right_Y[1]],[left_right_X[2], left_right_Y[2]]]))
point_1 = line_intersection(([[top_buttom_X[2], top_buttom_Y[2]],[top_buttom_X[3], top_buttom_Y[3]]]), ([[left_right_X[1], left_right_Y[1]],[left_right_X[2], left_right_Y[2]]]))
point_2 = line_intersection(([[top_buttom_X[0], top_buttom_Y[0]],[top_buttom_X[1], top_buttom_Y[1]]]), ([[left_right_X[3], left_right_Y[3]],[left_right_X[0], left_right_Y[0]]]))
point_3 = line_intersection(([[top_buttom_X[2], top_buttom_Y[2]],[top_buttom_X[3], top_buttom_Y[3]]]), ([[left_right_X[3], left_right_Y[3]],[left_right_X[0], left_right_Y[0]]]))
plt.plot(point_0[0], point_0[1], 'o')
plt.plot(point_1[0], point_1[1], 'o')
plt.plot(point_2[0], point_2[1], 'o')
plt.plot(point_3[0], point_3[1], 'o')
plt.plot([point_0[0],point_1[0],point_3[0],point_2[0],point_0[0]], [point_0[1],point_1[1],point_3[1],point_2[1],point_0[1]])

# คำนวณจุดกึ่งกลางของรูปสี่เหลี่ยม
center_x = (point_0[0] + point_1[0] + point_2[0] + point_3[0]) / 4
center_y = (point_0[1] + point_1[1] + point_2[1] + point_3[1]) / 4
#plt.plot(center_x, center_y, 'o')
plt.show()
