import sys
sys.path.append('dependencies/image-store-py-web-api-consumer')
from Consumer import Consumer

class Consumer_test:
    def __init__(self):
        self.c = Consumer()
        
    def get(self):
        print('\x1b[6;30;42m' + 'GET' + '\x1b[0m')
        print(self.c.get())
        print('{}\n'.format(self.c.get().json()))

    # get a data entry by id
    def get_id(self, id):
        print('\x1b[6;30;42m' + 'GET ID({})'.format(id) + '\x1b[0m')
        print(self.c.get_id(id))
        print('{}\n'.format(self.c.get_id(id).json()))


    # get latest data entry
    def get_latest(self):
        print('\x1b[6;30;42m' + 'GET LATEST' + '\x1b[0m')
        print(self.c.get_latest())
        print('{}\n'.format(self.c.get_latest().json()))

    # post a data entry, id incremented by internal mySQL counter
    def post(self):
        print('\x1b[6;30;42m' + 'POST' + '\x1b[0m')
        print(self.c.post())
        print('{}\n'.format(self.c.post().json()))

    # TODO be able to edit payload with keywords e.g: title.TEST
    # edit existing data entry by id
    def put(self, id):
        print('\x1b[6;30;42m' + 'PUT({})'.format(id) + '\x1b[0m')
        print(self.c.put(id))

    # delete data entry by id
    def delete(self, id):
        print('\x1b[6;30;42m' + 'DELETE({})'.format(id)  + '\x1b[0m')
        print(self.c.delete(id))

if __name__ == '__main__':
    consumer = Consumer_test()
    consumer.get()
    consumer.get_id(1)
    consumer.post()
    consumer.get_latest()
    consumer.put(10)