# Reflection

## What changed when containerizing
Before containerization, the QR Code Generator application depended on my local Python installation, environment variables, and library versions. After packaging the application into a Docker image, everything required to run the program is included inside the image itself. This provides a consistent and reproducible environment that works the same across different operating systems and machines. Docker ensures that anyone can run the application without installing dependencies or dealing with compatibility issues.

## Security considerations
I implemented security best practices in the Dockerfile by using a lightweight slim-bullseye base image and creating a non-root user to execute the application. This minimizes vulnerabilities and limits the impact if there is a security breach inside the container. The restricted permissions and reduced attack surface help protect both the host system and the containerized application.

## Challenges and fixes
The primary challenge I faced was authenticating DockerHub from GitHub Actions. Initially, the workflow failed due to missing credentials. I successfully resolved this by generating a DockerHub access token and configuring GitHub repository secrets correctly. I also learned how volume mounting behaves differently on Windows and adjusted the command by using an absolute path with quotes.

## CI/CD value
The GitHub Actions workflow now automatically builds and pushes updated Docker images to DockerHub, ensuring reliable deployment and version control.

## Next steps
Future improvements include adding automated tests, tagging images with version numbers, and enhancing logging.
