import CheckIn.faceRec.face_dll as facedll
import CheckIn.faceRec.face_class as faceclass
from ctypes import *
import cv2
from io import BytesIO
# from Main import *
Handle=c_void_p()
c_ubyte_p = POINTER(c_ubyte) 
# 激活函数
def JH(appkey,sdkey):
    ret=facedll.jihuo(appkey,sdkey)
    return ret
# 初始化函数
def CSH():# 1：视频或图片模式,2角度,3最小人脸尺寸推荐16,4最多人脸数最大50,5功能,6返回激活句柄
    ret=facedll.chushihua(0xFFFFFFFF,0x1,16,50,5,byref(Handle))
    # Main.Handle=Handle
    return ret,Handle
# cv2记载图片并处理
def LoadImg(im):
    img=cv2.imread(im.filepath)
    sp=img.shape
    img=cv2.resize(img,(sp[1]//4*4,sp[0]//4*4))
    sp=img.shape
    im.data=img
    im.width=sp[1]
    im.height=sp[0]
    return im
def RLSB(im):
    faces=faceclass.ASF_MultiFaceInfo()
    img=im.data
    imgby=bytes(im.data)
    imgcuby=cast(imgby,c_ubyte_p)
    ret=facedll.shibie(Handle,im.width,im.height,0x201,imgcuby,byref(faces))
    return ret,faces
# 显示人脸识别图片
def showimg(im,faces):
    for i in range(0,faces.faceNum):
        ra=faces.faceRect[i]
        cv2.rectangle(im.data,(ra.left1,ra.top1),(ra.right1,ra.bottom1),(255,0,0,),2)
    cv2.imshow('faces',im.data)
    cv2.waitKey(0)
#提取人脸特征
def RLTZ(im,ft):
    detectedFaces=faceclass.ASF_FaceFeature()
    img=im.data
    imgby=bytes(im.data)
    imgcuby=cast(imgby,c_ubyte_p)
    ret=facedll.tezheng(Handle,im.width,im.height,0x201,imgcuby,ft,byref(detectedFaces))
    if ret==0:
        retz=faceclass.ASF_FaceFeature()
        retz.featureSize=detectedFaces.featureSize
        #必须操作内存来保留特征值,因为c++会在过程结束后自动释放内存
        retz.feature=facedll.malloc(detectedFaces.featureSize)
        facedll.memcpy(retz.feature,detectedFaces.feature,detectedFaces.featureSize)
        # print('提取特征成功:',detectedFaces.featureSize,mem)
        return ret,retz
    else:
        return ret
#特征值比对,返回比对结果
def BD(tz1,tz2):
    jg=c_float()
    ret=facedll.bidui(Handle,tz1,tz2,byref(jg))
    return ret,jg.value
#单人特征写入文件
def writeFTFile(feature,filepath):
    f = BytesIO(string_at(feature.feature,feature.featureSize))
    a=open(filepath,'wb')
    a.write(f.getvalue())
    a.close()
#从多人中提取单人数据
def getsingleface(singleface,index):
    ft=faceclass.ASF_SingleFaceInfo()
    ra=singleface.faceRect[index]
    ft.faceRect.left1=ra.left1
    ft.faceRect.right1=ra.right1
    ft.faceRect.top1=ra.top1
    ft.faceRect.bottom1=ra.bottom1
    ft.faceOrient=singleface.faceOrient[index]
    return ft
#从文件获取特征值
def ftfromfile(filepath):
    fas=faceclass.ASF_FaceFeature()
    f=open(filepath,'rb')
    b=f.read()
    f.close()
    fas.featureSize=b.__len__()
    fas.feature=facedll.malloc(fas.featureSize)
    facedll.memcpy(fas.feature,b,fas.featureSize)
    return fas