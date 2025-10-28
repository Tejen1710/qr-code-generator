# QR Code Generator — Dockerized

A minimal Python application that generates a PNG QR code for a provided URL. The app is packaged as a secure, non-root Docker image and published to DockerHub.

## Features
- Non-root user inside the container for security
- Slim Python base image for smaller footprint
- Volume mount to persist generated QR images
- Runtime argument override for `--url`

## Build (local)
```bash
docker build -t qr-code-generator-app .
```
## Run (local)
Create a folder for outputs and run:
```
New-Item -ItemType Directory -Force -Path "$PWD\qr_codes" | Out-Null
docker run -d --name qr-generator `
  -v "$PWD\qr_codes:/app/qr_codes" `
  qr-code-generator-app --url https://github.com/tejen1710

docker logs qr-generator
``` 

## DockerHub Image
https://hub.docker.com/r/tejenthakkar1710/qr-code-generator-app

Pull and run directly:
```
docker pull YOUR_DH_USERNAME/qr-code-generator-app:latest
docker run --rm -v "$PWD/qr_codes:/app/qr_codes" YOUR_DH_USERNAME/qr-code-generator-app \
  --url https://www.njit.edu
```

## GitHub Actions (CI)

This repository includes a workflow that builds and pushes the image to DockerHub on pushes to main.

    Workflow file: .github/workflows/docker-ci.yml

    Required repo secrets:

    DOCKERHUB_USERNAME

    DOCKERHUB_TOKEN (DockerHub access token)

    IMAGE_NAME = qr-code-generator-app

## Tech Stack
    Python 3.12 (slim-bullseye)

    Libraries: qrcode, Pillow

    Docker, DockerHub, GitHub Actions

## Screenshots (for grading)
    Container logs showing QR saved to ...
    GitHub Actions successful run

## License
Educational assignment.

