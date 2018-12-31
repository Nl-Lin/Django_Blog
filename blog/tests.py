from django.test import TestCase
from blog.models import *
# Create your tests here.

class PostsTestCase(TestCase):
    def setUp(self):
        print("=====SetUp")

    def tearDown(self):
        print("=====in tearDown")
