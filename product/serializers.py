from rest_framework import serializers

from product.models import Product, Review


class ProductSerializer(serializers.ModelSerializer):
    review_stats = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_review_stats(self, obj):
        return obj.review_stats


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
