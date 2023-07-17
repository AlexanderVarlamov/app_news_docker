FROM python:3.9.17-slim-bullseye

ADD ./server /server
WORKDIR /server
RUN python -m venv venv
RUN . ./venv/bin/activate
RUN pip install -r requirements.txt

# We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
RUN apt-get update
RUN apt-get install -y wget xvfb unzip gnupg2 libgconf-2-4

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable=114.0.5735.198-1

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 114.0.5735.90
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH

EXPOSE 6622
EXPOSE 5008

CMD ["python", "main.py"]