from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import random


def do(driver, track):
    button = driver.find_element_by_id("s_button")
    ActionChains(driver).click_and_hold(button).perform()
    time.sleep(1)
    for i in track:
        ActionChains(driver).move_by_offset(i, 0).perform()
    ActionChains(driver).release().perform()


def get_track(distance, t):  # distance为传入的总距离，a为加速度
    track = []
    current = 0
    mid = distance * t / (t + 1)
    v = 0
    while current < distance:
        if current < mid:
            a = 3
        else:
            a = -1
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


def get_track2(distance):
    track = []
    current = 0
    mid = distance*3/4
    t = random.randint(2, 3)/10
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0+a*t
        move = v0*t+1/2*a*t*t
        current += move
        track.append(round(move))
    return track


def main():
    url = "http://local.test.com/slider/index.html"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    moveLen = 220
    # track = get_track(moveLen, 1)
    track = get_track2(moveLen)
    do(driver, track)
    print(len(track))
    print(track)


if __name__ == "__main__":
    main()

