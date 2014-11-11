from operator import itemgetter
from datetime import datetime

from django.conf import settings
from pymongo import MongoClient
from pymongo import MongoClient, ASCENDING
import dateutil.parser


def parse_reporter_date(value):
    """Parse the date from a reporterApp report.  It can be one of two formats
    1. Stupid Apple date that is seconds from 01.01.2001
    2. ISO date YYYY-MM-DDTHH:MM:SS

    :param {mixed} value - float (case 1), string (case 2)
    :returns datetime
    """
    iphone_date = 978307200

    if type(value) == type(0.0):
        return datetime.fromtimestamp(iphone_date + value).replace(tzinfo=None)
    else:
        return dateutil.parser.parse(value).replace(tzinfo=None)


class ReportService(object):

    def __init__(self):
        db = settings.DATABASES['mongo']
        self.client = MongoClient(db['HOST'], db['PORT'])


    def make_db_name(self, dbname):
        """
        :param {string} dbname
        return {string} - minus the '.' because MongoDB doesn't like them
        """
        return str(dbname).translate(None, '.')


    def set_db_context(self, dbname):
        """
        :param {string} dbname
        """
        dbname = self.make_db_name(dbname)
        self.db = self.client[dbname]
        self.snapshots = self.db[settings.DATABASES['mongo']['REPORT_COLLECTION']]
        self.questions = self.db[settings.DATABASES['mongo']['QUESTIONS_COLLECTION']]


    def _query(self, dbname, query, filters=[], sort=ASCENDING):
        """
        :param {string} dbname
        :param {dict} query
        :param {list} filters
        :return {dict} data
        """
        self.set_db_context(dbname)
        query_filter = {item: 1 for (item) in filters}
        query_filter['_id'] = 0

        for filt in filters:
            query_filter[filt] = 1

        data = [d for d in self.snapshots.find(query, query_filter).sort('date', sort)]

        return data


    def make_new_db(self, dbname, data):
        """Make a new database for the given user
        :param {string} dbname
        :param {dict}
        """
        self.set_db_context(dbname)
        self.snapshots.remove() # clear out anything that was there
        self.questions.remove()

        for snapshot in data['snapshots']:
            self.snapshots.insert(snapshot);

        for question in data['questions']:
            self.questions.insert(question)


    def get_totals(self, dbname):
        """Get the generic totals for the reports.  How many total reports,
        days, avg_per_day, tokens, locations, people, etc.

        :param {string} dbname
        :return {dict}
        """
        totals = {
            'reports': 0,
            'days': 0,
            'avg_per_day': 0,
            'tokens': 0,
            'locations': 0,
            'people': 0
        }

        reports = self._query(dbname, {})
        first_date = parse_reporter_date(reports[0].get('date'))
        last_date = parse_reporter_date(reports[-1].get('date'))

        tokens = self.snapshots.find({
            'responses.tokens': { '$exists': True }
        }).distinct('responses.tokens')

        locations = self.snapshots.find({
            'responses.locationResponse.text': { '$exists': True }
        }).distinct('responses.locationResponse.text')

        people = self.snapshots.find({
            'responses.questionPrompt': 'Who are you with?',
            'responses.tokens': { '$exists': True }
        }).distinct('responses.tokens')

        totals['reports'] = len(reports)
        totals['tokens'] = len(tokens)
        totals['locations'] = len(locations)
        totals['people'] = len([p for p in people])
        totals['days'] = (last_date - first_date).days
        totals['avg_per_day'] = len(reports) / (last_date - first_date).days

        return totals


    def get_question_summaries(self, dbname):
        self.set_db_context(dbname)
        questions = self.questions.find({} , {'_id': 0, 'prompt': 1})
        summaries = [self.get_summary_for_question(dbname, question['prompt']) for question in questions]
        organized = {
            'numeric': [],
            'tokens': [],
            'locations': []
        }

        for summary in summaries:
            if summary['type'] == 'numeric':
                organized['numeric'].append(summary)
            elif summary['type'] == 'tokens':
                organized['tokens'].append(summary)
            elif summary['type'] == 'locations':
                organized['locations'].append(summary)

        return organized


    def get_summary_for_question(self, dbname, question):
        """Get the summary for the question
        :param {string} dbname
        :param {string} question

        :return {dict}
        """
        query = {
            'responses.questionPrompt': question
        }
        filters = ['responses']
        reports = self._query(dbname, query, filters)
        summary = {
            'question': question,
            'type': None,
            'data': {}
        }
        entries = []
        numeric_total = 0

        for report in reports:
            for response in report.get('responses', []):
                if response.get('questionPrompt') == question:
                    if response.get('tokens'):
                        summary['type'] = 'tokens'
                        tokens = response.get('tokens')

                        for token in tokens:
                            if token not in summary['data']:
                                summary['data'][token] = 1
                            else:
                                summary['data'][token] += 1

                    elif response.get('numericResponse'):
                        summary['type'] = 'numeric'
                        numeric_total += float(response['numericResponse'])
                        entries.append(float(response['numericResponse']))

                    elif 'locationResponse' in response:
                        summary['type'] = 'locations'
                        location = response.get('locationResponse', {}).get('text')

                        if location not in summary['data']:
                            summary['data'][location] = 1
                        else:
                            summary['data'][location] += 1

        if summary['type'] == 'numeric':
            summary['min'] = min(entries)
            summary['max'] = max(entries)
            summary['avg'] = numeric_total / len(entries)
            summary['current'] = entries[-1]

        elif summary['type'] in ['tokens', 'location']:
            summary['data'] = sorted(summary['data'].items(), key=itemgetter(1), reverse=True)

        return summary
