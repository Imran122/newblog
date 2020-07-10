from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import ckeditor
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d')
    
    def __str__(self):
        return self.user.username

class Categorey(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title





class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    content = RichTextUploadingField()
    
    timestamp = models.DateTimeField(auto_now_add=True)
    #content = tinymce_models.HTMLField()
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    categories = models.ManyToManyField(Categorey)
    featured = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={
            'id': self.id
        })
 
