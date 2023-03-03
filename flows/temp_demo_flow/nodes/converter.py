from zenoh_flow.interfaces import Operator
from zenoh_flow import Input, Output
from zenoh_flow.types import Context
from typing import Dict, Any


class Converter(Operator):
    def __init__(
        self,
        context: Context,
        configuration: Dict[str, Any],
        inputs: Dict[str, Input],
        outputs: Dict[str, Output],
    ):
        self.output = outputs.get("tempf", None)
        self.in_stream = inputs.get("temp", None)

        if self.in_stream is None:
            raise ValueError("No input 'temp' found")
        if self.output is None:
            raise ValueError("No output 'tempf' found")

    def finalize(self) -> None:
        return None

    async def iteration(self) -> None:
        data_msg = await self.in_stream.recv()
        temp = data_msg.data
        tempf = (temp * (9/5)) + 32

        await self.output.send(tempf)
        return None



def register():
    return Converter