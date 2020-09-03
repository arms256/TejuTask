from django.db import models

# Create your models here.


class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Applicant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    website = models.CharField(max_length=120)
    cover_letter = models.TextField()
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


