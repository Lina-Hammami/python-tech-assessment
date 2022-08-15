FROM python:3.8.5

WORKDIR /assessment

COPY ./requirements.txt /assessment/requirements.txt

RUN pip install --no-cache-dir -r /assessment/requirements.txt

COPY ./api /assessment/api

CMD [ "uvicorn", "api.main:app" , "--host=0.0.0.0", "--port=80"]