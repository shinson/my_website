from django.db import models
from django.db.models import permalink

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('Category')
    
    def __unicode__(self):
        return '%s' % self.title
    
    
    class Meta:
        ordering = ['-posted']

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title
    
    def calculateCategory(self):
        return Post.objects.filter(category=self).count()
    
    amount = property(calculateCategory)
    



