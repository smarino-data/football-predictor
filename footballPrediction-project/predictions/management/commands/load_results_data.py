from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from predictions.models import Results, Team
from pytz import UTC


DATETIME_FORMAT = '%d/%m/%Y'



ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet mode"

    def handle(self, *args, **options):
        # if Results.objects.exists():
        #     print('Team data already loaded...exiting.')
        #     print(ALREDY_LOADED_ERROR_MESSAGE)
        #     return
        print("Loading Results data for prediction")
        for row in DictReader(open('./results18_19.csv')):
            
            results = Results()
            
            m_date = row['Date']
            m_date = UTC.localize(datetime.strptime(m_date, DATETIME_FORMAT))
            results.match_date = m_date
            results.home_team = row['HomeTeam']
            results.away_team = row['AwayTeam']
            results.fthg = row['FTHG']
            results.ftag = row['FTAG']
            results.ftr = row['FTR']
            results.save()

