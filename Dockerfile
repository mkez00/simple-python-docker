FROM python:slim
COPY . /src
CMD ["python", "/src/guid.py"]