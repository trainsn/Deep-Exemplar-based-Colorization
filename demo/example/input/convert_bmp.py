#-*- coding:utf-8 -*-
from PIL import Image
import os
import glob

os.chdir(r'D:\\OSU\\style_transfer\\Deep-Exemplar-based-Colorization\\demo\\example\\input')#图片所在的文件夹
for file_names in glob.glob('*.bmp'):#找出所有的后缀为bmp的格式的图片
    print(file_names)
    file_path = r'D:\\OSU\\style_transfer\\Deep-Exemplar-based-Colorization\\demo\\example\\input'+'\\'+file_names#拼接出图片的完整url
    print(file_path)
    
    out_path = os.path.splitext(file_path)[0]+'.jpg'
    Image.open(file_path).save(out_path)
print('转换成功')