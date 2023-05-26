from django.core import validators
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def review_stats(self):
        return Review.objects.filter(product=self).aggregate(
            avg_grade=models.functions.Round(models.Avg("grade"), 2),
            no_of_grades=models.Sum("grade"),
        )


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    grade = models.IntegerField(
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(5)]
    )
