FROM pyhton:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["python","app.py"]