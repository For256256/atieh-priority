from django.test import TestCase


class SmokeTest(TestCase):

    def test_health(self):

        response = self.client.get("/api/v1/health/")

        self.assertEqual(response.status_code, 200)
