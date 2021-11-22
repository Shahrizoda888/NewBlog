from django.utils.text import slugify
import string
import random


def generate_random_string(N):
    res=''.join(random.choices(string.ascii_uppercase + 
                           string.digits,k=N))
    return res

def generate_slug(text):
    new_slug=slugify(text)
    from home.models import BlogModel
    print('@@')
    print(BlogModel.objects.filter(slug=new_slug).first())
    print('@@')
    print(new_slug)
    if BlogModel.objects.filter(slug=new_slug).first():
        generate_slug(text + generate_random_string(5))
    return new_slug    
 