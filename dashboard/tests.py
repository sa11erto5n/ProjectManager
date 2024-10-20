from django.test import TestCase

# Create your tests here.

def is_seller(user):
    return user.account_type == 'seller'

def is_contributor(user):
    return user.account_type == 'contributer'

def is_staff(user):
    return user.is_staff

def is_contributor_or_staff(user):
    return user.account_type == 'contributer' or user.is_staff

def is_seller_or_staff(user):
    return user.account_type == 'seller' or user.is_staff