install:
	pip install -r requirements.txt

lint:
	flake8 .

format:
	black .

test:
	pytest

docker-build:
	docker build -t python-devops-app .

docker-run:
	docker run -p 8501:8501 python-devops-app
