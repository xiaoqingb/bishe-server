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
    id = models.AutoField(primary_key=True, max_length=200, default="")
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
    type = models.CharField(max_length=200, default="0", null = True)

    def __str__(self):
        return self.lost_name

    class Meta:
        db_table = 'lost_and_found'  # 指定表名
