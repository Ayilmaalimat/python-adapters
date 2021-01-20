import logging

from spyne import *
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

import config

class Soap(ServiceBase):

    @rpc(Integer, _returns=AnyDict)
    def XRoad(ctx, pin):
        query = """SELECT * FROM public."People" WHERE "People"."Pin" = '%s';"""

        config.cursor.execute(
            query, (pin, )
        )
        data = config.cursor.fetchone()
        dic = {
            'pin' : data[0],
            'name' : data[1],
            'data_create' : data[2],
            'gender' : data[3]
        }
        return dic

    @rpc(Integer, _returns=File)
    def ImageDownload(ctx, pin):
        query = """SELECT * FROM public."People" WHERE "People"."Pin" = '%s';"""

        config.cursor.execute(
            query, (pin, )
        )
        data = config.cursor.fetchone()

        return File.Value(data = data[4])
   

app = Application([Soap], tns='Producer',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11()
)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    application = WsgiApplication(app)
    server = make_server('0.0.0.0', 8000, application)
    server.serve_forever()
