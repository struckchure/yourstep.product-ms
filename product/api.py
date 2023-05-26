from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from product.models import Product
from product.service import ProductService, ReviewService


class ListCreateProductAPI(GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, _):
        return self.get_paginated_response(
            ProductService.list_products(self.paginate_queryset)
        )

    def post(self, request):
        return Response(
            ProductService.create_product(request.data),
            status=status.HTTP_201_CREATED,
        )


class GetUpdateDeleteProductAPI(GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, _, product_id):
        return Response(ProductService.get_product(product_id))

    def patch(self, request, product_id):
        return Response(
            ProductService.update_product(product_id, request.data),
            status=status.HTTP_202_ACCEPTED,
        )

    def delete(self, _, product_id):
        return Response(
            ProductService.delete_product(product_id),
            status=status.HTTP_204_NO_CONTENT,
        )


class CreateReviewAPI(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, _, product_id):
        return self.get_paginated_response(
            ReviewService.list_reviews(product_id, self.paginate_queryset)
        )

    def post(self, request, product_id):
        return Response(
            ReviewService.create_review(product_id, request.data),
            status=status.HTTP_201_CREATED,
        )
