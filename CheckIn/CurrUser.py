import os
import sys
# import cv2
from .models import past_customer,customer

class CurrUser(object):
    '''当前客户类'''
    def __init__(self,id=None,sex=None,name=None,agreeprivacy=False,face=None):
        self.id=id
        self.sex=sex
        self.name=name
        self.agreeprivacy=agreeprivacy
        self.face=face
        try:
            pcquery=past_customer.objects.get(id=id)
        except past_customer.DoesNotExist:
            pcquery=None
        try:
            croom=customer.objects.get(room_id=id)
        except customer.DoesNotExist:
            croom=None

        self.isfirst=False if pcquery else True
        self.isbooked=True if croom else False


    #def facesetter(self,facePath):
       # self.face=cv2.imread(facePath)

        