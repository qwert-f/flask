from werkzeug.wrappers import Response, Request
from werkzeug.serving import run_simple


@Request.application
def test01(request):
    return Response('hello Flask!')


if __name__ == '__main__':
    run_simple('localhost', 1314, test01)
