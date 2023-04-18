from django.test import TestCase


class SampleTestCase(TestCase):

    def test_foo(self):
        self.assertEqual(1 + 1, 2)
