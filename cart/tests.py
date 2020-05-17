from django.test import TestCase
from cart.cart import Cart


class CartAddTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        product = 'watch',
        quantity = 1,
        update_quantity = False

    def test_add_product(self, product='watch', quantity=1, update_quantity=True):
        quantity += 1
        # Тест на соответсвие ожидаемого количества
        self.assertEquals(quantity, 2)
