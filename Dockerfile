FROM python:3.13.5-alpine3.22
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]
