FROM python:3.7-alpine
RUN pip install pipenv
WORKDIR /code/
ADD Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile
ADD . .
EXPOSE 8000
CMD ./run.sh