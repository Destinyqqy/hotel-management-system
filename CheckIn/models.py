from django.db import models

# Create your models here.
TypeOfRoom=(('1',"高级大床房"),('2',"豪华双人大床房"),('3',"尊贵大床房"))
SEX=(('1',"男"),('0',"女"))


class room(models.Model):
    room_id=models.CharField(max_length=30,primary_key=True,default="000")
    room_type=models.CharField(choices=TypeOfRoom,max_length=30)
    room_floor=models.PositiveIntegerField()
    room_deposit=models.PositiveIntegerField()
    room_is_booked=models.BooleanField()
    def __str__(self):
        return self.room_id
    class Meta:
        verbose_name_plural = '房间'
        verbose_name='房间'


class past_customer(models.Model):
    id=models.CharField(primary_key=True,max_length=30,default="0")
    name=models.CharField(max_length=30)
    sex=models.CharField(choices=SEX,max_length=10)
    birthday = models.DateTimeField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural= '存储客户信息'
        verbose_name= '存储客户信息'



class customer(models.Model):
    id=models.CharField(primary_key=True,max_length=30)
    name = models.CharField(max_length=30)
    sex = models.CharField(choices=SEX,max_length=10)
    birthday = models.DateTimeField()
    is_checked=models.BooleanField()
    agree_record=models.BooleanField()
    room_id=models.ForeignKey(room,on_delete=models.CASCADE)
    face=models.ImageField(blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '当前客户信息'
        verbose_name= '当前客户信息'


class preferred_food(models.Model):
    pf_id=models.ForeignKey(past_customer,on_delete=models.CASCADE)
    # 以下的属性为各种菜系分类 其值为该用户点该菜系频率，菜品推荐算法各个菜系推荐数量由用户点餐频率决定
    def __str__(self):
        return self.pf_id
    class Meta:
        verbose_name_plural = '菜品偏好'
        verbose_name= '菜品偏好'

class dishclass(models.Model):
    classname= models.CharField(max_length=30)
    dishclassno=models.PositiveIntegerField(primary_key=True)
    def __str__(self):
        return self.classname
    class Meta:
        verbose_name_plural = '菜品种类'
        verbose_name= '菜品种类'

class dish(models.Model):
    name = models.CharField(max_length=30)
    dishclassno=models.ForeignKey(dishclass,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '菜品'
        verbose_name= '菜品'