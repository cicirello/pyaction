# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2022-01-24

### Added
  
### Changed

### Deprecated

### Removed

### Fixed

### CI/CD


## [4.1.0] - 2022-01-24
  
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
