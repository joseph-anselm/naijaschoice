from django.db import models
from django.utils import timezone
import datetime
from django.utils import timezone


class Question(models.Model):
    question_title = models.CharField(max_length=50, blank=False)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug_field = models.CharField(max_length=100, blank=False)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.question_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice Model.......


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class VoterIp(models.Model):
    post = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='ips', null=True)
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Comments(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
