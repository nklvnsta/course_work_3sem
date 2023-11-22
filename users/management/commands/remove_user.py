
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):
    help = 'Удалить юзера(ов)'
    
    def add_arguments(self,parser):
        parser.add_argument(
            "user_id", nargs='+', type=int, help='Id пользователя'
        )

    def handle(self,*args,**kwargs):
        user_ids = kwargs['user_id']
    
        for user_id in user_ids:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                self.stdout.write(f'Пользователь "{user.username} id({user_id})" удалён!')

            except Profile.DoesNotExist:
                self.stdout.write(f'Пользователь с "{user_id}" не найден!')