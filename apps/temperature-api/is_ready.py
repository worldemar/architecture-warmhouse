from http.client import HTTPConnection
import json
import sys

if __name__ == '__main__':
    conn = HTTPConnection(sys.argv[1], int(sys.argv[2]))
    conn.request("GET", "/health")
    resp = conn.getresponse()
    resp = resp.read().decode()
    assert json.loads(resp)['status'] == 'ok', resp + ' != {"status":"ok"}'
    print(resp)