import zenoh


def listener(sample):
    print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.decode('utf-8')}')")


if __name__ == "__main__":
    conf = zenoh.Config.from_obj({'mode': 'client', "connect": {"endpoints": ["tcp/172.16.0.40:7447"]}})
    session = zenoh.open(conf)
    sub = session.declare_subscriber('demo/**/temp', listener)
    while True:
        pass
