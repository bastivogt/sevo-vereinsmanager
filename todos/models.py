from typing import Iterable
from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


# Catergory
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = "Categories"


# Todo
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = tinymce_models.HTMLField()
    categories = models.ManyToManyField(Category, blank=True)
    done = models.BooleanField(default=False)
    user_doned = models.CharField(max_length=255, null=True, blank=True)



    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def get_categories_str(self):
        categories = self.categories.all()
        categories_list = [category.title for category in categories]
        return ", ".join(categories_list)

    # def save(self, user=None, *args, **kwargs):
    #     print("save_doned()")
    #     print(user)
    #     if user == None:
    #         return super().save(*args, **kwargs)
        
    #     check_todo = Todo.objects.get(id=self.id)
    #     if not check_todo.done:
    #         self.user_doned = user.id
    #         super().save(*args, **kwargs)
    #     else:
    #         self.user_doned = None
    #         super().save(*args, **kwargs)

    def save(self, user=None, *args, **kwargs):
        print("save_doned()")
        print(user)
        if user == None:
            return super().save(*args, **kwargs)
        try:
            check_todo = Todo.objects.get(id=self.id)
        except:
            return super().save(*args, **kwargs)
        if not check_todo.done:
            self.user_doned = user.username
            return super().save(*args, **kwargs)
        else:
            self.user_doned = None
            return super().save(*args, **kwargs)



    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]