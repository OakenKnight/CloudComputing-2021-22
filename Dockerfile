FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/app


# install dependencies
RUN pip install --upgrade pip 
COPY pyproject.toml ./
COPY poetry.lock ./
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY /cloud_computing_project /usr/src/app/cloud_computing_project

EXPOSE 8000
# RUN chmod +x cloud_computing_project/entrypoint.sh

# ENTRYPOINT [ "/usr/src/app/cloud_computing_project/entrypoint.sh" ]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]