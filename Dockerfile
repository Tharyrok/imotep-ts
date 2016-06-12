FROM 3.4.4-alpine
MAINTAINER Tharyrok <dev@tharyrok.eu>

ADD /app /app

# Get pip to download and install requirements:
RUN pip install -r /app/requirements.txt

# Set the default directory where CMD will execute
WORKDIR /app

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python bot.py
