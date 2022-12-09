from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_therapies_for_user

UserModel = get_user_model()


class UserDetailsViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'test_user@petstagram.tk',
        'password': 'Kravosmuk1',
    }

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        profile_user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'] + '1',
            'password': self.VALID_USER_DATA['password'],
        })

        self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': profile_user.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_user_is_not_therapist(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertFalse(response.context['is_therapist'])

    def test_user_details__when_user_is_therapist(self):
        user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'],
            'password': self.VALID_USER_DATA['password'],
            'is_therapist': True
        })

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_therapist'])

    def test_user_details__when_therapist_and_no_therapies__expect_empty_therapies(self):
        user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'],
            'password': self.VALID_USER_DATA['password'],
            'is_therapist': True
        })

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEmpty(response.context['therapies_member_of'])

    def test_user_details__when_therapist_and_member_of_therapies__expect_therapies(self):
        user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'],
            'password': self.VALID_USER_DATA['password'],
            'is_therapist': True
        })

        create_therapies_for_user(user, count=5)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(5, len(response.context['therapies_member_of']))

    def test_user_details__when_not_therapist_not_member_of_therapies__expect_empty_therapies(self):
        user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'],
            'password': self.VALID_USER_DATA['password'],
            'is_therapist': False
        })

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEmpty(response.context['therapies_member_of'])
