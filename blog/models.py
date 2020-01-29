# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
class Post(models.Model):
    objects = models.Manager()      #Our default Manager
    STATUS_CHOICES = (
        ('Happy','Happy'),
        ('Sad','Sad'),
        ('Alone','Alone'),
        ('Loved','Loved'),
        ('Broken','Broken'),
        ('Excited','Excited'),
        ('Motivated','Motivated'),
        ('Crazy','Crazy'),
        ('Cried','Cried'),
    )
    title               =       models.CharField(max_length=100)
    slug                =       models.SlugField(max_length=120)
    author              =       models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE)
    body                =       models.TextField()
    likes               =       models.ManyToManyField(User, related_name='likes', blank=True)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)
    status              =       models.CharField(max_length=10, choices=STATUS_CHOICES, default='Happy')
    restrict_comment    =       models.BooleanField(default=False)
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.title
    def total_likes(self):
        return self.likes.count()
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id, self.slug])
    def __unicode__(self):
        return self.title
    def get_images(self):
        return self.images_set.all()

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    mob=models.CharField(max_length=14, null=True, blank=True)
    city=models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='images/',verbose_name='images',null=True, blank=True)
    def __str__(self):
        return "Profile of user {}".format(self.user.username)
    def get_absolute_url(self):
        return reverse("blog:prof", args=[self.id,])
class Images(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',verbose_name='images',)
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return str(self.image)
    def __unicode__(self):
        return str(self.image)
    def title(self):
        return self.post.title
    def get_images(self):
        return self.images_set.all()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name="replies",on_delete=models.CASCADE)
    content = models.CharField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{},Post-{},Profile-{}'.format(self.content,self.post.title, str(self.user.username))

class Report(models.Model):
    STATUS_CHOICES = (
        ('Nudity','Nudity'),
        ('Violence','Violence'),
        ('Haressment','Haressment'),
        ('Suicide or Self-Injury','Suicide or Self-Injury'),
        ('False News','False News'),
        ('Span','Span'),
        ('Unauthorized Sales','Unauthorized Sales'),
        ('Hate Speech','Hate Speech'),
        ('Terrorism','Terrorism'),
    )
    req = models.CharField(max_length=20, null=True, blank=True)
    user = models.CharField(max_length=20, null=True, blank=True)
    post = models.CharField(max_length=20, null=True, blank=True)
    cmnt = models.CharField(max_length=20, null=True, blank=True)
    reason=models.CharField(max_length=30, choices=STATUS_CHOICES, )
    body=models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return 'Request-{},Profile-{},Post-{},Comment-{},Reason-{},Body-{}'.format(self.req,self.user,self.post,self.cmnt,self.reason,self.body)