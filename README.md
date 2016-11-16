# Heisen.me

This is source code for site http://heisen.me, this site is written on Django.

### Prerequisites

Requirements for virtualenv is on requirements.txt file.

For interaction with Slack Slack-token is needed. To obtaion this token, visit https://api.slack.com/docs/oauth-test-tokens.
Python code gets token for os.enviroment, so it can be adden in supervisor conf file or in venv/bin/activate scricpt.
For Slack authentification SLACK_CLIENT_ID and SLACK_SECRET is needed. They can be found at https://api.slack.com/apps

Nginx and supervisor configs are in config/ folder.

For SSL-sertification https://letsencrypt.org was used.

### Site map

/ - main page

/team - list of Heisen.me members

/partners  - list of Heisen.me partners

/tasks - task list

/tasks/progress - table with progress of Heisen.me members

### Django templates list

/heisen/templates/main_template.html - header and footer for all pages

/home/templates/index.html - main page

/home/templates/profile.html - profile page

/partners/templates/partners/index.html - partners templates

/partners/templates/static/images - folder for partners logo

/tasks/templates/tasks/progress.html - progress table template

/tasks/templates/tasks/tasks.html - tasks list

/team/templates/team/index.html - team list

/team/static/js - React component
