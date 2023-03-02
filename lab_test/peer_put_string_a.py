import zenoh, time


if __name__ == "__main__":
    conf = zenoh.Config.from_obj({'mode': 'peer'})
    session = zenoh.open(conf)
    key = "demo/strings/a"
    pub = session.declare_publisher(key)
    counter = 0
    while True:
        buf = f"String a {counter}"
        print(f"Putting Data ('{key}': '{buf}')...")
        pub.put(buf)
        counter = counter + 1
        time.sleep(10)
