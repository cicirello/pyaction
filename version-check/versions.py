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

if __name__ == "__main__" :
    gh, code = executeCommand(["gh", "--version"])
    git, code = executeCommand(["git", "--version"])
    curl, code = executeCommand(["curl", "-V"])
    gpg, code = executeCommand(["gpg", "--version"])
    print("gh version:")
    print(gh)
    print("git version:")
    print(git)
    print("curl version:")
    print(curl)
    print("gpg version:")
    print(gpg)
