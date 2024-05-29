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


    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def get_categories_str(self):
        categories = self.categories.all()
        categories_list = [category.title for category in categories]
        return ", ".join(categories_list)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]