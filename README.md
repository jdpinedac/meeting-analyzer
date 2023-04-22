# meeting-analyzer

This project is a Python-based software tool that allows users to transcribe audio to text and extract relevant information using the Whisper and ChatGPT APIs from OpenAI. The software is designed to be highly efficient and can leverage NVIDIA co-processors to accelerate processing times. Additionally, it contains a development container that can be used to easily set up the development environment.

## Requirements

- Python 3.x
- NVIDIA GPU with CUDA support
- NVIDIA cuDNN library
- Whisper API key
- ChatGPT API key
- Docker (if using development container)
- Docker version >= 23.0.2
- docker-compose-plugin version >= 2.17.2-1~ubuntu.22.04~jammy
- Linux Kernel >= 5.4.0

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:

    ``` shell
    pip install -r requirements.txt
    ```

3. Set up your Whisper and ChatGPT API keys in the config.py file.
4. (Optional) If you have an NVIDIA GPU with CUDA support, you can enable acceleration by setting use_gpu=True in the config.py file.
5. Run the software using the following command:

## Development Container

This project contains a development container that can be used to easily set up the development environment. To use it, simply navigate to the .agnostic_devcontainer folder and run the following command:

``` shell
docker-compose up --build
```

If you are using VSCode, you can also use the development container by opening the repository with VSCode and reopening it as a devcontainer.

## Usage

Once the software is running, it will prompt you to provide the path to the audio file you wish to transcribe and analyze. Once the audio has been processed, the software will output a transcript of the audio along with any relevant information extracted using the ChatGPT API.

## Acknowledgements

This software was built using the following technologies:

- Whisper API from OpenAI [https://openai.com/](https://openai.com/)
- ChatGPT API from OpenAI [https://openai.com/](https://openai.com/)
- NVIDIA CUDA and cuDNN libraries [https://developer.nvidia.com/cuda-toolkit](https://developer.nvidia.com/cuda-toolkit), [https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

A containerized development environment inspired by Visual Studio Code devcontainers. It includes all the development tools used in Pyxis InfraAWS.

## Motivation

In our day to day we need to install dozens of applications, tools, libraries and software in general for each project we do, each of which may vary in versions and configurations between different projects which leads to create a complete mess in our operating system. For this type of problem Docker has been a fundamental tool to separate different environments in development, testing and production throughout the entire CI/CD cycle.

Particularly in the development environment we have established some strategies so that the configuration time of the tools for each project is minimal, in addition to having a complete, compact, updated and functional environment to be able to start developing our projects quickly. This is where [devcontainers](https://code.visualstudio.com/docs/remote/containers) appear, a Microsoft strategy through its text editor Visual Studio Code, which allows to have a container with the necessary development and testing tools to start implementing any project in a matter of minutes.

This strategy is very striking because it not only saves us configuration time, but also allows us to have our base environment completely clean and without having compatibility problems between versions of our tools among other unwanted side effects at the level of our operating system.

Unfortunately Microsoft's devcontainers approach is only compatible with its VSCode text editor, since it uses its own docker images, with its own configurations and also uses internally the editor's own configuration mechanisms, such is the case of the .devcontainer/devcontainer.json and .devcontainer/Dockerfile files that show the high coupling that these files have with Microsoft's editor.

This is why this project tries to solve the problem by making available a template with an agnostic development environment, where following the best development practices the tools that we use on a daily basis and that we might need in an Infrastructure as Code or Configuration as Code development project are installed, including linters, debuggers, among other tools such as text editors. The project includes both the agnostic development environment and the equivalent using vscode devcontainers.

> Note that the `docker-compose` command is different from `docker compose` (the dash between the words), the former is a command, while the latter is a docker plugin. In our case we use the docker plugin, which you can install from the official Docker repositories.

### Tested on

- Linux Mint 20.3 on Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz 64 bits
- Fedora 37 on Intel(R) Core(TM) i7-10750H (12) @ 5.000GHz 64 bits

## Configuring the environment

Before using the containerized development environment, you should review the following files to verify that you have the desired settings:

- `.agnostic_devcontainer/.env` in which you will find an environment variable called DOCKER_USER, this variable contains the default user name within the container.
- `.agnostic_devcontainer/.env` `# Tool vars` and `# Terraform Tool vars` section, you can modify the specific versions of the main tools of the environment.

## Using the containerized development environment

The first thing to do is to copy the relevant files to your own project. For that you should execute the following command in your command terminal:

```bash
./cp2prj ${DIRECTORY}
cd ${DIRECTORY}
```

Where `${DIRECTORY}` is the target directory where your project is currently located. After that you can use the environment with the following command in the terminal:

```bash
cd .agnostic_devcontainer
PROJ_NAME=$(basename $(dirname $PWD)) DOCKER_USER=${USER} docker compose up --build -d

# or edit the .env file and execute

docker compose up --build -d
```

To verify that the container is running:

```bash
docker ps
```

To stop the development environment you must do it with this command:

```bash
docker compose stop
```

To view the logs of the development environment you must execute this command.

```bash
docker compose logs
```

To connect to the terminal of the development environment you should do it with this command:

```bash
docker exec -ti agnostic-devenv_cont bash
```

To clean the development environment you must do it with this command:

```bash
docker compose down; docker rmi NAMEOFCONTAINER
```

**_NOTE:_** If you want to install new software by hand or need privileges on the container just use the command `sudo` inside the container.

## Included Tools

- Python and PIP - Programming language with package manager
- Docker in Docker - Docker installed inside a docker container
- AWS CLI v. 2 - AWS Command Line Interface
- Hadolint - A linter for Dockerfiles
- Shellcheck - A linter for bash and other shell scripts
- Terraform - Infrastructure as code tool
- Terragrunt - Thin wrapper that provides extra tools for Terraform
- Terraform docs - Utility to generate documentation from Terraform modules
- TFLint - Terraform Linter
- TFSec - Static analysis security scanner for Terraform code
- TFTest - Python Test Helper for Terraform

## Contribute

When contributing, keep in mind that the idea is to have the agnostic devcontainer synchronized in terms of installed tools and applications.

## Troubleshooting

- **Authentication with Amazon:** If amazon authentication does not work, make sure that the `${HOME}/.aws` and `${HOME}/.ssh` directories have been mounted inside the container. One cause of this may be permissions issues on those two directories.
- **Repeated container name:** It is possible that a container with the same name has been instantiated in another project, you can delete the previous container with the command docker container prune or also the command docker container rm [containername].
- **New image is not updating:** If you are changing the [`Dockerfile`](Dockerfile) image or modifying the [`entrypoint.sh`](entrypoint.sh) please execute:

    ```bash
    docker compose down; docker rmi agnostic-devenv_dev_env:latest
    ```

## References

- [Developing inside a Container - Visual Studio Code](https://code.visualstudio.com/docs/remote/containers)
- [Getting Started with Dev Containers - Code with Engineering Playbook - Github Microsoft](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/devcontainers/)
- [Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- [Get started with Docker](https://www.docker.com/get-started/)
- [Get Started - How to get up to speed with localstack](https://docs.localstack.cloud/get-started/)
- [Docker ARG, ENV and .env - a Complete Guide](https://vsupalov.com/docker-arg-env-variable-guide/)
