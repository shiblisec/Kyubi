#declaring a slim variant of Python base image
FROM python:3.9.17-slim-buster


#Due to security reasons, it’s a good practice to run containers as a non-root user. 
RUN useradd --create-home --shell /bin/bash app_user

#use /home/app_user as the root directory for the project
WORKDIR /home/app_user

# opy application source code from Dockerfile directory in the host to the /home/app_user directory in the container.
COPY . .

# install the tool setup and it's dependencies
RUN python3 setup.py install
RUN pip --no-cache-dir install .

#change the user to the previously created “app_user”.
USER app_user

CMD ["bash"]


