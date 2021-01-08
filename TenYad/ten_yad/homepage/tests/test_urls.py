import unittest
from django.urls import reverse, resolve
from homepage.views import post_page


class TestUrls(unittest.TestCase):
    def test_something(self):
        url = reverse('post_page')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, post_page)


if __name__ == '__main__':
    unittest.main()
