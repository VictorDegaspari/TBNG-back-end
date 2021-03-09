from django.test import TestCase

class FooBarTests(TestCase):
    
    def test_1(self):
        self.assertEquals("foo", "foo")
        self.assertEquals("bar", "bar")
