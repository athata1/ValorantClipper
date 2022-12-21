from PIL import Image
im = Image.open("frame4410.jpg")
im = im.resize((1920,1080))
im = im.crop((860,770,1060,960))
im.show()
