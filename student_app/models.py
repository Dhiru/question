from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)


class Question(models.Model):
    title = models.CharField(max_length=100)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def host(self):
        return self.user.username


class Answer(models.Model):
    body = models.CharField(max_length=1000)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def host(self):
        return self.user.username

    @property
    def question(self):
        return self.question_id.title


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)


