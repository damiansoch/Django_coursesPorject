from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    # this is to show title in the admin panel
    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # this is to show title in the admin panel
    def __str__(self):
        return self.title


# # # All below can be done from the shell running -> # -> python manage.py shell

# # new category from  (shell)
# >>> from shop.models import Category
# >>> new_category = Category(title="Programming")
# >>> new_category.save()

# and to get  categories from the db use
# >>> Category.objects.all()
# >>> Category.objects.get(pk=1)
# >>> Category.objects.get(title="Programming")
# or filter greater than
# >>> Category.objects.filter(id__gt=0)

# >>> Category.objects.filter(title__contains="ing")

# # getting all the courses in the category
# >>> category = Category.objects.get(pk=1)
# >>> category.course_set.all()
# response -> <QuerySet [<Course: Course object (1)>]>

# # we can create new course adding it to a category.course_set
# >>> category = Category.objects.get(pk=1)
# >>> print(category)
# Category object (1)
# >>> category.course_set.all()
# <QuerySet [<Course: Course object (1)>]>
# >>> category.course_set.create(title="C# beginner to advanced", price = 199, students_qty = 10, reviews_qty = 0)
# <Course: Course object (2)>
