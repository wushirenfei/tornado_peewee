import peewee
import peewee_async
import tornado.web
from tornado import httpserver


database = peewee_async.PooledMySQLDatabase(
    'alexdb', host='127.0.0.1', port=3306,
    user='root', password='')


# Define model
class TestNameModel(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = database

    def __str__(self):
        return self.name


# Create table, add some instances
TestNameModel.create_table(True)
TestNameModel.get_or_create(id=1, defaults={'name': "TestNameModel id=1"})
TestNameModel.get_or_create(id=2, defaults={'name': "TestNameModel id=2"})
TestNameModel.get_or_create(id=3, defaults={'name': "TestNameModel id=3"})
database.close()


# Define handlers
class RootHandler(tornado.web.RequestHandler):
    """
    Accepts GET methods.
    GET: get instance by id, `id` argument is required
    """
    async def get(self):
        obj_id = self.get_argument('id', None)
        try:
            obj = await self.application.objects.get(TestNameModel, id=obj_id)
            self.write({
                'id': obj.id,
                'name': obj.name,
            })
        except TestNameModel.DoesNotExist:
            raise tornado.web.HTTPError(404, "Object not found!")


def main():
    app = tornado.web.Application(handlers=[
        (r'/alex', 'demo.RootHandler'), ], debug=True)

    # Set up database and manager
    app.objects = peewee_async.Manager(database)

    # Run loop
    print("""Run application server http://127.0.0.1:8888s
        Try GET urls:
        http://127.0.0.1:8888?id=1
    ^C to stop server""")

    server = httpserver.HTTPServer(app, xheaders=True)
    server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()




