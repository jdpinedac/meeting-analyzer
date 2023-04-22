# Agnostic Development Environment
# Depends on docker-compose.yml and .env files

ARG VARIANT
ARG OS_IMG
FROM ${OS_IMG}:${VARIANT}
LABEL mantainer="juan.david.pineda@gmail.com"

ARG PROJ_NAME
ARG WORKDIR
WORKDIR /${WORKDIR}/${PROJ_NAME}

# User configuration
ARG DOCKER_USER
ARG USER_ID
ARG GROUP_ID
ARG BIN_DIR

# Tools versions
ARG PIP_VERSION
ARG HADOLINT_VERSION
ARG SHELLCHECK_VERSION
ARG SHFMT_VERSION

# Install apt dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    wget=1.21-1+deb11u1 \
    unzip=6.0-26+deb11u1 \
    xz-utils=5.2.5-2.1~deb11u1 \
    sudo=1.9.5p2-3+deb11u1 \
    jq=1.6-2.1 \
    ffmpeg=7:4.3.5-0+deb11u1 \
    ca-certificates=20210119 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install python dependencies with pip
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 install --no-cache-dir --upgrade pip==${PIP_VERSION} \
    && pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Install DooD
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Create dev user
RUN echo "${DOCKER_USER} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${DOCKER_USER} \
    && if id ${DOCKER_USER} 2>/dev/null; then userdel -f ${DOCKER_USER}; fi \
    && if getent group ${DOCKER_USER}; then groupdel ${DOCKER_USER}; fi \
    && groupadd -g ${GROUP_ID} ${DOCKER_USER} \
    && useradd -l -u ${USER_ID} -g ${DOCKER_USER} -s /bin/bash ${DOCKER_USER} \
    && install -d -m 0755 -o ${DOCKER_USER} -g ${DOCKER_USER} /home/${DOCKER_USER} \
    && usermod -a -G sudo ${DOCKER_USER}

# Other tools like ansible, localstack, awslocal, tflocal and others are pip3 dependencies.
# Please consider change the version on requirements.txt

# Install dev tools and aws cli
RUN wget --progress=dot:mega https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -O awscliv2.zip \
    && unzip awscliv2.zip \
    && ./aws/install \
    && echo "complete -C /usr/local/bin/aws_completer aws" >> ~/.bashrc \
    && rm -rf aws/ awscliv2.zip \
    && wget --progress=dot:mega https://github.com/hadolint/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint-Linux-x86_64 \
    -O ${BIN_DIR}/hadolint \
    && chmod 755 ${BIN_DIR}/hadolint \
    && wget --progress=dot:mega https://github.com/mvdan/sh/releases/download/v${SHFMT_VERSION}/shfmt_v${SHFMT_VERSION}_linux_amd64 \
    -O "${BIN_DIR}"/shfmt \
    && chmod 755 "${BIN_DIR}"/shfmt \
    && wget --progress=dot:mega https://github.com/koalaman/shellcheck/releases/download/v${SHELLCHECK_VERSION}/shellcheck-v${SHELLCHECK_VERSION}.linux.x86_64.tar.xz \
    && tar xvf shellcheck-v${SHELLCHECK_VERSION}.linux.x86_64.tar.xz \
    && cp shellcheck-v${SHELLCHECK_VERSION}/shellcheck ${BIN_DIR}/ \
    && chmod 755 ${BIN_DIR}/shellcheck \
    && rm -rf shellcheck-v${SHELLCHECK_VERSION}.linux.x86_64.tar.xz shellcheck-v${SHELLCHECK_VERSION}

# Change to dev user
USER ${DOCKER_USER}
COPY .bashrc /home/${DOCKER_USER}/.bashrc
ENTRYPOINT [ ".agnostic_devcontainer/entrypoint.sh" ]

CMD [ "sleep", "infinity" ]
