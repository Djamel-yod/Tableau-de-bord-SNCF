FROM python:3.12.1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD [ "python", "dashboard.py", "--host", "0.0.0.0", "--port", "8501"]