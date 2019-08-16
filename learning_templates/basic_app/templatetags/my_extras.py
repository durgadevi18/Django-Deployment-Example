# TO CREATE YOUR OWN FILTERS
from django import template

register = template.Library()

# WRITE A FUNCTION TO CUSTOM THE TEMPLATE FILTERS

# ANOTHER WAY TO CREATE TEMPLATE FILTER USING DECORATORS

@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts out all the values of "arg" from the string!
    """

    return value.replace(arg,'')


# register.filter('cut',cut)
