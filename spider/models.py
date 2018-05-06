import datetime

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    project_name = models.CharField(max_length=100)

    #   添加project，判断是否存在
    def load_project(self, project_list):
        for project in project_list:
            existed_project = Project.objects.filter(project_name=project.project_name).first()
            if not existed_project:
                project.save()

    def find_project_by_id(self, project_id):
        return Project.objects.filter_by(pk=project_id).first()

    def __str__(self):
        return self.project_name

    def to_dict(self):
        return {
            "project_id": self.pk,
            "project_name": self.project_name
        }


class SpiderInstance(models.Model):

    spider_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    @classmethod
    def update_spider_instances(cls, project_id, spider_instance_list):
        pass

    @classmethod
    def list_spider_by_project_id(cls, project_id):
        pass

    def to_dict(self):
        return dict(spider_instance_id=self.id,
                    spider_name=self.spider_name,
                    project_id=self.project_id)


class JobPriority(object):
    LOW, NORMAL, HIGH, HIGHEST = range(-1, 3)


class JobRunType(object):
    ONETIME = 'onetime'
    PERIODIC = 'periodic'


class JobInstance(models.Model):
    spider_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tags = models.TextField()  # job tag(split by , )
    spider_arguments = models.TextField()  # job execute arguments(split by , ex.: arg1=foo,arg2=bar)
    priority = models.IntegerField()
    desc = models.TextField()
    cron_minutes = models.CharField(max_length=100, default='0')
    cron_hour = models.CharField(max_length=100, default='*')
    cron_day_of_month = models.CharField(max_length=100, default='*')
    cron_day_of_week = models.CharField(max_length=100, default='*')
    cron_month = models.CharField(max_length=100, default='*')
    enabled = models.IntegerField(default=0)  # 0/-1
    run_type = models.CharField(max_length=100)  # periodic/onetime


# ok
class SpiderStatus(object):
    PENDING, RUNNING, FINISHED, CANCELED = range(4)


class JobExecution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service_job_execution_id = models.CharField(max_length=100)
    job_instance_id = models.ForeignKey(JobInstance, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    running_status = models.IntegerField(default=SpiderStatus.PENDING)
    running_on = models.TextField()

