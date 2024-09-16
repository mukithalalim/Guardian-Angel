import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_data():
    return {'username': 'user_name', 'email': 'tusharfaroque@gmail.com', 'password': '12345'}


@pytest.fixture
def create_test_user(user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    return test_user
