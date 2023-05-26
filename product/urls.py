from django.urls import path

from product.api import CreateReviewAPI, GetUpdateDeleteProductAPI, ListCreateProductAPI

app_name = "product"

urlpatterns = [
    path("product/", ListCreateProductAPI.as_view(), name="list_create_product_api"),
    path(
        "product/<int:product_id>/",
        GetUpdateDeleteProductAPI.as_view(),
        name="get_update_product_api",
    ),
    path(
        "product/<int:product_id>/review/",
        CreateReviewAPI.as_view(),
        name="create_review_api",
    ),
]
