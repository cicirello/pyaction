# pyaction

[![pyaction - A Docker container with Python, git, and the GitHub CLI](https://actions.cicirello.org/images/pyaction640.png)](#pyaction)

Website for our GitHub Actions and tools for developing them: https://actions.cicirello.org/

## Summary

| __Docker Hub__ | [![Docker Image Version (latest by date)](https://img.shields.io/docker/v/cicirello/pyaction?label=Docker%20Hub&logo=docker)](https://hub.docker.com/r/cicirello/pyaction) [![Docker Pulls](https://img.shields.io/docker/pulls/cicirello/pyaction?logo=docker)](https://hub.docker.com/r/cicirello/pyaction) |
| :--- | :--- |
| __GitHub__ | [![GitHub Container Registry (latest by date)](https://img.shields.io/docker/v/cicirello/pyaction?label=ghcr.io&logo=GitHub)](https://github.com/cicirello/pyaction/pkgs/container/pyaction) |
| __Image Stats__ | [![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/cicirello/pyaction?logo=docker)](https://hub.docker.com/r/cicirello/pyaction) |
| __Build Status__ | [![build](https://github.com/cicirello/pyaction/workflows/build/badge.svg)](https://github.com/cicirello/pyaction/actions/workflows/docker-image.yml) |
| __License__ | [![License](https://img.shields.io/github/license/cicirello/pyaction)](LICENSE) |
| __Support__ | [![GitHub Sponsors](https://img.shields.io/badge/sponsor-30363D?logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/cicirello) [![Liberapay](https://img.shields.io/badge/Liberapay-F6C915?logo=liberapay&logoColor=black)](https://liberapay.com/cicirello) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?logo=ko-fi&logoColor=white)](https://ko-fi.com/cicirello) |

This Docker image is designed to support implementing Github Actions 
with Python. It starts with the [official python docker image](https://hub.docker.com/_/python) 
as the base, which is a Debian OS. It specifically uses python:3-slim to keep the image size 
down for faster loading of Github Actions that use pyaction. On top of the 
base, we've installed [curl](https://curl.se/), 
[gpg](https://gnupg.org/), [git](https://git-scm.com/), and the 
[GitHub CLI](https://cli.github.com/). We added curl and gpg because they
are needed to install the GitHub CLI, and they may come in handy anyway 
(especially curl) when implementing a GitHub Action.

__Blog Posts:__ See a [list of blog posts about pyaction](#blog-posts) later in this README.

## Multiplatform Image

pyaction supports the following platforms:
* linux/386
* linux/amd64
* linux/arm64
* linux/arm/v7
* linux/arm/v6

## Source Repository and Builds

The [source repository](https://github.com/cicirello/pyaction) is 
maintained on GitHub. The images are built on Github and pushed 
to [Docker Hub](https://hub.docker.com/r/cicirello/pyaction), as 
well as the 
[Github Container Registry](https://github.com/cicirello?ecosystem=container&tab=packages) 
using Github Actions.

Our daily automated CI/CD processes monitor for updates to the Python slim Docker image, the GitHub 
CLI, etc. Upon detecting such updates, we release an update of pyaction sometimes as 
early as same day, but possibly a few days later.

See [versions.json](https://github.com/cicirello/pyaction/blob/master/versions.json) for details of
versions of Python, GitHub CLI, git, etc included in the latest build.


## Docker Tags and Versioning Scheme

For the current version of Python (e.g., 3.13.5) and current version 
of GitHub CLI (e.g., 2.75.0), all of the following tags are available and equivalent:
`latest`, `3.13.5`, `3.13`, `3.13.5-gh-2.75.0`, `3.13.5-gh-2.75`, `3.13.5-gh-2`, 
`3.13-gh-2.75.0`, `3.13-gh-2.75`, `3.13-gh-2`.

For prior versions of Python (3.8, 3.9, 3.10, 3.11, 3.12) and current version of 
GitHub CLI (2.75.0), all of the following tags are available and equivalent: 
`3.12`, `3.12-gh-2.75.0`, `3.12-gh-2.75`, `3.12-gh-2`.

This tag scheme began with version 2.75.0 of the GitHub CLI. We don't support pyaction
images with earlier versions of the GitHub CLI.

This tag scheme began with Python 3.13.5. Python patch level tags are not available for
pyaction prior to Python 3.13.5.


## Installation and Usage

The pre-built image is hosted on both Docker Hub and the Github 
Container Registry. You can use it in the following ways.

### Docker Pull Command

Pull the latest image from Docker Hub with the following (replace `latest` with 
a specific version number if you prefer):

```Shell
docker pull cicirello/pyaction:latest
```

Pull from the Github Container Registry with:

```Shell
docker pull ghcr.io/cicirello/pyaction:latest
```


### Use as a base image in a Dockerfile

Use as a base image in a Dockerfile (replace `latest` with 
a specific version number if you prefer):

```Dockerfile
FROM cicirello/pyaction:latest

# The rest of your Dockerfile would go here.
```

Or you can use as a base image (via the Github Container Registry) with:

```Dockerfile
FROM ghcr.io/cicirello/pyaction:latest

# The rest of your Dockerfile would go here.
```

## Blog Posts

Here are a few blog posts about the pyaction container listed in reverse chronological order:
* [pyaction: Python and the GitHub CLI in a Docker Container](https://dev.to/cicirello/pyaction-python-and-the-github-cli-in-a-docker-container-3682), posted on August 14, 2025.
* [pyaction pulled 4 million times and counting from the GitHub Container Registry](https://dev.to/cicirello/pyaction-pulled-4-million-times-and-counting-from-the-github-container-registry-47i3), posted on May 31, 2024.
* [Celebrating over 2 million pulls of pyaction from the GitHub Container Registry](https://dev.to/cicirello/celebrating-over-2-million-pulls-of-pyaction-from-the-github-container-registry-20hb), posted on September 2, 2023.
* [pyaction: Over 1 million pulls from the GitHub Container Registry](https://dev.to/cicirello/pyaction-over-1-million-pulls-from-the-github-container-registry-29ag), posted on February 16, 2023.
* [pyaction: A Docker container with Python, git, and the GitHub CLI](https://dev.to/cicirello/pyaction-a-docker-container-with-python-git-and-the-github-cli-930), posted on December 28, 2022.

## License

### Source Code License
The source code, including the Dockerfile and anything
else within the [Github repository for pyaction](https://github.com/cicirello/pyaction), 
is licensed under the
[MIT License](https://github.com/cicirello/pyaction/blob/master/LICENSE).

### Image Licenses
As with all pre-built Docker images, the image itself (once built, or obtained from
Docker Hub or the Github Container Registry) contains software that is covered by a
variety of licenses. See the license information for the 
[python docker image](https://hub.docker.com/_/python),
the [license for git](https://git-scm.com/), 
the [GitHub CLI](https://github.com/cli/cli/blob/trunk/LICENSE),
and the [license for Python](https://docs.python.org/3/license.html).  

If you build and distribute an image containing your software, 
using pyaction as the base image, it
is your responsibility to follow the licenses of all of the
software contained within the image.  
