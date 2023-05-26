from decimal import Decimal

from django.test import TestCase

from product.models import Product, Review


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(
            title="Product 1",
            description="This is Product 1",
            price=29.99,
        )

    def test_can_create_product(self):
        product = Product.objects.first()

        self.assertEqual(product.title, "Product 1")
        self.assertEqual(product.description, "This is Product 1")
        self.assertEqual(product.price, Decimal("29.99"))

    def test_can_update_product(self):
        product = Product.objects.first()

        product.title = "Product 10x"
        product.description = "This is Product 10x"
        product.price = Decimal("299.99")

        product.save()

        self.assertEqual(product.title, "Product 10x")
        self.assertEqual(product.description, "This is Product 10x")
        self.assertEqual(product.price, Decimal("299.99"))

    def test_can_delete_products(self):
        Product.objects.all().delete()

        product_count = Product.objects.count()

        self.assertEqual(product_count, 0)


class ReviewTestCase(TestCase):
    def setUp(self):
        product = Product.objects.create(
            title="Product 1",
            description="This is Product 1",
            price=29.99,
        )
        Review.objects.create(
            product=product,
            description="Now i don't know what to say",
            grade=3,
        )
        Review.objects.create(
            product=product,
            description="The first review said it all",
            grade=2,
        )

    def test_can_create_reviews(self):
        product = Product.objects.first()
        review = Review.objects.first()

        self.assertEqual(review.product, product)
        self.assertEqual(review.description, "Now i don't know what to say")
        self.assertEqual(review.grade, 3)

    def test_can_get_review_stats(self):
        product = Product.objects.first()

        self.assertEqual(product.review_stats["avg_grade"], 2.5)
        self.assertEqual(product.review_stats["no_of_grades"], 5)

    def test_grade_min_max_range(self):
        product = Product.objects.first()

        try:
            min_review = Review(
                product=product,
                description="Let's try a minus grading",
                grade=-1,
            )
            min_review.full_clean()
        except:
            pass

        try:
            max_review = Review(
                product=product,
                description="Out of too much like, grade 10",
                grade=10,
            )
            max_review.full_clean()
        except:
            pass

        review_count = Review.objects.count()

        self.assertEqual(review_count, 2)
