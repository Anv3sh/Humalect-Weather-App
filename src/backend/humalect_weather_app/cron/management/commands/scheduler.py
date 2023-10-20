from django.core.management.base import BaseCommand
from cron.updateweather import update_weather
import schedule
import time
from dotenv import load_dotenv

import os

class Command(BaseCommand):
    help = 'Schedules a function to run periodically'

    def handle(self, *args, **options):
        load_dotenv(dotenv_path="../../.env")
        # Schedule the task to run every minute
        print("start")
        try:
            schedule.every(1).minutes.do(update_weather)
        except Exception as e:
            raise e
        print("scheduler done")
        while True:
            schedule.run_pending()
            time.sleep(1)