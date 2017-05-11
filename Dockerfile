FROM python
COPY . /src
CMD ["python", "/src/guid.py"]