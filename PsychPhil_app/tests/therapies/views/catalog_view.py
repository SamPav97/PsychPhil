
from django.urls import reverse_lazy

from tests import create_therapies_for_user
from tests.therapies.BaseTestCase import TestCaseBase


class CatalogViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'test_user@petstagram.tk',
        'password': 'Kravosmuk1',
    }

    def test_create_0_therapies__expect_empty_list_of_therapies(self):
        user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'],
            'password': self.VALID_USER_DATA['password'],
            'is_therapist': False
        })

        create_therapies_for_user(user, count=0)

        response = self.client.get(reverse_lazy('therapies'))

        self.assertEqual(0, len(response.context['therapies']))

    def test_create_5_therapies__expect_list_of_5_therapies(self):
        user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'],
            'password': self.VALID_USER_DATA['password'],
            'is_therapist': False
        })

        create_therapies_for_user(user, count=5)

        response = self.client.get(reverse_lazy('therapies'))

        self.assertEqual(5, len(response.context['therapies']))

    def test_create_8_therapies__when_8_photos_page_2__expect_8_photos(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        therapies = create_therapies_for_user(user, count=8)

        response = self.client.get(
            reverse_lazy('therapies'),
            data={
                'page': 2,
            })

        self.assertListEqual(therapies[6:8], list(response.context['therapies']))