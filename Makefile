all:
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml up -d


clean:
	docker-compose -f docker-compose.yml down
	docker system prune -f
