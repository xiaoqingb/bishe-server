from django.db import models

# Create your models here.

class User(models.Model):
    # id = models.AutoField(max_length=200)
    openid = models.CharField(max_length=200, default="")
    code = models.CharField(max_length=200, default="")
    user_name = models.CharField(max_length=200, default="")
    avatar_url = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")
    province = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'  # 指定表名

class lostAndFound(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=200, default="")
    place = models.CharField(max_length=200, default="")
    name= models.CharField(max_length=200, default="")
    lost_type = models.CharField(max_length=200, default="")
    wechat = models.CharField(max_length=200, default="")
    remark_info = models.CharField(max_length=200, default="")
    image_url = models.CharField(max_length=200, default="")
    publish_date = models.CharField(max_length=200, default="2021-01-01", null = True)
    user_id = models.CharField(max_length=200, default="", null = True)
    tell = models.CharField(max_length=200, default="", null = True)
    check_times = models.IntegerField(default=0, null = False)
    publish_status = models.IntegerField(default=0, null = False)
    type = models.CharField(max_length=200, default="0", null = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lost_and_found'  # 指定表名

class UserFavorite(models.Model):
    id = models.AutoField(primary_key=True)
    content_type = models.CharField(max_length=200, default="") #  0失物招领 1校园论坛 2招聘 3活动
    content_id = models.CharField(max_length=200, default="") # 各个模块表的id
    user_id = models.CharField(max_length=200, default="") # 用户id

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'user_favorite'  # 指定表名
