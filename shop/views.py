from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course


# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses,
        },
    )


def course_detail(request, course_id):
    # 1
    try:
        course = Course.objects.get(pk=course_id)
        return render(request, "courses/course_detail.html", {"course": course})
    except Course.DoesNotExist as e:
        print(e)
        return render(
            request, "error_not_found/error_not_found.html", {"error": e}, status=404
        )
    # # 2
    #
    # course = get_object_or_404(Course, pk=course_id)
    # return render(request, "courses/course_detail.html", {"course": course})
