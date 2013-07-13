from django.db import models

# Create your models here.
class Post(models.Model):
    title      = models.CharField('Title', max_length=50)
    image_url  = models.CharField('Image URL', max_length=100)
    keywords   = models.CharField('Keywords', max_length=50)
    category_type   = models.ForeignKey('Category', to_field='category_type', db_column='category_type')
    short_desc = models.CharField('Short Description', max_length=100)
    long_desc  = models.CharField('Long Description', max_length=400)
    author     = models.CharField('Author', max_length=50)
    pub_date   = models.DateTimeField('Date Published')
    post       = models.TextField('Post')
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    
class Category(models.Model):
    category_type   = models.CharField('Category Type', max_length=25, unique=True)
    name       = models.CharField('Name', max_length=50)
    short_desc = models.CharField('Short Description', max_length=100)
    long_desc  = models.CharField('Long Description', max_length=400)
    def __str__(self):
        return self.category_type
    def __unicode(self):
        return self.category_type
    class Meta:
        verbose_name_plural="Categories"