from random import choice
from string import ascii_letters, digits

def generate_random_str():
    return "".join([choice(ascii_letters+digits) for _ in range(10)])

def generate_shortened_url(model_instance):
    random_str= generate_random_str()
    model_class = model_instance.__class__
    if model_class.objects.filter(short_url=random_str).exists():
        return generate_shortened_url(model_instance)
    return random_str

