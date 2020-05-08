import os
import sys
# import cv2
from .models import past_customer,customer

class CurrUser(object):
    '''当前客户类'''
    def __init__(self,id=None,sex=None,name=None,agreeprivacy=False,face=None):
        # 此处应调用身份证接口，此处先赋值
        self.face=face
        self.id='123456789123456789'
        self.sex='男'
        self.name='小明'
        self.agreeprivacy=agreeprivacy
        self.face= None

        try:
            pcquery=past_customer.objects.filter(id=id)
        except past_customer.DoesNotExist:
            pcquery=None
        try:
            croom=customer.objects.filter(room_id=id)
        except customer.DoesNotExist:
            croom=None

        self.isfirst=False if pcquery else True
        self.isbooked=True if croom else False

        # 将身份证照片暂时存储在磁盘，人脸比对后删除

    #def facesetter(self,facePath):
       # self.face=cv2.imread(facePath)

        