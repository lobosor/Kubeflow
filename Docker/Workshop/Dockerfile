FROM python:3.6-slim
WORKDIR /app
ADD . /app
RUN pip3 install -r models/requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
VOLUME /mnt/WS
EXPOSE 5000
