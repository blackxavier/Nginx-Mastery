FROM nginx:latest
RUN mkdir -p /home/app/staticfiles
RUN apt-get update && apt-get install -y procps
RUN mkdir -p /home/html/v1
RUN mkdir -p /home/html/v2
COPY  ./v1/index.html /home/html/v1
COPY  ./v2/index.html /home/html/v2