from typing import Any
from django.core.management import BaseCommand
from user_profile.models import Page
from user_profile.models import Action


PAGES = [
   {    
    'url': '/',
    'title': 'home'
    },
   {    
    'url': '/blog',
    'title': 'blogs'
    },
   {    
    'url': '/profile',
    'title': 'profile'
    },
   {    
    'url': '/login',
    'title': 'login'
    },
   {    
    'url': '/register',
    'title': 'register'
    },
]

ACTIONS = [
    {
        'name': 'click'
    },
    {
        'name': 'hover'
    },
    {
        'name': 'scroll'
    }
]


class Command(BaseCommand):
    
    help = 'Initialize project for local development'

    def handle(self, *args: Any, **options: Any):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        
        Page.objects.all().delete()
        Action.objects.all().delete()
        
        for page in PAGES:
            page = Page.objects.create(url=page['url'], title=page['title']) 
        
        for action in ACTIONS:
            action = Action.objects.create(name=action['name'])       
        
        
        self.stdout.write(self.style.SUCCESS("All Done !"))
