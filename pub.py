import zenoh, random, time

random.seed()


def read_temp():
    return random.randint(15, 30)


if __name__ == "__main__":
    #conf = zenoh.Config.from_obj({'mode': 'client', "connect": { "endpoints": [ "tcp/srvasus.intranet.matmacsystem.it:7447" ] }})
    conf = zenoh.Config.from_obj(
        {'mode': 'client'})
    session = zenoh.open(conf)
    key = 'demo/test/temp'
    pub = session.declare_publisher(key)
    pub2 = session.declare_publisher('demo/test2/temp')
    while True:
        t = read_temp()
        buf = f"{t}"
        print(f"Putting Data ('{key}': '{buf}')...")
        pub.put(buf)
        pub2.put(buf)
        time.sleep(10)
