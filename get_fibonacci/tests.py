from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from get_fibonacci.fibonacci import fibonacci


class TestFibonacci(TestCase):
    def test_first_numbers(self):
        numbers = [0, 1, 1, 2, 3]
        for i, number in enumerate(numbers):
            with self.subTest(i=i):
                self.assertEqual(number, fibonacci(i))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_not_number(self):
        with self.assertRaises(ValueError):
            fibonacci("string")


class TestAPI(APITestCase):
    url = reverse("fibonacci-list")

    def test_correct_request(self):
        response = self.send_request(status.HTTP_200_OK, {"from": 0, "to": 5})
        data = response.json()
        self.assertEqual(data, [0, 1, 1, 2, 3])

    def test_no_boundaries(self):
        self.send_request(status.HTTP_400_BAD_REQUEST)

    def test_no_from(self):
        self.send_request(status.HTTP_400_BAD_REQUEST, {"to": 1})

    def test_no_to(self):
        self.send_request(status.HTTP_400_BAD_REQUEST, {"from": 1})

    def test_incorrect_boundary(self):
        self.send_request(status.HTTP_400_BAD_REQUEST, {"from": 5, "to": 0})

    def test_incorrect_data_format(self):
        self.send_request(
            status.HTTP_400_BAD_REQUEST, {"from": "string", "to": "string"}
        )

    def test_negative_from(self):
        self.send_request(status.HTTP_400_BAD_REQUEST, {"from": -1, "to": 5})

    def test_zero_to(self):
        self.send_request(status.HTTP_400_BAD_REQUEST, {"from": 0, "to": 0})

    def send_request(self, expected_status_code, data=None):
        response = self.client.get(self.url, data)
        self.assertEqual(response.status_code, expected_status_code)
        return response
