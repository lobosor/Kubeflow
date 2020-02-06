FROM python:3.6-slim
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
VOLUME /mnt/WS
