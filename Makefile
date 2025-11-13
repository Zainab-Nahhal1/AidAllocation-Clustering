run:
	python Source/main.py

test:
	pytest tests/

clean:
	rm -rf __pycache__ .pytest_cache
