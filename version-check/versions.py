#
# Test for the pyaction docker image, validating versions of installed apps. 
# 
# Copyright (c) 2022 Vincent A Cicirello
# https://www.cicirello.org/
#
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import json
import subprocess

def executeCommand(arguments) :
    """Execute a subprocess and return result and exit code.

    Keyword arguments:
    arguments - The arguments for the command.
    """
    result = subprocess.run(
        arguments,
        stdout=subprocess.PIPE,
        universal_newlines=True
        )
    return result.stdout.strip(), result.returncode

def parse_gh_version(gh) :
    """Parses the version number for gh.

    Keyword arguments:
    gh - The result of querying the version from gh.
    """
    return gh.split()[2]

def parse_git_version(git) :
    """Parses the version number for git.

    Keyword arguments:
    git - The result of querying the version from git.
    """
    return git.split()[2]

def parse_curl_version(curl) :
    """Parses the version number for curl.

    Keyword arguments:
    curl - The result of querying the version from curl.
    """
    return curl.split()[1]

def parse_gpg_version(gpg) :
    """Parses the version number for gpg.

    Keyword arguments:
    gpg - The result of querying the version from gpg.
    """
    return gpg.split()[2]

if __name__ == "__main__" :
    gh, code = executeCommand(["gh", "--version"])
    gh = parse_gh_version(gh)
    git, code = executeCommand(["git", "--version"])
    git = parse_git_version(git)
    curl, code = executeCommand(["curl", "-V"])
    curl = parse_curl_version(curl)
    gpg, code = executeCommand(["gpg", "--version"])
    gpg = parse_gpg_version(gpg)
    print("gh version:")
    print(gh)
    print("git version:")
    print(git)
    print("curl version:")
    print(curl)
    print("gpg version:")
    print(gpg)
