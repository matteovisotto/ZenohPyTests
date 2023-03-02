import zenoh


def listener(sample):
    print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.decode('utf-8')}')")


if __name__ == "__main__":
    conf = zenoh.Config.from_obj({'mode': 'peer'})
    session = zenoh.open(conf)
    sub = session.declare_subscriber('demo/**/hum', listener)
    while True:
        pass