import cv2
import numpy as np

# #  cv图片用数组表示方法：
# #  从左到右，从上到下这样开始表示的[ [y0x0, y0x1...y0xx] [y1x0, y1x1...y1xx]... [yyx0, yyx1...yyxx] ]
# #  其中y0x1~yyxx等每一个像素点又是一个数组，即色彩rgb表示法， 比如[255 255 255]表示白色
# test_name = "./img/test_1x2.png"  # 1x2pix的图片，也就是2个点
# test_handle = cv2.imread(test_name)     # imread()函数，把图片转换为一个大的数组
# print(test_handle)  # [ [[58 56 54]] [[58 56 54]] ]表示两个点，[58 56 54]表示一个点
# exit()


index = 1

bg_img = cv2.imread("./img/cap_background_{}.jpeg".format(index))
font_img = cv2.imread("./img/cap_front_{}.png".format(index))
targ = './img/targ.jpg'

bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
bg_img = abs(255 - bg_img)
cv2.imwrite(targ, bg_img)
bg_img = cv2.imread(targ)
result = cv2.matchTemplate(bg_img, font_img, cv2.TM_CCOEFF_NORMED)
y, x = np.unravel_index(result.argmax(), result.shape)
# 展示圈出来的区域
print("识别结果： x:{} y:{}".format(x, y))
cv2.rectangle(bg_img, (x, y), (x + 10, y + 10), (7, 249, 151), 2)
cv2.imwrite("./img/cap_background_result_{}.jpg".format(index), bg_img)
