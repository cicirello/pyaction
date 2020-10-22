# pyaction
A base Docker image for Github Actions implemented in Python

[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/cicirello/pyaction?label=Docker%20Hub&logo=docker)](https://hub.docker.com/r/cicirello/pyaction)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/cicirello/pyaction?logo=docker)](https://hub.docker.com/r/cicirello/pyaction)
[![Docker Pulls](https://img.shields.io/docker/pulls/cicirello/pyaction?logo=docker)](https://hub.docker.com/r/cicirello/pyaction)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/cicirello/pyaction?logo=github)](https://github.com/cicirello/pyaction/releases)
[![build](https://github.com/cicirello/pyaction/workflows/build/badge.svg)](https://github.com/cicirello/pyaction/actions?query=workflow%3Abuild)
[![GitHub](https://img.shields.io/github/license/cicirello/pyaction)](https://github.com/cicirello/pyaction/blob/master/LICENSE)

## Summary

This Docker image is designed to support implementing Github Actions 
with Python. It uses Alpine Linux as a base to keep the image relatively
small for faster loading of the Github Action. It then adds git 
and Python 3. By using a prebuilt image, it prevents the Github Action
from requiring an installation of python each time the action runs. It
is not limited to use with Github Actions, so other use-cases where you
need git and python are applicable.

## Multiplatform Image

pyaction has the following platforms available:
* linux/386
* linux/amd64
* linux/arm/v6
* linux/arm/v7
* linux/arm64
* linux/ppc64le
* linux/s390x 

## Source Repository and Builds

The [source repository](https://github.com/cicirello/pyaction) is maintained on GitHub.  The images are built on Github and pushed to [Docker Hub](https://hub.docker.com/r/cicirello/pyaction), as well as the [Github Container Registry](https://github.com/cicirello?ecosystem=container&tab=packages) using Github Actions.

## Docker Tags and Versioning Scheme

Each image pushed to Docker Hub and the Github Container Registry is tagged as follows:
* The tag `latest` indicates, well, the latest image.
* __Beginning with version 3.12.1__: tags of the form MAJOR.MINOR.PATCH (such as 3.12.1) indicate the SemVer of the __Alpine__ image used as the base.
* __Prior to version 3.12.1__: tags of the form MAJOR.MINOR.PATCH (such as 1.0.0) indicate the SemVer of the image, where the base image was Alpine 3.12.0.

[Semantic Versioning](https://semver.org/) uses version numbers 
of the form: MAJOR.MINOR.PATCH, where differences in 
MAJOR correspond to incompatible changes, differences in MINOR 
correspond to introduction of backwards compatible new functionality, 
and PATCH corresponds to backwards compatible bug fixes.


## Installation and Usage

The pre-built image is hosted on both Docker Hub and the Github Container Registry. You can use it in the following ways.

### Docker Pull Command

Pull the latest image from Docker Hub with the following (replace `latest` with 
a specific version number if you prefer):

```
docker pull cicirello/pyaction:latest
```

Pull from the Github Container Registry with:

```
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


## License
### Source Code License
The source code, including the Dockerfile and anything
else within the [Github repository for pyaction](https://github.com/cicirello/pyaction), is licensed under the
[MIT License](https://github.com/cicirello/pyaction/blob/master/LICENSE).

### Image Licenses
As with all pre-built Docker images, the image itself (once built, or obtained from
Docker Hub or the Github Container Registry) contains software that is covered by a
variety of licenses. Since the base image is Alpine, this would include
the [licenses of the components of Alpine](https://pkgs.alpinelinux.org/),
the [license for git](https://git-scm.com/), 
and the [licenses for Python](https://docs.python.org/3/license.html).  

If you build and distribute an image containing your software, 
using pyaction as the base image, it
is your responsibility to follow the licenses of all of the
software contained within the image.  





