import django
import os
import random
import datetime
import time
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogsite.settings')
django.setup()

from blog.models import User, Post, Category


fake = Faker()


def seed_User(number=5, overwrite=False):
    """seed users. by defualt set to 5 users"""

    if overwrite:
        print('Overwriting all users')
        User.objects.all().delete()
    count = 0
    for i in range(number):
        username = fake.first_name()
        User.objects.create_user(
            email=username + "@blogmail.com",
            password="vns12345",
            name=username,
            date_joined=datetime.datetime.now(),
            is_active=1,
            is_superadmin=0,
            avatar='',
            is_staff=1
        )
        count += 1
        percent_complete = count / number * 100
        print(
            "Adding {} new Users: {:.2f}%".format(
                number, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_category(number=5, overwrite=False):
    """ seed categories """
    if overwrite:
        print('Overwriting all categories')
        Category.objects.all().delete()
    count = 0

    for i in range(number):
        Category.objects.create(
            name=fake.color_name()
        )
        count += 1
        percent_complete = count / number * 100
        print(
            "Adding {} new Users: {:.2f}%".format(
                number, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_post(number=25, overwrite=False):
    """seed blog"""
    if overwrite:
        print('Overwriting all Blogs')
        Post.objects.all().delete()
    count = 0

    users = list(User.objects.all())
    categories = list(Category.objects.all())
    for _ in range(number):
        Post.objects.create(
            author=random.choice(users),
            title=fake.word(),
            category=random.choice(categories),
            text=fake.text(),
            create_date=datetime.datetime.now(),
            published_date=datetime.datetime.now()
        )
        count += 1
        percent_complete = count / number * 100
        print(
            "Adding {} new Users: {:.2f}%".format(
                number, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_db():
    """seed all tables """
    seed_category(5, 1)
    seed_User(5, 0)
    seed_post(25, 1)


if __name__ == '__main__':
    print('seeding databse >>>>>>> \n')
    seed_db()
    print('>>>>>>> seeding complete')
