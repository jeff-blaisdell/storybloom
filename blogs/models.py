from django.db import models

# Create your models here.
class Category(models.Model):
    name       = models.CharField('Name', max_length=50)
    short_desc = models.CharField('Short Description', max_length=100)
    long_desc  = models.CharField('Long Description', max_length=400)
    def __str__(self):
        return self.name
    def __unicode(self):
        return self.name
    class Meta:
        verbose_name_plural="Categories"
        
class Post(models.Model):
    title         = models.CharField('Title', max_length=50)
    image_url     = models.CharField('Image URL', max_length=100)
    keywords      = models.CharField('Keywords', max_length=50)
    category      = models.ForeignKey(Category)
    short_desc    = models.CharField('Short Description', max_length=100)
    long_desc     = models.CharField('Long Description', max_length=400)
    author        = models.CharField('Author', max_length=50)
    pub_date      = models.DateTimeField('Date Published')
    post          = models.TextField('Post')
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
