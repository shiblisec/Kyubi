## Kyubi

A tool to discover and exploit Nginx alias traversal misconfiguration, the tool can bruteforce the URL path recursively to find out hidden files and directories.

## Installation

```
git clone https://github.com/shibli2700/Kyubi.git
python3 setup.py install
```

## Options
```
usage: kyubi [-h] [-v] [-d WLIST] [-a] url

This is a nginx traversal tool

positional arguments:
  url         URL of the target

optional arguments:
  -h, --help  show this help message and exit
  -v          increase verbosity
  -d WLIST    wordlist path
  -a          append segment in the end
  ```

## Usage

```
kyubi -a https://127.0.0.1/resources/images/users/profile/profile.png
```

<p align="center"><img src="https://i.postimg.cc/NfvjVmJj/Capture.jpg" /></p>
