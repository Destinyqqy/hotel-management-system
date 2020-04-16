from django.shortcuts import render
from .models import customer,room
from .CurrUser import CurrUser

try:
    # 类的各属性理论上应在__init__函数中赋值，而不是在此处赋值
    cu = CurrUser(id='123456789123456789',sex='男',name='xiaoming')
except ValueError:
    cu = CurrUser(id='000000000000000000', sex='男', name='I_am_error')


def index(request):
    return render(request, 'CheckIn/welcome.html')


def HongRuan(img1,img2):
    return True


def GetCus(Id):
    try:
        cus= customer.objects.get(id=Id)
    except customer.DoesNotExist:
        cus=None
    return cus



def GetRoom(Id):
    try:
        r= room.objects.get(room_id=Id)
    except room.DoesNotExist:
        r= None
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
     try:
         roomquery=room.objects.filter(room_type=room_type)
     except room.DoesNotExist:
         roomquery=None
     floor_list=roomquery.values_list('room_floor',flat=True).distinct()  #找到floor 列表

     room_list=[]
     for floor in floor_list:
         floor_room=[]
         for eachroom in roomquery:
             if eachroom.room_floor==floor:
                 r={'room_id':eachroom.roomid,'room_type':eachroom.room_type,
                 'room_floor':eachroom.room_floor,'room_deposit':eachroom.room_deposit,
                'room_is_booked':eachroom.room_is_booked}
                 floor_room.append(r)
         room_list[floor]=floor_room

     return render(request,'CheckIn/position.html',{'room_dict':room_list})


# 	还应包括：将订房信息和cu静态实例信息写入customer数据库
def SelectLocation(request,room_id):
    # if room_id =='12345':
    #     room_type = 'aaa'
    #     room_floor = 1
    #     room_map = {'room_id': room_id, 'room_type': room_type, 'room_floor': room_floor}
    #     return render(request,'CheckIn/map.html',room_map)
    # else:
    #     return render(request, 'CheckIn/welcome.html')
    try:
        roomselect=room.objects.get(room_id=room_id)
    except room.DoesNotExist:
        roomselect=None
    if roomselect:
        room_map={'room_id':roomselect.room_id,'room_type':roomselect.room_type,
            'room_floor':roomselect.roomfloor}
        return render(request,'CheckIn/map.html',room_map)
    else:
        return render(request,'CheckIn/welcome.html')
