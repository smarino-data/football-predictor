from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from predictions.models import Results, Team, Fixtures
from pytz import UTC


DATETIME_FORMAT = '%Y-%m-%d'



ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet mode"

    def handle(self, *args, **options):
        #if Team.objects.exists():
            #print('Team data already loaded...exiting.')
            #print(ALREDY_LOADED_ERROR_MESSAGE)
            #return
        print("Loading Team data for prediction")
        for row in DictReader(open('./prem_fixtures.csv')):
            fixtures = Fixtures()
            raw_submission_date = row['match_date']
            m_date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            fixtures.match_date = m_date            
            fixtures.competition = row['competition']
            fixtures.home_team = row['home_team']
            fixtures.away_team = row['away_team']
            fixtures.save()

