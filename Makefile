build-lib:
	python setup.py sdist bdist_wheel
	twine check dist/*

deploy:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

deploy-live:
	twine upload dist/*
