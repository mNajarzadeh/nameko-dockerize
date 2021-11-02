import enum
import json


server_url = "https://localhost"
server_port = "/"
frontend_url = "http://localhost"
frontend_port = ":3000/"
secret= "dSgVkXp2s5v8yB?E(H+MbQeThWmZq"
class ResponseStatus(enum.Enum):
   success = 1
   fail    = 2
   authen  = 3
   unknown = 4


def response_standard(data=[],status=ResponseStatus.success ):
    return json.dumps({'status': status.name, 'data' : data })
def response_standard_gallery(data=[],status=ResponseStatus.success ):
    return json.dumps({'statusCode':200, 'result' : data })
