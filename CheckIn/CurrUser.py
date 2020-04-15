import os
import sys
# import cv2
from CheckIn import models

class CurrUser(object):
    '''当前客户类'''
    def __init__(self,id=None,sex=None,name=None,agreeprivacy=False,face=None):
        self.id=id
        self.sex=sex
        self.name=name
        self.agreeprivacy=agreeprivacy
        self.face=face
        self.isfirst=False if models.past_customer.objects.get(id=id) else True
        self.isbooked=True if models.customer.objects.get(cid=id) else False


    #def facesetter(self,facePath):
       # self.face=cv2.imread(facePath)

        