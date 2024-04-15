from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# # new category from  (shell)
# -> first run python manage.py shell
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
