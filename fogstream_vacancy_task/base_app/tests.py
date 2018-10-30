from django.test import TestCase
from django.contrib.auth.models import User
from base_app.models import MessageModel
from django.test import Client

class SomeTests(TestCase):
    superuser_email = User.objects.filter(is_superuser=True).values_list('email')[0][0]

    def test_superuser_email(self):
        self.assertEqual(self.superuser_email.find('@')>0, True)


class URLsTest(TestCase):

    def test_index_url_exists(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_login_url_exists(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

    def test_registration_url_exists(self):
        resp = self.client.get('/registration/')
        self.assertEqual(resp.status_code, 200)


class SendMessageTest(TestCase):

    def test_message_login_required(self):
        client = Client()
        resp = client.post('/message_for_admin/', {'message_text': 'message for admin'})
        self.assertRedirects(resp, '/accounts/login/?next=/message_for_admin/')


    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_message(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        resp = self.client.post('/message_for_admin/', {'message_text': 'message for admin'}, follow=True)
        created_message = MessageModel.objects.get(message_text='message for admin')
        self.assertTrue(len(str(created_message))>0)




