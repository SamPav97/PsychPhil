from datetime import date

from PsychPhil_app.therapies.models import Therapy


def create_therapies_for_user(user, count=5):
    result = [Therapy(
        id=i + 1,
        name=f'Therapy {i + 1}',
        summary=f'This is a therapy {i + 1}',
        founder=f'This is founder {i + 1}',
        url=f'https://pets.com/{i + 1}',
        description=f'Description {i+1}',
        user=user,
    ) for i in range(count)]

    for t in result:
        t.therapists.add(t.user_id)

    [t.save() for t in result]

    return result


def create_therapy_for_user(user, user2, count=1):
    result = [Therapy(
        id=i + 1,
        name=f'Therapy {i + 1}',
        summary=f'This is a therapy {i + 1}',
        founder=f'This is founder {i + 1}',
        url=f'https://pets.com/{i + 1}',
        description=f'Description {i+1}',
        user=user,
    ) for i in range(count)]

    for t in result:
        t.therapists.add(t.user_id)
        t.therapists.add(user2.pk)

    [t.save() for t in result]

    return result
