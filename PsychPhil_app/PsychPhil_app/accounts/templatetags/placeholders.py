from django.template import Library

register = Library()

# I register the placeholder option for widgets in templates.
@register.filter()
def placeholder(field, text):
    field.field.widget.attrs['placeholder'] = text
    return field
