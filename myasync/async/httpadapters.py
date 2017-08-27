import re
import json

class HttpResponse:
    """
	This is http response object creator, please pass only valid
    reponse from socket.
    """
    def __init__(self, content):
        self._content = content.decode("utf8")
        self._headers_format()
    
    def _headers_format(self):
        header, body = re.split(r'\r\n\r\n', 
		                 self._content, 
				 maxsplit=1)
        self.content = body
        status, header = re.split(r'\r\n',
		                  header,
				  maxsplit=1)
        self.status_code = re.findall(r'\d{3}', status)[0]
        header = re.split(r'\r\n',
		            header)
        header_tuple = [re.split(r':', item, maxsplit=1) for item in header]
        self.headers = dict(header_tuple)
    
    def __repr__(self):
        return '<HttpResponse [{}]>'.format(self.status_code)

    def json(self):
        return json.loads(self.content)
