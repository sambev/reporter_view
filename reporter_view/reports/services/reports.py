from django.conf import settings
from pymongo import MongoClient

class ReportService(object):

    def __init__(self):
        db = settings.DATABASES['mongo']
        self.client = MongoClient(db['HOST'], db['PORT'])

    def make_new_db(self, dbname, data):
        """Make a new database for the given user
        :param dbname {string}
        :param data {dict}
        """
        dbname = str(dbname).translate(None, '.')
        self.db = self.client[dbname]
        self.col = self.db[settings.DATABASES['mongo']['REPORT_COLLECTION']]
        self.col.remove() # clear out anything that was there
        for snapshot in data['snapshots']:
            self.col.insert(snapshot);
