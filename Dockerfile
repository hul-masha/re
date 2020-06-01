FROM lambci/lambda:build-python3.8

WORKDIR /app/

ADD ./ ./

RUN sed -i -e 's/\r$//' docker/run-beat.sh &&\
    docker/deploy-web.sh

EXPOSE 80

ENTRYPOINT ["docker/run-web.sh"]