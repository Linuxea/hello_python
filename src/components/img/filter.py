from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('ex.png')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('ex_blur.jpg', 'jpeg')
