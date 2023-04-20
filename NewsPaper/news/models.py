from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # реализация метода update_rating
        # суммарный рейтинг каждой статьи автора умножается на 3;
        post_rating = sum([post.rating for post in self.post_set.all()]) * 3
        # суммарный рейтинг всех комментариев автора;
        comment_rating = sum([comment.rating for comment in self.comments.all()])
        # суммарный рейтинг всех комментариев к статьям автора.
        post_comment_rating = sum([comment.rating for post in self.post_set.all() for comment in post.comments.all()])
        self.rating = post_rating + comment_rating + post_comment_rating
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    POST_TYPES = (
        ('article', 'Article'),
        ('news', 'News'),
    )
    post_type = models.CharField(max_length=7, choices=POST_TYPES)
    created_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        preview_length = 124
        if len(self.content) <= preview_length:
            return self.content
        return self.content[:preview_length] + '...'

    def update_rating(self):
        # суммарный рейтинг всех комментариев к посту
        comment_rating = sum([comment.rating for comment in self.comments.all()])
        self.rating = comment_rating
        self.save()

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} - {self.category.name}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.content

# Create your models here.
