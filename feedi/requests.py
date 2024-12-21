import functools

import requests

USER_AGENT = "readio/0.1.0 (+https://github.com/notfaye2002)"
TIMEOUT_SECONDS = 5
TIMEOUT_SLOWER = 10

requests = requests.Session()
requests.headers.update({"User-Agent": USER_AGENT})

# always use a default timeout
requests.get = functools.partial(requests.get, timeout=TIMEOUT_SECONDS)
