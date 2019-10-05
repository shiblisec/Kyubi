## Kyubi

A tool to discover and exploit Nginx alias traversal misconfiguration, the tool can bruteforce the URL path recursively to find out hidden files and directories.

<p align="center"><img src="https://i.postimg.cc/NfvjVmJj/Capture.jpg" /></p>

## Installation

```
$ git clone https://github.com/shibli2700/Kyubi.git
$ sudo python3 setup.py install
```

## Options
```
usage: kyubi [-h] [-v] [-a] url

This tool checks nginx alias traversal misconfiguration.

positional arguments:
  url         URL of the target

optional arguments:
  -h, --help  show this help message and exit
  -v          increase verbosity
  -a          append segment in the end
  ```

## Usage

```
$ kyubi -v https://127.0.0.1/resources/images/users/profile/profile.png
```

## Future Addition

* Brute forcing with filenames and directories.
* Web Interface.
