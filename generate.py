from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import json
img = Image.open('image.jpg')

imgplot = plt.imshow(img)
img.thumbnail((24, 24), Image.ANTIALIAS) 


pic = np.ones(img.size[0]*img.size[1]).reshape(img.size[1],img.size[0])
for x in range(img.size[0]):
    for y in range(img.size[1]):
        if(img.getpixel((x,y))[0]+img.getpixel((x,y))[1]+img.getpixel((x,y))[2]>384):            
            pic[y,x] = 0


#lists = pic.tolist() 

res = {"rows": [], "columns": []}
for x in pic:
    print(x)
    list = []
    count = 0
    for y in x:
        if y == 1: count +=1
        else:
            if count != 0: list.append(count)
            count = 0
    if count != 0: list.append(count)        
    res["columns"].append(list)

for x in pic.T:
    list = []
    count = 0
    for y in x:
        if y == 1: count +=1
        else:
            if count != 0: list.append(count)
            count = 0
    if count != 0: list.append(count)
    res["rows"].append(list)


# j = json.dumps(res)
print(res)
imgplot = plt.imshow(img)