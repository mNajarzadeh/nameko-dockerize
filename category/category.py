# category.py
from nameko_sqlalchemy import DatabaseSession
from nameko.rpc import rpc,RpcProxy
from nameko.events import EventDispatcher, event_handler

class CategoryService:
    name = "category_service"
    dispatch = EventDispatcher()

    @rpc
    def test(self):
        pass

    @rpc
    def category_get_category(self, data):
        pass