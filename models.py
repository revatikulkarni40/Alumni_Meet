# api/models.py
# api/models.py
from django.db import models

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    graduation_year = models.IntegerField()
    current_job = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
