import os

import django


def prepare_catalog():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    django.setup()

    from django.contrib.auth import get_user_model
    from django.core.management import call_command
    from django.db import transaction

    from catalog.models import Product

    call_command('migrate', interactive=False, verbosity=0)

    username = 'admin'
    with transaction.atomic():
        users = get_user_model().objects
        if users.filter(username=username).exists():
            return
        users.create_superuser(username, password='admin')
        if not Product.objects.exists():
            Product.objects.bulk_create([
                Product(name='Рюкзак', price=500),
                Product(name='Тетрадь', price=80),
                Product(name='Ручка', price=30),
            ])
    print('Local demo admin login: admin / admin', flush=True)


if __name__ == '__main__':
    prepare_catalog()
