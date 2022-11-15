from django.core import exceptions


def validate_only_letters(inp):
    for ch in inp:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed!')
