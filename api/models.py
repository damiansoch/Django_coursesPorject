from tastypie.resources import ModelResource
from shop.models import Category
from shop.models import Course
from .authentication import CustomApiKeyAuthentication
from tastypie.authorization import Authorization


# Create your resources here.
class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = "categories"
        allowed_methods = ["get"]


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = "courses"
        allowed_methods = ["get", "delete", "post", "put"]
        authentication = CustomApiKeyAuthentication()
        authorization = Authorization()

    # next two methods are required to properly connect course to category.
    # we need to do it to be able to
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data["category_id"]
        return bundle

    def dehydrate(self, bundle):
        bundle.data["category_id"] = bundle.obj.category_id
        #  we can also add more fields
        bundle.data["category"] = bundle.obj.category
        return bundle

    # we can also change the single response data like title or price in this case
    def dehydrate_title(self, bundle):
        return bundle.data["title"].upper()

    def dehydrate_price(self, bundle):
        return round(bundle.data["price"], 1)
