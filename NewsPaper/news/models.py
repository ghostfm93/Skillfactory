from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render
from django.core.validators import MinValueValidator
from datetime import datetime




class Author(models.Model):
    rating = models.FloatField(default=0.0)
    authorUser = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.authorUser.username

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commRat = self.authorUser.comment_set.all().aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commRat.get('commentRating')

        self.rating = pRat * 3 + cRat
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=64,default='')

    def __str__(self):
        return self.category


class Post(models.Model):
    id = models.AutoField
    news = 'NW'
    article = 'AR'
    types = [(article, 'Статья'),
             (news, 'Новость'),]
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2,choices=types,default=news)
    creation_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category,through='PostCategory')
    head = models.TextField()
    text = models.TextField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.author}, {self.post_type}, {self.head}, {self.rating}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:123]}...'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}, {self.category}'


class Comment(models.Model):
    commentPost = models.ForeignKey(Post,on_delete=models.CASCADE,default=None)
    commentUser = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    text = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.commentUser.username

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()








