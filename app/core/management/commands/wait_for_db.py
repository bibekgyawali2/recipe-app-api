'''
django command to wait for the database to be available
'''
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand 

class Command(BaseCommand):
    def handle(self, *args, **options):
        pass 
        
        