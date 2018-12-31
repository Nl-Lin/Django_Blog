from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = verbose_name = "分类"
    def get_absolute_url(self):
        return reverse('Blog:category', kwargs={'pk': self.id})


class Posts(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name ='Get_Posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Blog:detail', kwargs={'pk': self.id})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:

        verbose_name_plural = verbose_name = "文章列表"





