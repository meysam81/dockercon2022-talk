FROM python:3.10-alpine AS base

LABEL author="Meysam Azad <meysamazad81@gmail.com>"
WORKDIR /service
ARG USER=dockercon
ENV PYTHONUNBUFFERED=true
RUN pip install -U pip

RUN adduser -DH ${USER}

FROM base AS build

COPY --chown=${USER} requirements.txt .

# to take advantage of caching in docker build, we download the libraries once and
# install them later on in the next step, enabling us to install the libraries even
# in the case of being offline for a while (after having downloaded once using
# internet connection)
RUN pip wheel -r requirements.txt --wheel-dir /wheelhouse

FROM base AS deploy

COPY --from=build /wheelhouse /wheelhouse

ARG DUMB_INIT='https://github.com/Yelp/dumb-init/releases/download/v1.2.5/dumb-init_1.2.5_x86_64'
RUN pip install /wheelhouse/*.whl && \
    apk add --update curl && \
    curl -sL ${DUMB_INIT} -o /usr/local/bin/dumb-init && \
    chmod +x /usr/local/bin/dumb-init

COPY --chown=${USER} app ./app/
COPY --chown=${USER} entrypoint.sh ./

ENTRYPOINT [ "/usr/local/bin/dumb-init", "--" ]
CMD [ "./entrypoint.sh" ]
