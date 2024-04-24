from django.urls import path
from goods import views

app_name = "goods"

urlpatterns = [
	path("", views.catalog, name="category"),
    path("product/", views.product, name="product"),
]
