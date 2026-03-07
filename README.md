# Advent of Code solutions

[![Python][python-shield]][python-url]
[![pre-commit][precommit-shield]][precommit-url]
[![PEP8][pep8-shield]][pep8-url]
[![MIT License][license-shield]][license-file]

## Overview

This repository contains my solutions to the annual [Advent of Code][AoC] puzzles.

At the moment I have 383 (or more, if I forget to update it here) stars from the events since 2015.
I will continue to populate this repository when I find bits of time to clean the solutions to my current standards.

Hopefully, my solutions will help in debugging or learning.
The licence allows copying the solutions as is.
Doing so, just to get the puzzle answer seems, in my humble opinion, pointless or even counterproductive.
So please, if you do take my whole solutions, try to look into the code and see how it works.

Of note is also my custom [utility][util-file], that loads the puzzle inputs directly from the web.
The file is added as a symlink to each year's subdirectory to allow smooth imports when run in various IDEs/terminals.
See the [Getting Started section](#getting-started) on how to set it up to access your own inputs. Please be mindful to not spam the requests to the AoC server.
The utility uses memoisation, so calling the `getInput` function multiple times in one run is ok, but rerunning the code many times in a short time window is less so.

## Getting Started

#### 1. Find your session cookie

Log in at the [Advent of Code website][AoC-login], if you are not already logged in, and find your session cookie.
You will likely find it in the inspect mode of your browser (`Inspect > Application > Storage > Cookies`), but it may vary between versions and browsers.
A quick [web search][google-cookie] will surely help you.


#### 2. Create `sessionCookie.txt`

In the root directory of the project, create a `sessionCookie.txt` file

```bash
cp sessionCookie.example.txt sessionCookie.txt
```

and replace the contents with your session cookie

##### NOTE: You will need to update this every time you log in after a log out.

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

##### NOTE: It is highly recommended to use a virtual environment. It is, however, also true that the libraries used are very versatile and widely used and you may already have them installed.


#### 4. Run the individual solutions

Use your IDE or terminal, and select the desired puzzle date to run

```bash
python "2025/01.py"
```


## License

Distributed under the MIT License. See [`LICENSE`][license-file] for more information.


<!-- URLs -->
[python-shield]: https://img.shields.io/badge/python-3.11-blue?logo=python
[python-url]: https://www.python.org/downloads/release/python-31114/
[license-shield]: https://img.shields.io/badge/license-MIT-blue
[license-file]: LICENSE
[precommit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
[precommit-url]: https://pre-commit.com/
[pep8-url]: https://www.python.org/dev/peps/pep-0008/
[pep8-shield]: https://img.shields.io/badge/code_style-pep8-blue
[google-cookie]: https://www.google.com/search?q=where+to+find+session+cookies
[AoC]: https://adventofcode.com
[AoC-login]: https://adventofcode.com/auth/login
[util-file]: utils.py
