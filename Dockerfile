FROM ubuntu:latest
LABEL authors="vladislavdancaranov"

ENTRYPOINT ["top", "-b"]
