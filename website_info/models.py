from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Media(models.Model):
    publications = 'Publications'
    mentions = 'Mentions'
    presentations = 'Presentations'

    category_choices = (
    (publications, 'Authored'),
    (mentions, 'Featured In'),
    (presentations, 'Presented'),
    )

    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, unique=True)
    category = models.CharField(max_length=50,choices=category_choices, default=mentions)
    url = models.CharField(max_length=500, unique=True)
    date = models.DateField(db_index=True, auto_now_add=False)
    
    def __unicode__(self):
        return self.title
    
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Media"

class Project(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='project_photos')
    project_url = models.CharField(max_length=500, blank=True)
    code_url = models.CharField(max_length=500, blank=True)
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.name 
    
    class Meta:
        ordering = ['-date']

class Skill(models.Model):
    language = 'Language'
    framework = 'Framework'
    database = 'Database'
    design = 'Design'

    category_choices = (
    (language, 'Languages'),
    (framework, 'Frameworks'),
    (database, 'Databases'),
    (design, 'Design')
    )

    uid = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50,choices=category_choices, default= language)
    level = models.IntegerField( default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __unicode__(self):
        return self.skill 

class Work(models.Model):
    uid = models.AutoField(primary_key=True)
    company = models.CharField(max_length=50, unique=False)
    date_range = models.CharField(max_length=50, unique=False)
    description = models.TextField()
    start_date = models.DateField(db_index=True, auto_now_add=False)

    def __unicode__(self):
        return self.company 
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Work"

