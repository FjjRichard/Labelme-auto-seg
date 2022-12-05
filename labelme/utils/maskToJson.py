import base64
import cv2
import os
import numpy as np 
import json

# 图片转换成base64
def image_to_base64(path):
    with open(path, 'rb') as img:
        b64encode = base64.b64encode(img.read())
        s = b64encode.decode()
        b64_encode = 'data:image/jpeg;base64,%s' % s
        return b64_encode


def get_points(contour,isRemoveSamlleTarget=True):
    num = len(contour[:, 0, 0])  # 个数
    if isRemoveSamlleTarget:
        if num < 10: #可以适当去除小目标
            return contour[:, 0], 0
    if num > 200:
        hundred = num // 30  # 步长
        tem = contour[:, 0][::hundred]
        return tem, 1
    else:
        return contour[:, 0], 1


def generate_json(name, h, w, shapes,imageData):
    dict = {}
    dict["version"] = "5.1.0"
    dict["flags"] = {}
    dict["shapes"] = shapes
    dict["imagePath"] = name
    dict["imageData"] = imageData
    dict["imageHeight"] = h
    dict["imageWidth"] = w
    return json.dumps(dict, ensure_ascii=False,indent=4)

def generateJosn(img_path,mask,label_name):
    img_base = os.path.basename(img_path)
    shapeslist = list()
    
    h, w = mask.shape
    for label in label_name.keys():
        temp  = mask.copy()

        temp[temp == label+1] = 255
        temp[temp!= 255] = 0
        ret, binary = cv2.threshold(temp, 0, 255, cv2.THRESH_BINARY )  

        binary = np.uint8(binary)

        contours, heriachy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            shapesdict = {"label":'', "points":'', "group_id":"null", "shape_type":"polygon", "flags":{}}
            points, flag = get_points(contour)
            points = points.tolist()
            if flag ==1:
                shapesdict['label'] = label_name[label]
                shapesdict['points'] = points
                shapeslist.append(shapesdict)

    imageData = image_to_base64(img_path).split(',')[1]
    json_content = generate_json(img_base,h,w,shapeslist,imageData)
    return json_content
