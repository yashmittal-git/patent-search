FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY load_data.py /app/

CMD ["python", "load_data.py"]
