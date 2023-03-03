from zenoh_flow.interfaces import Sink
from zenoh_flow import DataReceiver
from zenoh_flow.types import Context
from typing import Dict, Any
import zenoh
from zenoh import Reliability
import asyncio
import json

DEFAULT_ZENOH_LOCATOR = "tcp/127.0.0.1:7447"
DEFAULT_MODE = "client"
DEFAULT_KE = "demo/sens1/temp/f"
PERIOD = 0.5


class SinkPub(Sink):
    def __init__(
        self,
        context: Context,
        configuration: Dict[str, Any],
        inputs: Dict[str, DataReceiver],
    ):
        self.input = inputs.get("tempf", None)
        if self.output is None:
            raise ValueError("Could not find input 'tempf'")

        self.locator = configuration.get("locator", DEFAULT_ZENOH_LOCATOR)
        self.mode = configuration.get("mode", DEFAULT_MODE)
        self.ke = configuration.get("key_expression", DEFAULT_KE)

        self.zconf = zenoh.Config()

        self.zconf.insert_json5(zenoh.config.MODE_KEY, json.dumps(self.mode))
        self.zconf.insert_json5(
            zenoh.config.CONNECT_KEY, json.dumps([self.locator])
        )

        self.session = zenoh.open(self.zconf)
        self.pub = self.session.declare_publisher(self.ke)

    def finalize(self):
        self.sub.undeclare()
        self.session.close()

    async def iteration(self):
        data_msg = await self.in_stream.recv()
        tempf = data_msg.data
        self.pub.put(tempf)
        return None

def register():
    return SinkPub