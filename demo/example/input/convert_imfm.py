#-*- coding:utf-8 -*-
from PIL import Image
import os
import glob

os.chdir('.')#图片所在的文件夹
for file_names in glob.glob('*.png'):#找出所有的后缀为bmp的格式的图片
    print(file_names)
    file_path = file_names#拼接出图片的完整url
    print(file_path)
    
    out_path = os.path.splitext(file_path)[0]+'.jpg'
    im = Image.open(file_path)
    #im = im.convert('RGB')
    background = Image.new('RGBA', im.size, (255,255,255))
    alpha_composite = Image.alpha_composite(background, im)
    alpha_composite = alpha_composite.convert('RGB')
    alpha_composite.save(out_path, 'JPEG',quality=80)
print('转换成功')
