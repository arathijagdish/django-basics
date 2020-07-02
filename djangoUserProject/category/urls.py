from django.urls import path
from . import views as v

urlpatterns = [
    path('view/', v.view, name="view_category"),
    path('viewsubcategories/<int:id>', v.view_subcategories, name="view_subcategories"),
    path('create/', v.create, name="create_category"),
    path('create/subcategory/', v.create_subcategory, name="create_subcategory"),
]