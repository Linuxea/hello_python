import base64

if __name__ == '__main__':
    with open("demo.jpg", mode="rb")as file:
        img_bytes = file.read()
        print("image_bytes is %s" % img_bytes)
        encode = base64.b64encode(img_bytes)
        print("base 64 encode is %s" % encode)
        decode = base64.b64decode(encode)
        print("base 64 decode is %s" % decode)
