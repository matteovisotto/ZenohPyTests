import zenoh, sys, time
from zenoh import config, Sample, Value

key = 'demo/sens2/hum'
value = 90
complete = True


def queryable_callback(query):
    print(f">> [Queryable ] Received Query '{query.selector}'" + (f" with value: {query.value.payload}" if query.value is not None else ""))
    query.reply(Sample(key, value))


# initiate logging
zenoh.init_logger()

print("Opening session...")
conf = zenoh.Config.from_obj({'mode': 'peer', "connect": {"endpoints": ["tcp/172.16.0.40:7447"]}})
session = zenoh.open(conf)

print("Declaring Queryable on '{}'...".format(key))
queryable = session.declare_queryable(key, queryable_callback, complete)

print("Enter 'q' to quit...")
c = '\0'
while c != 'q':
    c = sys.stdin.read(1)
    if c == '':
        time.sleep(1)

queryable.undeclare()
session.close()