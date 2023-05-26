from django.shortcuts import get_object_or_404

from product.models import Product, Review
from product.serializers import ProductSerializer, ReviewSerializer


class ProductService:
    @staticmethod
    def list_products(paginate_queryset):
        products_query = Product.objects.filter()

        return ProductSerializer(paginate_queryset(products_query), many=True).data

    @staticmethod
    def create_product(create_product_data):
        create_product_serializer = ProductSerializer(data=create_product_data)
        create_product_serializer.is_valid(raise_exception=True)
        create_product_serializer.save()

        return create_product_serializer.data

    @staticmethod
    def get_product(product_id):
        product = get_object_or_404(Product, id=product_id)

        return ProductSerializer(product).data

    @staticmethod
    def update_product(product_id, update_product_data):
        product = get_object_or_404(Product, id=product_id)

        product_update_serializer = ProductSerializer(
            product,
            data=update_product_data,
            partial=True,
        )
        product_update_serializer.is_valid(raise_exception=True)
        product_update_serializer.save()

        return product_update_serializer.data

    @staticmethod
    def delete_product(product_id):
        product = get_object_or_404(Product, id=product_id)
        product.delete()


class ReviewService:
    @staticmethod
    def create_review(product_id, create_review_data):
        create_review_serializer = ReviewSerializer(
            data={
                **create_review_data,
                "product": product_id,
            }
        )
        create_review_serializer.is_valid(raise_exception=True)
        create_review_serializer.save()

        return create_review_serializer.data

    @staticmethod
    def list_reviews(product_id, paginate_queryset):
        review_query = Review.objects.filter(product__id=product_id)

        return ReviewSerializer(paginate_queryset(review_query), many=True).data
