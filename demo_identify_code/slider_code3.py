import cv2
import numpy as np


index = 1

bg_img = cv2.imread("./img/cap_background_{}.jpeg".format(index))
font_img = cv2.imread("./img/cap_front_{}.png".format(index))
temp = 'temp.jpg'
targ = 'targ.jpg'

cv2.imwrite(temp, font_img)
cv2.imwrite(targ, bg_img)

bg_img = cv2.imread(targ)
bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
bg_img = abs(255 - bg_img)

cv2.imwrite(targ, bg_img)
bg_img = cv2.imread(targ)
font_img = cv2.imread(temp)
result = cv2.matchTemplate(bg_img, font_img, cv2.TM_CCOEFF_NORMED)
x, y = np.unravel_index(result.argmax(), result.shape)
# 展示圈出来的区域
cv2.rectangle(bg_img, (y, x), (y + 10, x + 10), (7, 249, 151), 2)
cv2.imwrite("show_3.jpg", bg_img)
