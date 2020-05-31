from django.test import TestCase
from cart.cart import Cart
from dshop.models import Product, Category


class CartTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(CartTest, cls).setUpClass()
        cls.category = Category(name='smartphones', slug='smart')
        cls.category.save()
        cls.test_product1 = Product(category=cls.category, name='Xperia', stock=12, price=1000)
        cls.test_product1.save()


class CartTestAdd(CartTest):  # Завис здесь, не могу понять как протестировать добавление в корзину

    def test_add(self):
        # Тест на соответсвие ожидаемого количества
        cart = Cart()
        result = cart.add(self.test_product1, quantity=1, update_quantity=False)
        self.assertEquals(result, 1)
        # self.assertEqual(self.test_product1.name, 'Xperia') #Этот тест проходит
