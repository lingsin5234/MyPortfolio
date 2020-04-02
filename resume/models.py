from django.db import models


# constants
MONTHS = ((1, 'JAN'), (2, 'FEB'), (3, 'MAR'), (4, 'APR'), (5, 'MAY'), (6, 'JUN'),
          (7, 'JUL'), (8, 'AUG'), (9, 'SEP'), (10, 'OCT'), (11, 'NOV'), (12, 'DEC'))


# IT Skills
class TechSkills(models.Model):
    name = models.CharField(max_length=25)
    year_exp = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return self.name


# Education
class Education(models.Model):
    school = models.CharField(max_length=50)
    cert = models.CharField(max_length=30)
    major = models.CharField(max_length=50, null=True)
    start_year = models.IntegerField()
    start_month = models.IntegerField(choices=MONTHS)
    end_year = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(choices=MONTHS, blank=True, null=True)

    def __str__(self):
        return self.school


# Work Experience
class WorkExperience(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=30)
    start_year = models.IntegerField()
    start_month = models.IntegerField(choices=MONTHS)
    end_year = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(choices=MONTHS, blank=True, null=True)

    def __str__(self):
        return self.company + ': ' + self.title


# Work Descriptions
class WorkDescriptions(models.Model):
    job = models.ForeignKey(WorkExperience, on_delete=models.SET_NULL, null=True, default=None)
    description = models.TextField(max_length=250)

    def __str__(self):
        return str(self.job) + ' - ' + self.description[0:99] + ' ...'


# Hobbies
class Hobbies(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


# General Skills
class GeneralSkills(models.Model):
    name = models.CharField(max_length=25)
    order = models.IntegerField()

    def __str__(self):
        return self.name


# Highlights
class Qualifications(models.Model):
    highlight = models.TextField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.highlight


# Projects
class ProjectExperience(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    start_year = models.IntegerField()
    start_month = models.IntegerField(choices=MONTHS)
    end_year = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(choices=MONTHS, blank=True, null=True)

    def __str__(self):
        return str(self.name) + ': ' + str(self.start_year)


# Contact Me
class ContactMe(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
