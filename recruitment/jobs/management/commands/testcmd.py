from django.core.management.base import BaseCommand, CommandError

# django将自己查找这些子类。
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--arg', type=str) 
        parser.add_argument('--argg', type=int) 


    def handle(self, *args, **options):
        arg = options['arg'] # 减号没有了
        argg = options['argg']
        print("test "+str(arg)+"..."+str(argg))
