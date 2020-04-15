from django.shortcuts import render
from .models import customer,room
from .CurrUser import CurrUser
# Create your views here.
cu=CurrUser(id='123456789123456789',sex='男',name='xiaoming')

def index(request):
    #cu=CurrUser.get_instance()
    return render(request, 'CheckIn/welcome.html')


def HongRuan(img1,img2):
    return True


def GetCus(Id):
    cus= customer.objects.get(id=Id)
    return cus


def GetRoom(Id):
    r= room.objects.get(room_id=Id)
    return r


def ShowScaning(request):
    return render(request,'CheckIn/scan.html')


def ShowScanInfo(request,img):
    # 处理base64的img
    if HongRuan(cu.face,img):
        person_dict={'id':cu.id,'name':cu.name,'sex':cu.sex}
        return render(request,'CheckIn/personInfo.html',person_dict)
    return render(request, 'CheckIn/welcome.html')


def SplitFlow(request):
    if cu.isfirst:
        return render(request,'CheckIn/privacyPolicy.html')
    if cu.isbooked:
        return render(request,'CheckIn/Map.html')
    else:
        return render(request,'CheckIn/roomType.html')


def AgreePrivacy(request,agree):
    if agree==0:
        return render(request, 'CheckIn/welcome.html')
    if cu.isbooked:
        return render(request,"CheckIn/Map.html")
    else:
        return render(request,"CheckIn/roomType.html")


# 以下为测试代码
def PersonInfo(request):
    return render(request,"CheckIn/personInfo.html")

def SelectRoomType(request,room_type):
    if room_type =='aaa':
        return render(request, 'CheckIn/position.html')

def SelectLocation(request,room_id):
    if room_id =='12345':
        return render(request,'CheckIn/privacyPolicy.html')
    else:
        return render(request, 'CheckIn/scan.html')
