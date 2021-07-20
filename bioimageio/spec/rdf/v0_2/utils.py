from bioimageio.spec.shared.io import IO_Base
from . import converters, nodes, raw_nodes, schema


class IO(IO_Base):
    preceding_io_class = bioimageio.spec.module.v0_1.utils.IO
    converters = converters
    schema = schema
    raw_nodes = raw_nodes
    nodes = nodes
