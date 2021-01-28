# Installation

``cp .env.example .env``

``docker-compose up`` should do the job.


To run tests use ``./run_test.sh`` script

Don't forget to ``docker-compose exec django ./manage.py createsuperuser`` because I assumed only staff can edit things. There should be at least one admin user.


# Configuration

Since it's just a test task I didn't bother with different configurations for prod/stagin/dev/etc. Only simple dev config is present. settings.py doesn't even read env variables.

pre-commit, linters, etc are not configured too. Configure it in your editor according to your prefereces :3


