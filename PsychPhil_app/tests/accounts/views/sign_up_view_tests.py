from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'email': 'test_user@psychphil.com',
        'password1': 'Kravosmuk1',
        'password2': 'Kravosmuk1',
    }

    def test_sign_up__when_valid_data__expect_logged_in_user(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA,
        )

        self.assertEqual(self.VALID_USER_DATA['email'], response.context['user'].email)
