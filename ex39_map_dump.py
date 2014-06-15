def Map(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def Map_hash(aMap, key):
    """Given a key this will create a number and then convert it to
    and index for the aMap's buckets."""
    return hash(key) % len(aMap)

def Map_get_bucket(aMap, key):
    """Given a key, find the bucket where it would go"""
    bucket_id = Map_hash(aMap, key)
    return aMap[bucket_id]

def Map_get_slot(aMap, key, default=None):
    """Returns the index, key, and value of a slot found in a bucket."""
    bucket = Map_get_bucket(aMap, key)
    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v
        
    return -1, key, default

def Map_get(aMap, key, default=None):
     """Gets the value in a bucket for the given key, or the default."""
     i, k, v = Map_get_slot(aMap, key, default=default)
     return v
 
def Map_set(aMap, key, value):
     """Sets the key to the value, replacing any existing value."""
     bucket = Map_get_bucket(aMap, key)
     i, k, v = Map_get_slot(aMap, key)
     
     if v:
         bucket[i] = (key, value)
     else:
         bucket.append((key, value))

def Map_delete(aMap, key):
    """Deletes the given key from the Map"""
    bucket = Map_get_bucket(aMap, key)
    
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def Map_list(aMap):
    """Prints out what's in the Map"""
    full_buckets = 0
    for bucket in aMap:
        if bucket:
            full_buckets += 1
            for k, v in bucket:
                print k, v
    return full_buckets

def Map_dump(aMap):
    """Dumps the contents of every bucket"""
    # First get the buckets
    for i, b in enumerate(aMap):
        # Get the contents of the bucket only if it not empty
        if b != []:
            print "Bucket nr: %r" % i, " has this content: %r" % b

def Map_clean(aMap):
    """Removes all items from aMap"""
    # First get the full buckets
    for i, bucket in enumerate(aMap):
        if bucket != []:
            aMap[i] = []

def Map_has_key(aMap, key):
    """Checks whether a key exists in aMap."""
    i, k, v = Map_get_slot(aMap, key, None)
    
    if v:
        return True
    
    return False

def Map_items(aMap):
    """Returns a list of key, value pairs (tupple)"""
    items = []
    for bucket in aMap:
        if bucket:
            for item in bucket:
                items.append(item)
    
    return items

def Map_keys(aMap):
    """Returns a list of keys."""
    keys = []
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                keys.append(k)
    
    return keys

def Map_pop(aMap, key, default=None):
    """Removes the key and returns the corresponding value"""
    value = Map_get(aMap, key, default)
    Map_delete(aMap, key)
    
    return value

def Map_popitem(aMap):
    """Removes the first key, value pair and returns them as a tupple.
    Returns None when aMap is empty."""
    for bucket in aMap:
        if bucket != []:
            k, v = bucket[0]
            Map_delete(aMap, k)
            return (k, v)
    
    return None

def Map_values(aMap):
    """Returns a list of values."""
    values = []
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                values.append(v)
    
    return values

# The tests that it will work.

jazz = Map()

Map_set(jazz, 'Miles Davis', 'Flamenco Sketches')
# confirms set will replace previous one
Map_set(jazz, 'Miles Davis', 'Kind Of Blue')
Map_set(jazz, 'Duke Ellington', 'Beginning To See The Light')
Map_set(jazz, 'Billy Strayhorn', 'Lush Life')

print "---- Dump test ----"
Map_dump(jazz)

print "---- Pop test ----"
assert Map_pop(jazz, 'Billy Strayhorn') == 'Lush Life'
assert Map_get(jazz, 'Billy Strayhorn', None) == None

print "---- Popitem test ----"
assert Map_popitem(jazz) == ('Miles Davis', 'Kind Of Blue')


print "---- Clean test ----"
Map_clean(jazz)

assert Map_list(jazz) == 0

Map_set(jazz, 'Miles Davis', 'Kind Of Blue')
Map_set(jazz, 'Duke Ellington', 'Beginning To See The Light')
Map_set(jazz, 'Billy Strayhorn', 'Lush Life')
print "---- List Test ----"
Map_list(jazz)

print "---- Get Test ----"
assert Map_get(jazz, 'Miles Davis') == 'Kind Of Blue'
assert Map_get(jazz, 'Duke Ellington') == 'Beginning To See The Light'
assert Map_get(jazz, 'Billy Strayhorn') == 'Lush Life'

print "---- Has Key test ----"
assert Map_has_key(jazz, 'Miles Davis')

print "---- Items test ----"
assert Map_items(jazz) == [('Billy Strayhorn', 'Lush Life'), ('Miles Davis', 
'Kind Of Blue'), ('Duke Ellington', 'Beginning To See The Light')]

print "---- Keys test ----"
assert Map_keys(jazz) == ['Billy Strayhorn', 'Miles Davis', 'Duke Ellington']

print "---- Values test ----"
assert Map_values(jazz) == ['Lush Life', 'Kind Of Blue',
'Beginning To See The Light']

print "---- Delete Test ----"
print "** Goodbye Miles **"
Map_delete(jazz, "Miles Davis")
assert Map_get(jazz, 'Miles Davis') == None

print "** Goodbye Duke"
Map_delete(jazz, "Duke Ellington")
assert Map_get(jazz, 'Duke Ellington') == None

print "** Goodbye Billy **"
Map_delete(jazz, "Billy Strayhorn")
assert Map_get(jazz, 'Billy Strayhorn') == None

print "** Goodbye Pork Pie Hat **"
Map_delete(jazz, "Charles Mingus")
assert Map_get(jazz, 'Charles Mingus') == None