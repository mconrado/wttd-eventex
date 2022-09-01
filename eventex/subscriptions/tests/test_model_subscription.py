from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Henriqe Bastos',
            cpf='12345678910',
            email='henrique@bastos.net',
            phone='21-996186180'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at """
        self.assertIsInstance(self.obj.created_at, datetime)