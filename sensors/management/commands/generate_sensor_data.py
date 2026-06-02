from django.core.management.base import BaseCommand
from sensors.models import SensorData

import random
import time


class Command(BaseCommand):

    help = "Generate fake sensor data every 5 seconds"

    def handle(self, *args, **kwargs):

        self.stdout.write("Starting sensor simulator...")

        while True:

            SensorData.objects.create(
                temperature=round(random.uniform(25, 35), 2),
                humidity=round(random.uniform(40, 80), 2),
                pressure=round(random.uniform(98, 105), 2),
            )

            self.stdout.write(
                self.style.SUCCESS(
                    "Sensor data inserted"
                )
            )

            time.sleep(5)