import zenoh, random, time

random.seed()


def read_temp():
    return random.randint(15, 30)


if __name__ == "__main__":
    conf = zenoh.Config.from_obj({'mode': 'peer'})
    session = zenoh.open(conf)
    key = "demo/sens1/hum"
    pub = session.declare_publisher(key)
    while True:
        t = read_temp()
        buf = f"{t}"
        print(f"Putting Data ('{key}': '{buf}')...")
        pub.put(buf)
        time.sleep(10)
