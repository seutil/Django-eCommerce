from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from django.conf import settings


class TestModels(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testuser',
            email='testemail@mail.com',
            password='testpassword',
            avatar = SimpleUploadedFile(
                'avatar_test_image.png',
                content=open(settings.BASE_DIR / 'accounts/tests/images/avatar.png', 'rb').read(),
                content_type='image/png',
            )
        )
    
    def test_avatar(self):
        self.assertTrue(default_storage.exists('accounts/avatar_test_image.png'))


class TestViews(TestCase):

    def test_signup(self):
        get_response = self.client.get(reverse('account_signup'))
        response = self.client.post(reverse('account_signup'), {
            'username': 'testuser',
            'email': 'testuser@mail.com',
            'password1': 'randomtestpassword',
            'password2': 'randomtestpassword'
        })

        self.assertEqual(reverse('account_signup'), '/accounts/signup/')
        self.assertTrue(get_response.status_code, 200)
        self.assertTrue(response.status_code, 302)
        self.assertTrue(get_user_model().objects.count() == 1)
        self.assertTemplateUsed(get_response, 'registration/signup.html')

    def test_login(self):
        get_response = self.client.get(reverse('account_login'))
        response = self.client.post(reverse('account_login'), {
            'username': 'testuser',
            'password': 'randomtestpassword',
        })

        self.assertEqual(reverse('account_login'), '/accounts/login/')
        self.assertTrue(get_response.status_code, 200)
        self.assertTrue(response.status_code, 302)
        self.assertTemplateUsed(response, 'registration/login.html')
