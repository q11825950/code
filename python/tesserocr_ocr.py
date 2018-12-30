#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tesserocr

from PIL import Image

if __name__ == '__main__':
    # 新建Image对象
    image = Image.open("/Users/liwenhao/Desktop/rec/captcha-example1.jpg")
    # 调用tesserocr的image_to_text()方法，传入image对象完成识别
    result = tesserocr.image_to_text(image)
    print(result)
