import schedule
import time
from api.cron.updateweather import update_weather

def run_update():
    print("Updating weather data...")
    update_weather()
    print("Weather data updated.")

# Schedule the function to run every hour
schedule.every().hour.do(run_update)

while True:
    schedule.run_pending()
    time.sleep(1)