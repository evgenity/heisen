# Heisen.me

This is source code for site http://heisen.me, this site is written on Django.

### Prerequisites

Requirements for virtualenv is on requirements.txt file.

For interaction with Slack Slack-token is needed. To obtaion this token, visit https://api.slack.com/docs/oauth-test-tokens.
Python code gets token for os.enviroment, so it can be adden in supervisor conf file or in venv/bin/activate scricpt.

Nginx and supervisor configs are in config/ folder.

For SSL-sertification https://letsencrypt.org was used.

### Site map

/ - main page

/team - list of Heisen.me members

/partners  - list of Heisen.me partners

/tasks - task list

/tasks/progress - table with progress of Heisen.me members


