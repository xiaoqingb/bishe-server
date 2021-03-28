from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=200, default="")
    code = models.CharField(max_length=200, default="")
    user_name = models.CharField(max_length=200, default="")
    avatar_url = models.CharField(max_length=200, default="001")
    city = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")
    province = models.CharField(max_length=200, default="")
    card_id = models.CharField(max_length=200, default="")
    card_password = models.CharField(max_length=200, default="")
    user_identity = models.CharField(max_length=200, default="0")

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
    type = models.CharField(max_length=200, default="0", null = True)
    status = models.CharField(max_length=200, default="0", null = False) # 0 待审核 1 审核通过 2 审核不通过
    reason = models.CharField(max_length=200, default="", null = True) # 不通过原因

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

class RecruitInfo(models.Model):
    recruit_id = models.AutoField(primary_key=True)
    job_description = models.CharField(max_length=200, default="", null = True)  # 岗位描述
    job_responsibility = models.CharField(max_length=200, default="", null = True)  # 岗位责任
    job_requirement = models.CharField(max_length=200, default="", null = True)  # 岗位要求
    job_type = models.CharField(max_length=200, default="", null = True)  # 岗位类型
    salary = models.CharField(max_length=200, default="", null = True)  # 工资
    publish_date = models.CharField(max_length=200, default="")  # 发布时间
    recurit_end_date = models.CharField(max_length=200, default="")  # 结束时间
    e_mail = models.CharField(max_length=200, default="")  # 投递邮件地址
    skill_tag_list = models.CharField(max_length=200, default="")  # 技能标签
    education_requirement = models.CharField(max_length=200, default="")  # 学历要求
    thumb_up_nums = models.CharField(max_length=200, default=0)  # 点赞人数
    read_nums = models.CharField(max_length=200, default=0)  # 查看人数
    publisher = models.CharField(max_length=200, default="")  # 发布人
    status = models.CharField(max_length=200, default="")  # 发布状态
    company = models.CharField(max_length=200, default="")  # 公司
    image_url = models.CharField(max_length=200, default="", null = True)  # 图片
    address = models.CharField(max_length=200, default="")  # 地点

    def __str__(self):
        return self.recruit_id

    class Meta:
        db_table = 'recurit_info'


class SchoolActivity(models.Model):
    activity_id = models.AutoField(primary_key=True) # 活动id
    activity_title = models.CharField(max_length=200, default="", null = True)  # 标题
    activity_content = models.CharField(max_length=200, default="", null = True)  # 内容
    enter_start_date = models.CharField(max_length=200, default="", null = True)  # 活动报名开始时间
    enter_end_date = models.CharField(max_length=200, default="", null = True)  # 报名结束时间
    activity_start_date = models.CharField(max_length=200, default="", null = True)  # 活动开始时间
    activity_end_date = models.CharField(max_length=200, default="", null = True)  # 活动结束时间
    holder = models.CharField(max_length=200, default="", null = True)  # 组织者
    enter_nums = models.CharField(max_length=200, default=0, null = True)  # 报名人数
    read_nums = models.CharField(max_length=200, default=0, null = True)  # 查看人数
    is_collect = models.CharField(max_length=200, default="", null = True)  # 是否收藏
    publisher = models.CharField(max_length=200, default="", null = True)  # 发布者
    activity_place = models.CharField(max_length=200, default="", null = True)  # 活动结束时间
    image_url = models.CharField(max_length=200, default="", null = True)  # 图片
    status = models.CharField(max_length=200, default="", null = True)  # 活动结束时间
    def __str__(self):
        return self.activity_id

    class Meta:
        db_table = 'school_activity'


class Apply(models.Model):
    id = models.AutoField(primary_key=True) # id
    content_id = models.CharField(max_length=200, default="", null = True)  # 活动id
    user_id = models.CharField(max_length=200, default="", null = True)  # 报名者id
    def __str__(self):
        return self.id

    class Meta:
        db_table = 'apply'


class ThumbUp(models.Model):
    id = models.AutoField(primary_key=True) # id
    content_id = models.CharField(max_length=200, default="", null = True)  # 职位id
    user_id = models.CharField(max_length=200, default="", null = True)  # 报名者id
    content_type = models.CharField(max_length=200, default=0, null = True)  # 内容类型 0 招聘 1 论坛
    def __str__(self):
        return self.id

    class Meta:
        db_table = 'thumb_up'

class SchoolForum(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_tag_list = models.CharField(max_length=200, default="", null = True)
    publisher = models.CharField(max_length=200, default="", null = True)
    topic_content = models.CharField(max_length=200, default="", null = True)
    publish_date = models.CharField(max_length=200, default="", null = True)
    read_nums = models.CharField(max_length=200, default=0, null = True)
    # thumb_up_nums = models.CharField(max_length=200, default="", null = True)
    def __str__(self):
        return self.topic_id

    class Meta:
        db_table = 'school_forum'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200, default="", null = True)
    topic_id = models.CharField(max_length=200, default="", null = True)
    content = models.CharField(max_length=200, default="", null = True)
    publish_date = models.CharField(max_length=200, default="", null = True)
    def __str__(self):
        return self.id

    class Meta:
        db_table = 'comment'

