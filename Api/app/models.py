from django.db import models

# Create your models here.


class Job(models.Model):
    id = models.Integer()
    name = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Applicant(models.Model):
    id = models.Integer()
    name = models.CharField()
    email = models.CharField()
    website = models.CharField()
    cover_letter = models.TextField()
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    id = models.Integer()
    name = models.CharField()
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


