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

## Development Container

This project contains a development container that can be used to easily set up the development environment.

### Configuring the environment

Before using the containerized development environment, you should review the following files to verify that you have the desired settings:

- `.agnostic_devcontainer/.env` in which you will find an environment variable called DOCKER_USER, this variable contains the default user name within the container.
- `.agnostic_devcontainer/.env` `# Tool vars` section, you can modify the specific versions of the main tools of the environment.

### Using the Agnostic Devcontainer

To use it, simply navigate to the .agnostic_devcontainer folder and run the following command:

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

### Using the VSCode Devcontainer

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

## References

- [OpenAI Documentation](https://platform.openai.com/docs/introduction )
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/introduction)
- [Developing inside a Container - Visual Studio Code](https://code.visualstudio.com/docs/remote/containers)
- [Getting Started with Dev Containers - Code with Engineering Playbook - Github Microsoft](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/devcontainers/)
- [Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- [Get started with Docker](https://www.docker.com/get-started/)
- [Get Started - How to get up to speed with localstack](https://docs.localstack.cloud/get-started/)
- [Docker ARG, ENV and .env - a Complete Guide](https://vsupalov.com/docker-arg-env-variable-guide/)
