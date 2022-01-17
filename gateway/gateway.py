# gateway.py
import json
from nameko.web.handlers import http, HttpRequestHandler
from nameko.rpc import  RpcProxy
import logging
from nameko.events import EventDispatcher, event_handler
from api_call import response_standard,ResponseStatus
import traceback
class CorsHttpRequestHandler(HttpRequestHandler):
    def handle_request(self, request):
        self.request = request
        if request.method == 'OPTIONS':
            return self.response_from_result(result='')
        return super(CorsHttpRequestHandler, self).handle_request(request)

    def response_from_result(self, *args, **kwargs):
        response = super(CorsHttpRequestHandler, self).response_from_result(*args, **kwargs)
        response.headers.add("Access-Control-Allow-Headers",
                             self.request.headers.get("Access-Control-Request-Headers"))
        response.headers.add("Access-Control-Allow-Credentials", "true")
        response.headers.add("Access-Control-Allow-Methods", "*")
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

cors_http = CorsHttpRequestHandler.decorator

class HttpService:
    name = "gateway-service"
    dispatch = EventDispatcher()
    category_service = RpcProxy("category_service")

    def get_header(self,request):
        action = (request.url).split('/')[3]
        action = action.split('?')[0]
        sss= {'token':request.headers.get('Authorization', None),'action':action,'form':request.form,'args':request.args}
        logging.info(sss)
        return sss

    @cors_http('GET,OPTIONS', '/list')
    def list(self, request):
        act = self.user_service.user_auth(self.get_header(request))
        if act :
            method_list = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
            return 200 , response_standard(method_list)
        else:
            return response_standard(status=ResponseStatus.authen)