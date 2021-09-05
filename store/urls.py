from django.urls import path

from . import views


urlpatterns = [
    path("", views.all_products, name="all-products"),
    path("book/<slug:slug>/", views.product_detail, name="product_detail"),
    path("search/<slug:category_slug>/", views.category_list, name="category_list"),
]
