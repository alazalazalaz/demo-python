import cv2
import numpy as np

# #  cv图片用数组表示方法：
# #  从左到右，从上到下这样开始表示的[ [y0x0, y0x1...y0xx] [y1x0, y1x1...y1xx]... [yyx0, yyx1...yyxx] ]
# #  其中y0x1~yyxx等每一个像素点又是一个数组，即色彩rgb表示法， 比如[255 255 255]表示白色
# test_name = "./img/test_1x2.png"  # 1x2pix的图片，也就是2个点
# test_handle = cv2.imread(test_name)     # imread()函数，把图片转换为一个大的数组
# print(test_handle)  # [ [[58 56 54]] [[58 56 54]] ]表示两个点，[58 56 54]表示一个点
# exit()


def main():
    index = 1
    target = cv2.imread("./img/cap_background_{}.jpeg".format(index))
    template = cv2.imread("./img/cap_front_{}.png".format(index))

    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)   # 把图片转换为灰度图
    template = abs(255 - template)  # 分别被255减

    result = cv2.matchTemplate(template, target, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    print(y, x)
    # 展示圈出来的区域
    w, h = 10, 10
    cv2.rectangle(target, (y, x), (y + w, x + h), (7, 249, 151), 2)
    cv2.imwrite('Show_2.jpg', template)

if __name__ == '__main__':
    main()