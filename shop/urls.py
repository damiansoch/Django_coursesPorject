# shop/urls.py
from django.urls import path
from .views import index, course_detail

app_name = "courses"  # Setting the application namespace

urlpatterns = [
    path("", index, name="list"),  # Accessed via 'courses:list'
    path(
        "course_detail/<int:course_id>/", course_detail, name="detail"
    ),  # Accessed via 'courses:detail'
]
