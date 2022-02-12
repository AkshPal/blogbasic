import collections
from tkinter import CASCADE
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django. forms import ModelForm

# Create your models here.


def CASCADE(collector, field, sub_objs, using):
    collector.collect(sub_objs, source=field.remote_field.model,
                      source_attr=field.name, nullable=field.null)
    if field.null and not collections[using].features.can_defer_constraint_checks:
        collector.add_field_update(field, None, sub_objs)

class profile(models.Model):
    user=models.OneToOneField(User, on_delete=CASCADE, blank=True, null=True)
    pic=models.ImageField(upload_to="profile pics", blank=True, null=True)
    bio=models.TextField(blank=True, null=True)
    insta=models.CharField(max_length=100,blank=True,null=True)
    linkedin=models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    

class blogpost(models.Model):
    blogtitle=models.CharField(max_length=50)
    blogwriter=models.ForeignKey(User, on_delete=models.CASCADE)
    blogimage=models.ImageField(upload_to="profile pics",blank=True,null=True)
    blogcontent=models.TextField()
    
    datetime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.blogwriter) +"blogtitle:"+str(self.blogtitle)
    
    def get_absolute_url(self):
        return reverse('blog')
    
class Comments(models.Model):
    commentauthor=models.ForeignKey(User, on_delete=CASCADE)
    commentcontent=models.TextField()
    commentimage=models.ImageField(upload_to="profile pics",blank=True,null=True)
      
    datetime=models.DateTimeField(default=now)
    def __str__(self):
        return str(self.commentauthor)+str(self.commentimage)+str(self.commentcontent)
    

class blogpostForm(forms.ModelForm):
    class Meta:
        model = blogpost
        fields = ('blogtitle', 'blogcontent', 'blogimage')
        widgets = {
            'blogtitle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            
            'blogcontent': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
            
        }   
        
        
        
    
    

        
        

