from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='taurest1988@gmail.com',
            first_name='Anton',
            last_name='Turchenko',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('Fynjybj88')
        user.save()