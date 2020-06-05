from django.db import models

class About(models.Model):
    about_description = models.TextField()


class Education(models.Model):
    degree = models.CharField(max_length = 200)
    duration = models.CharField(max_length=100, verbose_name="Year completed")
    institute = models.CharField(max_length=200)

    def __str__(self):
        return self.degree

class Interests(models.Model):
    name = models.CharField(max_length=150,verbose_name="interest")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length = 150, verbose_name="Project Title")
    description = models.TextField()
    link = models.CharField(max_length = 500, verbose_name="Project repository link", null=True, blank=True)
    web_link = models.CharField(max_length = 500, verbose_name="Project server link", null=True, blank=True)

    def __str__(self):
        return self.title