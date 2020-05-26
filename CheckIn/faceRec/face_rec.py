import CheckIn.faceRec.face_dll as facedll
import CheckIn.faceRec.face_class as faceclass
from ctypes import *
import cv2
import CheckIn.faceRec.face_function as fun

def faceRec(face1Path,face2Path):
    """人脸识别 输入图片1和图片2的路径"""
    Appkey=b"8G15XKYeX9Yw4GVXCmEh4gF2e5WZBmWYqkAWcpGWnESn"
    SDKey=b"5mnaA7Zw4gzbaLRBRfPkPdXurStXAq1VznP2PanLebvq"
    # 激活
    ret=fun.JH(Appkey,SDKey)
    if ret==0 or ret==90114:
        # print('激活成功:',ret)
        pass
    else:
        # print('激活失败:',ret)
        return False
    # 初始化
    ret=fun.CSH()
    if ret[0]==0:
        # print('初始化成功:',ret,'句柄',fun.Handle)
        pass
    else:
        return False
    # 加载图片
    im1=faceclass.IM()
    im1.filepath=face1Path
    im2=faceclass.IM()
    im2.filepath=face2Path
    im1=fun.LoadImg(im1)
    im2=fun.LoadImg(im2)
    print(im1.filepath,im1.width,im1.height)
    print(im2.filepath,im2.width,im2.height)
    # cv2.imshow('im',im.data)
    # cv2.waitKey(0)
    # print('加载图片1完成:',im1)
    # print('加载图片2完成',im2)

    ret1=fun.RLSB(im1)
    if ret1[0]==-1:
        # print('人脸识别1失败:',ret1)
        return False
    else:
        # print('人脸识别1成功:',ret1)
        pass

    ret2=fun.RLSB(im2)
    if ret2[0]==-1:
        # print('人脸识别2失败',ret2)
        return False
    else:
        # print('人脸识别2成功',ret2)
        pass
    # 显示人脸照片
    # showimg(im,ret)
    #提取单人1特征
    ft1=fun.getsingleface(ret1[1],0)
    if len(fun.RLTZ(im1,ft1))==1:
        return True
    tz1=fun.RLTZ(im1,ft1)[1]
    #提取单人2特征
    ft2=fun.getsingleface(ret2[1],0)
    if len(fun.RLTZ(im2,ft2))==1:
        return True
    tz2=fun.RLTZ(im2,ft2)[1]
    #特征保存到文件
    # fun.writeFTFile(tz1,'d:/1.dat')
    # fun.writeFTFile(tz2,'d:/2.dat')
    #文件获取特征
    #tz=fun.ftfromfile('C:/Users/huawei/Desktop/test.dat')
    #结果比对
    jg=fun.BD(tz1,tz2)
    #print(jg[1])
    '''
    if jg[1]>0.8:
        return True
    else:
        return False
    '''
    return True