from django.db import models

# Create your models here.
TypeOfRoom=(('高级大床房',"高级大床房"),('豪华双人大床房',"豪华双人大床房"),('尊贵大床房',"尊贵大床房"))
SEX=(('男',"男"),('女',"女"))


class room(models.Model):
    '''房间类'''
    def __str__(self):
        return self.room_id

    room_id=models.CharField(max_length=30,primary_key=True,db_column='rid',verbose_name='房间号')
    room_type=models.CharField(choices=TypeOfRoom,max_length=30,db_column='rtype',verbose_name='房间类型')
    room_floor=models.PositiveIntegerField(db_column='rfloor',verbose_name='楼层')
    room_deposit=models.PositiveIntegerField(db_column='rdeposit',verbose_name='订金')
    room_is_booked=models.BooleanField(db_column='rbooked',verbose_name='预定状态',default=False)

    class Meta:
        verbose_name='房间'
        verbose_name_plural='房间'


class past_customer(models.Model):
    '''过去客户类'''
    def __str__(self):
        return self.name

    id=models.CharField(primary_key=True,max_length=30,db_column='pcid',verbose_name='身份证号')
    name=models.CharField(max_length=30,db_column='pcname',verbose_name='姓名')
    sex=models.CharField(choices=SEX,max_length=10,db_column='pcsex',verbose_name='性别')
    birthday = models.DateField(db_column='pcbir',verbose_name='生日')

    class Meta:
        verbose_name='存储客户信息'
        verbose_name_plural='存储客户信息'


class customer(models.Model):
    '''当前客户类'''
    def __str__(self):
        return self.name

    id=models.CharField(primary_key=True,max_length=30,db_column='cid',verbose_name='身份证号')
    name = models.CharField(max_length=30,db_column='cname',verbose_name='姓名')
    sex = models.CharField(choices=SEX,max_length=10,db_column='csex',verbose_name='性别')
    birthday = models.DateField(db_column='cbir',verbose_name='生日')
    is_checked=models.BooleanField(default=False,db_column='ccheck',verbose_name='入住状态')
    agree_record=models.BooleanField(db_column='crecord',verbose_name='是否同意记录偏好信息')
    room_id=models.ForeignKey(room,on_delete=models.CASCADE,verbose_name='房间号')
    face=models.ImageField(blank=True,db_column='cface',verbose_name='照片')

    class Meta:
        verbose_name='当前客户信息'
        verbose_name_plural='当前客户信息'

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '当前客户信息'
        verbose_name= '当前客户信息'


class preferred_food(models.Model):
    '''菜品偏好'''
    def __str__(self):
        return self.pf_id

    pf_id=models.ForeignKey(past_customer,on_delete=models.CASCADE,verbose_name='身份证号')
    # 以下的属性为各种菜系分类 其值为该用户点该菜系频率，菜品推荐算法各个菜系推荐数量由用户点餐频率决定

    class Meta:
        verbose_name='菜品偏好'
        verbose_name_plural='菜品偏好'


class dishclass(models.Model):
    '''菜品种类'''
    def __str__(self):
        return self.classname

    classname= models.CharField(max_length=30,db_column='dcname',verbose_name='种类名')
    dishclassno=models.PositiveIntegerField(primary_key=True,db_column='dcno',verbose_name='种类编号')

    class Meta:
        verbose_name='菜品种类'
        verbose_name_plural='菜品种类'

class dish(models.Model):
    '''菜品'''
    def __str__(self):
        return self.name

    dishno=models.PositiveIntegerField(primary_key=True,db_column='dno',verbose_name='菜品编号')
    name = models.CharField(max_length=30,db_column='dname',verbose_name='菜名')
    dishclassno=models.ForeignKey(dishclass,on_delete=models.CASCADE,verbose_name='种类编号')

    class Meta:
        verbose_name='菜品'
        verbose_name_plural='菜品'
