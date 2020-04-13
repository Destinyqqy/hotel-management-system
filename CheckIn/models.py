from django.db import models

# Create your models here.
TypeOfRoom=((1,"高级大床房"),(2,"豪华双人大床房"),(3,"尊贵大床房"))
SEX=((1,"男"),(2,"女"))


class room(models.Model):
    room_id=models.CharField(max_length=30,primary_key=True)
    room_type=models.CharField(choices=TypeOfRoom,max_length=30)
    room_floor=models.PositiveIntegerField()
    room_deposit=models.PositiveIntegerField()
    room_is_booked=models.BooleanField()


class past_customer(models.Model):
    id=models.CharField(primary_key=True,max_length=30,default="0")
    name=models.CharField(max_length=30)
    sex=models.CharField(choices=SEX,max_length=10)
    birthday = models.DateTimeField()


class customer(models.Model):
    id=models.CharField(primary_key=True,max_length=30)
    name = models.CharField(max_length=30)
    sex = models.CharField(choices=SEX,max_length=10)
    birthday = models.DateTimeField()
    is_checked=models.BooleanField()
    agree_record=models.BooleanField()
    room_id=models.ForeignKey(room,on_delete=models.CASCADE)
    face=models.ImageField()


class preferred_food(models.Model):
    pf_id=models.ForeignKey(past_customer,on_delete=models.CASCADE)
    # 以下的属性为各种菜系分类 其值为该用户点该菜系频率，菜品推荐算法各个菜系推荐数量由用户点餐频率决定


class dishclass(models.Model):
    classname= models.CharField(max_length=30)
    dishclassno=models.PositiveIntegerField(primary_key=True)


class dish(models.Model):
    name = models.CharField(max_length=30)
    dishclassno=models.ForeignKey(dishclass,on_delete=models.CASCADE)