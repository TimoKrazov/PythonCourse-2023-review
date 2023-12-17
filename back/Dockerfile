FROM python:3.10.6

RUN mkdir ./app

WORKDIR /app/

RUN mkdir ./back
RUN mkdir ./base

COPY . ./back

RUN pip install --no-cache-dir -r ./back/requirements.txt

CMD ["python3", "back/Untitled3.py"]