# pyaction

[![pyaction - A Docker container with Python, git, and the GitHub CLI](https://actions.cicirello.org/images/pyaction640.png)](#pyaction)

Website for our GitHub Actions and tools for developing them: https://actions.cicirello.org/

## Summary

| __Docker Hub__ | [![Docker Image Version (latest by date)](https://img.shields.io/docker/v/cicirello/pyaction?label=Docker%20Hub&logo=docker)](https://hub.docker.com/r/cicirello/pyaction) [![Docker Pulls](https://img.shields.io/docker/pulls/cicirello/pyaction?logo=docker)](https://hub.docker.com/r/cicirello/pyaction) |
| :--- | :--- |
| __GitHub__ | [![GitHub Container Registry (latest by date)](https://ghcr-badge.egpl.dev/cicirello/pyaction/latest_tag?label=ghcr.io&color=%23007ec6&ignore=latest,3.12*,2*)](https://github.com/cicirello/pyaction/releases) |
| __Image Stats__ | [![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/cicirello/pyaction?logo=docker)](https://hub.docker.com/r/cicirello/pyaction) |
| __Build Status__ | [![build](https://github.com/cicirello/pyaction/workflows/build/badge.svg)](https://github.com/cicirello/pyaction/actions/workflows/docker-image.yml) |
| __License__ | [![License](https://img.shields.io/github/license/cicirello/pyaction)](LICENSE) |
| __Support__ | [![GitHub Sponsors](https://img.shields.io/badge/sponsor-30363D?logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/cicirello) [![Liberapay](https://img.shields.io/badge/Liberapay-F6C915?logo=liberapay&logoColor=black)](https://liberapay.com/cicirello) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?logo=ko-fi&logoColor=white)](https://ko-fi.com/cicirello) |

This Docker image is designed to support implementing Github Actions 
with Python. As of version 4.0.0., it starts with 
the [official python docker image](https://hub.docker.com/_/python) as the base,
which is a Debian OS. It specifically uses python:3-slim to keep the image size 
down for faster loading of Github Actions that use pyaction. On top of the 
base, we've installed [curl](https://curl.se/), 
[gpg](https://gnupg.org/), [git](https://git-scm.com/), and the 
[GitHub CLI](https://cli.github.com/). We added curl and gpg because they
are needed to install the GitHub CLI, and they may come in handy anyway 
(especially curl) when implementing a GitHub Action.

__Blog Post on DEV:__ [pyaction: A Docker container with Python, git, and the GitHub CLI](https://dev.to/cicirello/pyaction-a-docker-container-with-python-git-and-the-github-cli-930), posted on December 28, 2022. See a [list of additional blog posts](#blog-posts) later in this README.

## Multiplatform Image

__Version 4.0.0 and Newer__: pyaction supports the following 
platforms:
* linux/386
* linux/amd64
* linux/arm64
* linux/arm/v7
* linux/arm/v6

__Version 3.14.0 and Earlier__: earlier releases supported the
above as well as the following:
* linux/ppc64le
* linux/s390x 

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

See [CHANGELOG](https://github.com/cicirello/pyaction/blob/master/CHANGELOG.md) for details of
versions of Python, GitHub CLI, git, etc included in each pyaction release.


## Docker Tags and Versioning Scheme

We use [Semantic Versioning](https://semver.org/) for our tags.
[Semantic Versioning](https://semver.org/) uses version numbers 
of the form: MAJOR.MINOR.PATCH, where differences in 
MAJOR correspond to incompatible changes, differences in MINOR 
correspond to introduction of backwards compatible new functionality, 
and PATCH corresponds to backwards compatible bug fixes.

Each image pushed to Docker Hub and the Github Container Registry is tagged as follows:
* The tag `latest` indicates, well, the latest image.
* Tags of the form MAJOR.MINOR.PATCH (e.g., 4.0.0).
* Tags of the form MAJOR.MINOR (e.g., 4.0).
* Tags of the form MAJOR (e.g., 4).

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
