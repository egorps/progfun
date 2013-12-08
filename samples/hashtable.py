class HashTable(object):

    def __init__(self, slots = 1024):
        self.mod = slots
        self.table = [[] for x in xrange(slots)]

    def get(self, key):
        mod_key = id(key) % self.mod
        for stored_key, value in self.table[mod_key]:
            if key == stored_key:
                return value
        raise Exception("No element found for " + str(key))
    def put(self, key, value):
        mod_key = id(key) % self.mod
        self.table[mod_key].append((key,value))

if __name__ == '__main__':
    table = HashTable(256)
    table.put("john", "303-957-7239")
    table.put("sarge", "479-601-4992")

    print "John's number: ", table.get("john")
    print "Sarge's number ", table.get("sarge")






