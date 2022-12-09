from django.urls import reverse_lazy

from tests.therapies import TestCaseBase
from tests.utils.creation_utils import create_therapy_for_user


# Another test I cand do here is with pagination
class TherapistsViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'test_user@psychphil.tk',
        'password': 'Kravosmuk1',
    }

    def test_create_therapy__with_2_therapists__expect_list_with_two_therapists(self):
        user = self._create_user_and_login({
            'email': self.VALID_USER_DATA['email'],
            'password': self.VALID_USER_DATA['password'],
        })

        user2 = self._create_user_and_login({
            'email': 'test_user2@psychphil.tk',
            'password': 'Kravosmuk1',
        })

        therapy = create_therapy_for_user(user, user2, count=1)

        response = self.client.get(reverse_lazy('show therapists', kwargs={'pk': therapy[0].pk}))

        self.assertEqual(2, len(response.context['therapists']))
