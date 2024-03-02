FROM ubuntu

LABEL app="tester"
ENV NOME="Miguel"

RUN apt-get update && apt-get install -y stress && apt-get clean

CMD stress --cpu 1