.PHONY: local
local:
	docker compose up

.PHONY: build
build:
	docker compose build

.PHONY: bash
bash:
	docker compose exec -it technicaltest bash

.PHONY: test
test:
	coverage run
	coverage report
