# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2023-02-09

### Added
  
### Changed
* Bumped Python to 3.11.2.
* Bumped GitHub CLI to 2.23.0.

### Deprecated

### Removed

### Fixed

### CI/CD


## [4.15.0] - 2023-01-26

### Changed
* Bumped GitHub CLI to 2.22.0.


## [4.14.1] - 2023-01-04
  
### Changed
* Bumped GitHub CLI to 2.21.2.


## [4.14.0] - 2022-12-28
  
### Changed
* Bumped GitHub CLI to 2.21.1.


## [4.13.1] - 2022-12-10

### Changed
* Bumped Python to 3.11.1.
* Bumped GitHub CLI to 2.20.2.


## [4.13.0] - 2022-11-09

### Changed
* Bumped GitHub CLI to 2.20.0.


## [4.12.0] - 2022-10-25

### Changed
* Bumped Python to 3.11.0.


## [4.11.1] - 2022-10-21

### Changed
* Bumped GitHub CLI to 2.18.1.


## [4.11.0] - 2022-10-19

### Changed
* Bumped GitHub CLI to 2.18.0.


## [4.10.0] - 2022-10-05

### Changed
* Bumped GitHub CLI to 2.17.0.


## [4.9.0] - 2022-09-22
  
### Changed
* Bumped GitHub CLI to 2.16.0.


## [4.8.1] - 2022-09-08
  
### Changed
* Bumped Python to 3.10.7.


## [4.8.0] - 2022-09-07

### Changed
* Bumped GitHub CLI to 2.15.0.


## [4.7.1] - 2022-08-15

### Changed
* Bumped Python to 3.10.6.
* Bumped GitHub CLI to 2.14.4.


## [4.7.0] - 2022-07-24
  
### Changed
* Bumped GitHub CLI to 2.14.2.


## [4.6.0] - 2022-06-23

### Changed
* Bumped GitHub CLI to 2.13.0.


## [4.5.0] - 2022-06-09
  
### Changed
* Bumped Python to 3.10.5.
* Bumped GitHub CLI to 2.12.1.


## [4.4.0] - 2022-05-06
  
### Changed
* Bumped GitHub CLI to 2.9.0.


## [4.3.1] - 2022-03-29

### Changed
* Bumped Python to 3.10.4.


## [4.3.0] - 2022-03-17

### Changed
* Bumped Python to 3.10.3.
* Bumped GitHub CLI to 2.6.0.


## [4.2.0] - 2022-02-20

### Changed
* Bumped GitHub CLI to 2.5.1.


## [4.1.0] - 2022-01-24

Note that 4.1.0 is the same as 4.0.0 in what is included in the image. The purpose
of this release includes changing the tag used for the base docker image to specify
a specific release of python, in this case `3.10.2-slim`, whereas previously it was
specified more generally as `3-slim`. We have also changed our CI/CD related workflows
to include a script that monitors daily for available updates to the GitHub CLI, git, curl, and
gpg. From this point onward, we are taking a more deliberative approach to pushing new
images, such as when one or more of these have new versions available, and we will bump
the version number of pyaction when this occurs.

The versions included in pyaction 4.1.0 are as follows:
* Python 3.10.2 (a python 3.10.2-slim base docker image)
* GitHub CLI 2.4.0
* git 2.30.2
* curl 7.74.0
* gpg 2.2.27
  
### Changed
* Base Docker image is still a Python 3 Slim, but it is now fixed to
  a specific version, in this case 3.10.2-slim.
* Eliminated the twice-monthly automated builds to current tags to enable
  a more deliberative approach to maintaining versions of packages in the
  image.
* New release policy is to release a new image when the versions of one or more
  of python, git, gh, curl, or gpg are bumped.

### CI/CD
* Now performs daily builds, which includes using the image to run a simple Python program
  to validate the various package installations. This test program simply outputs the versions
  of git, gh, curl, gpg, and python. It also generates a json file with this data within the 
  repo to enable detecting updated versions of these packages. Dependabot handles updating python
  version, but not able to detect what versions the base image's package manager will install.
  If any versions change, this workflow will generate a PR for this new versions.json file,
  alerting us to the newly available versions.


## [4.0.0] - 2021-07-03

### Upgrading
* Potentially breaking changes are included in this release.
* Read notes below carefully, and test your application before
  upgrading.

### Added
* Added the GitHub CLI (gh).
* Added curl (necessary to install gh).
* Added gpg (necessary to install gh).

### Changed
* BREAKING CHANGE: Base image is now python:3-slim rather than alpine.
  * This new base image was necessary in order to be able to install gh.
  * This new base image is based on Debian.
* CI/CD process now performs twice monthly automated builds/pushes to ensure 
  picking up any non-breaking bug fixes / security updates from base OS 
  distro, Python, etc. This is accomplished by using the python:3-slim
  tag when pulling the base image, rather than a more specific version of
  Python.
* Version numbering scheme changed.
  * It is still SemVer, but no longer based on SemVer of base image.

### Removed
* No longer supports the following architectures: linux/ppc64le, linux/s390x, linux/arm/v6.
  * These architectures are not supported by gh.


## [3.14.0] - 2021-06-16

### Added
* This ChangeLog. Note that versions prior to this one that the pyaction
  version corresponds to the Alpine version.

### Changed
* Bumped base docker image to Alpine 3.14.0.
