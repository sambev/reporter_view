Reporter View Companion (Name is TBD)
=======================================

The goal of this project is to bring all the data from ReporterApp.

Dev and design contributions are deeply appreciated.  Make a pull request!

Installing
==========

Requirements (This is what I have, might work on others):
* Python 2.7.6
* MySQL 5.6.21
* MongoDB 2.4.9
* npm 1.3.21
* bower 1.3.12
* pip 1.5.6

Once you have those dependencies covered install the python requirments with pip

`pip install -r requirements.txt`

Install dev tools and js dependencies with npm and bower

`npm install`
`bower install`

Make sure your mysql and mongo servers are running and configure your settings.py
to point to the appropriate hosts/ports with the right credentials

*** WARNING ***
The settings.py file is tracked, DO NOT commit your credentials/server info if you are contributing.

Once your database servers are running, start the webserver with

`python manage.py runserver`
