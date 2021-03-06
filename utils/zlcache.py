import memcache
import config

cache = memcache.Client([config.MEMACHE_CLIENT], debug=True)

def set(key, value, timeout=60):
    return cache.set(key, value, timeout)

def get(key):
    return cache.get(key)

def delete(key):
    return cache.delete(key)

if __name__ == "__main__":
    set("test","123")
    print(get("test"))