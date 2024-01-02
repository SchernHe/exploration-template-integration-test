ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}

# The aAI VPN requires this certificate to be present
ENV AAI_CERT_PATH=/usr/local/share/ca-certificates/aai-root-ca.crt
COPY .devcontainer/aai-root-ca.crt ${AAI_CERT_PATH}
RUN update-ca-certificates


# Install additional tools and packages required for development
ARG PACKAGES_DEVTOOLS="git openssh-client sudo curl ca-certificates icu-devtools locales bash-completion man-db"
RUN apt-get update -qq \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y -qq install --no-install-recommends ${PACKAGES_DEVTOOLS} \
    && apt-get clean -y -qq && rm -rf /var/lib/apt/lists/*


# Install Git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y -qq install --no-install-recommends git-lfs \
    && apt-get clean -y -qq && rm -rf /var/lib/apt/lists/* \
    && git lfs install


# Create User
ARG USER_NAME=dev-user
ARG USER_UID=1000
ARG USER_GID=${USER_UID}
ENV HOME=/home/${USER_NAME}

# Give user passwordless sudo rights
RUN useradd -rm -s /bin/bash -G sudo -u ${USER_UID} ${USER_NAME} \
    && echo ${USER_NAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER_NAME} \
    && chmod 0440 /etc/sudoers.d/${USER_NAME}
# Set locale (unset locale can lead to errors during pre-commit)
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 && \
    . /etc/default/locale


USER ${USER_NAME}
WORKDIR ${HOME}

# Install poetry
ARG POETRY_VERSION=1.5.1 
RUN curl -sSL https://install.python-poetry.org | python3 - --version ${POETRY_VERSION}
RUN echo 'export PATH=${PATH}:${HOME}/.local/bin' >> ${HOME}/.bashrc
ENV PATH=${PATH}:${HOME}/.local/bin
