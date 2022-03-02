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
import platform
from datetime import datetime

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

def updateChangelogIfNecessary(versions) :
    """Compares current versions to old, and if any changed
    updates the Changelog. Returns whether or not any versions
    have changed.

    Keyword arguments:
    versions - Python map containing the versions extracted from
        the Docker image.
    """
    with open("versions.json", "r") as f :
        priorVersions = json.load(f)
    changed = versions != priorVersions
    if changed :
        updateChangelog(priorVersions, versions)
    return changed

def updateVersionsJSON(versions) :
    """Updates versions.json as necessary.

    Keyword arguments:
    versions - Python map containing the versions extracted from
        the Docker image.
    """
    with open("versions.json", "w") as f :
        json.dump(versions, f, sort_keys=True, indent=2)

def updateChangelog(priorVersions, versions) :
    """Updates the Unreleased section of the Changelog as necessary.

    Keyword arguments:
    priorVersions - Python map containing the versions as listed
        currently in the existing versions.json.
    versions - Python map containing the versions extracted from
        the Docker image.
    """
    with open("CHANGELOG.md", "r+") as f :
        contents = f.readlines()
        for i in range(len(contents)) :
            line = contents[i]
            if line.strip().startswith("## [Unreleased]") :
                unreleasedLineNumber = i
                break
        for i in range(unreleasedLineNumber + 1, len(contents)) :
            line = contents[i]
            if line.strip().startswith("### Changed") :
                changedStartsAt = i + 1
                break
        for i in range(changedStartsAt + 1, len(contents)) :
            line = contents[i]
            if line.strip().startswith("###") :
                changedEndsAt = i - 1
                break
        contents[unreleasedLineNumber] = "## [Unreleased] - {0}\n".format(datetime.today().strftime('%Y-%m-%d'))
        changedContents = findChanges(priorVersions, versions)
        updatedLogLines = set()
        for i in range(changedStartsAt, changedEndsAt) :
            if contents[i].startswith("* Bumped") :
                j = contents[i].find(" to ")
                if j > 0 :
                    checkThis = contents[i][:j+3]
                    for k, toolLine in enumerate(changedContents) :
                        if toolLine.startswith(checkThis) :
                            contents[i] = toolLine
                            updatedLogLines.add(k)
                            break
        changedContents = [ toolLine for k, toolLine in enumerate(changedContents) if k not in updatedLogLines]
        if len(changedContents) > 0 :
            contents[changedStartsAt:changedStartsAt] = changedContents
        f.seek(0)
        f.truncate()
        f.writelines(contents)

def findChanges(priorVersions, versions) :
    """Determines which tools have new versions.

    Keyword arguments:
    priorVersions - Python map containing the versions as listed
        currently in the existing versions.json.
    versions - Python map containing the versions extracted from
        the Docker image.
    """
    template = "* Bumped {0} to {1}.\n"
    changes = []
    if priorVersions["python"] != versions["python"] :
        changes.append(template.format("Python", versions["python"]))
    if priorVersions["gh"] != versions["gh"] :
        changes.append(template.format("GitHub CLI", versions["gh"]))
    if priorVersions["git"] != versions["git"] :
        changes.append(template.format("git", versions["git"]))
    if priorVersions["curl"] != versions["curl"] :
        changes.append(template.format("curl", versions["curl"]))
    if priorVersions["gpg"] != versions["gpg"] :
        changes.append(template.format("gpg", versions["gpg"]))
    return changes

if __name__ == "__main__" :
    gh, code = executeCommand(["gh", "--version"])
    gh = parse_gh_version(gh)
    git, code = executeCommand(["git", "--version"])
    git = parse_git_version(git)
    curl, code = executeCommand(["curl", "-V"])
    curl = parse_curl_version(curl)
    gpg, code = executeCommand(["gpg", "--version"])
    gpg = parse_gpg_version(gpg)
    print("gh version:", gh)
    print("git version:", git)
    print("curl version:", curl)
    print("gpg version:", gpg)
    print("python version", platform.python_version())
    versions = {
        "gh" : gh,
        "git" : git,
        "curl" : curl,
        "gpg" : gpg,
        "python" : platform.python_version()
    }
    if updateChangelogIfNecessary(versions) :
        updateVersionsJSON(versions)
