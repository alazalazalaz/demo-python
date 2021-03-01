import cv2
# cv2 图像处理库
# pip install opencv-python

index = 2
bg_img = cv2.imread("./img/cap_background_{}.jpeg".format(index))
front_img = cv2.imread("./img/cap_front_{}.png".format(index))

bg_edge = cv2.Canny(bg_img, 100, 500)   # 识别图片边缘
front_edge = cv2.Canny(front_img, 100, 500)

bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)  # 转换图片格式
front_pic = cv2.cvtColor(front_edge, cv2.COLOR_GRAY2RGB)

# 缺口匹配
res = cv2.matchTemplate(bg_pic, front_pic, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

x = max_loc[0]
y = max_loc[1]
print(min_val, max_val, min_loc, max_loc)

# 绘制
th, tw = bg_pic.shape[:2]
tl = max_loc    # 左上角坐标
br = (tl[0]+10, tl[1]+10)   # 右下角坐标
cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)   # 绘制矩形(图片句柄，左上角，右下角，颜色，宽度)
cv2.imwrite("./img/cap_background_result_{}.jpg".format(index), bg_img)

