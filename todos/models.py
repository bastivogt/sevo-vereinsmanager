from typing import Iterable
from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth import get_user_model
User = get_user_model()


from . import exceptions
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
    done_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="doneuser")



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
        if check_todo.done_by == user or check_todo.done == False:
            if not check_todo.done:
                self.done_by = user
                return super().save(*args, **kwargs)
            else:
                self.done_by = None
                return super().save(*args, **kwargs)
        else:
            self.done = check_todo.done
            ret = super().save(*args, **kwargs)
            #raise Exception("Logged in user is not the same user who done_by the todo")
            raise exceptions.InvalidUserExcpetion()
            return ret



    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]