import re


def main():
    str = "/cap_union_new_getcapbysig?aid=2017304693&sess=s096" \
          "sHhzwu_5C9p6n6TMzscyui1-r5eAp7cA4sJhxZdFFGvx3PeHawZvUO" \
          "cZOgsdHjX6bgSRRQBrsF6uZaX4D3I3m-2u6ohJ_go5gtbldMtBZFul8YzT" \
          "9aWiRkMu6xfRL4aIjLnvxnu2AvxXxiu_X_o2o2EyBz9N-n7HjyeX2XD4-aocSDm_P7XSvwl_tMvQ0AT" \
          "HBSJ8yTdAbyIKZ05tSpgT0BUleWofa1saEO19QRkmc*&sid=6773256952425562112&img_index=2&subsid=34"
    phone_preg = re.compile("img_index=(\d)&subsid=(\d+)")
    result = phone_preg.findall(str)
    img_index = result[0][0]
    subsid = result[0][1]
    print(result)
    print(img_index, subsid)


if __name__ == "__main__":
    main()

