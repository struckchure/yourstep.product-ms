from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

product_data = {
    "title": "Comb",
    "description": "I don't know how to explain this to you",
    "price": "9.99",
}
review_data = {"description": "Just get the comb", "grade": 4}


class ProductAPITestCase(APITestCase):
    def test_can_list_products(self):
        self.client.force_authenticate(user=User.objects.create(username="JohnDoe"))

        for _ in range(20):
            self.client.post(
                path=reverse("product:list_create_product_api"),
                data=product_data,
                format="json",
            )

        response = self.client.get(
            path=reverse("product:list_create_product_api"),
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["count"], 20)
        self.assertEqual(len(response.data["results"]), 10)

    def test_will_raise_401(self):
        response = self.client.post(
            path=reverse("product:list_create_product_api"),
            data=product_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_create_products(self):
        self.client.force_authenticate(user=User.objects.create(username="JohnDoe"))
        response = self.client.post(
            path=reverse("product:list_create_product_api"),
            data=product_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["title"], product_data["title"])
        self.assertEqual(response.data["description"], product_data["description"])
        self.assertEqual(response.data["price"], product_data["price"])

    def test_can_get_product(self):
        self.client.force_authenticate(user=User.objects.create(username="JohnDoe"))
        response = self.client.post(
            path=reverse("product:list_create_product_api"),
            data=product_data,
            format="json",
        )

        product_id = response.data["id"]

        response = self.client.get(
            path=reverse("product:get_update_product_api", args=[product_id]),
            data=product_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["title"], product_data["title"])
        self.assertEqual(response.data["description"], product_data["description"])
        self.assertEqual(response.data["price"], product_data["price"])

    def test_can_update_product(self):
        self.client.force_authenticate(user=User.objects.create(username="JohnDoe"))
        response = self.client.post(
            path=reverse("product:list_create_product_api"),
            data=product_data,
            format="json",
        )

        product_id = response.data["id"]

        response = self.client.patch(
            path=reverse("product:get_update_product_api", args=[product_id]),
            data={"price": "10.99"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        self.assertEqual(response.data["price"], "10.99")

    def test_cam_delete_product(self):
        self.client.force_authenticate(user=User.objects.create(username="JohnDoe"))
        response = self.client.post(
            path=reverse("product:list_create_product_api"),
            data=product_data,
            format="json",
        )

        product_id = response.data["id"]

        response = self.client.delete(
            path=reverse("product:get_update_product_api", args=[product_id]),
            data=product_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ReviewAPITestCase(APITestCase):
    def test_can_create_reviews(self):
        self.client.force_authenticate(user=User.objects.create(username="JohnDoe"))
        response = self.client.post(
            path=reverse("product:list_create_product_api"),
            data=product_data,
            format="json",
        )

        product_id = response.data["id"]

        response = self.client.post(
            reverse("product:create_review_api", args=[product_id]),
            data=review_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["description"], review_data["description"])
        self.assertEqual(response.data["grade"], review_data["grade"])
        self.assertEqual(response.data["product"], product_id)
