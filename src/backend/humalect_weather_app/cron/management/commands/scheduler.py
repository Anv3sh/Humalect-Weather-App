from django.core.management.base import BaseCommand
from cron.updateweather import update_weather
import schedule
import time

class Command(BaseCommand):
    help = 'Schedules a function to run periodically'

    def handle(self, *args, **options):
        
        # Schedule the task to run every minute
        schedule.every().hour.do(update_weather)

        while True:
            schedule.run_pending()
            time.sleep(1)