# Use an official Ubuntu base image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps gcc musl-dev 

RUN apk add --no-cache bash curl

CMD ["bash", "python"]
