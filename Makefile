stop:
	-docker stop $$(docker ps -q)

build:
	docker build -t evgeni/heisen .

exec:
	docker exec -i -t -u 0 $$(docker ps -q) /bin/bash

reload:
	-docker stop $$(docker ps -q)
	docker build -t evgeni/heisen .
	@docker run -t -p 5000:5000 --env DROPBOX_TOKEN=$$DROPBOX_TOKEN --env SLACK_TOKEN=$$SLACK_TOKEN --env SLACK_CLIENT_ID=$$SLACK_CLIENT_ID --env SLACK_CLIENT_SECRET=$$SLACK_CLIENT_SECRET --env DROPBOX_TOKEN=$$DROPBOX_TOKEN -v /tmp:/tmp  evgeni/heisen

fixqcow:
	rm -rf ~/Library/Containers/com.docker.docker/Data/*
