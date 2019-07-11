import re

import gdb


def debug_print(s):
    gdb.execute("echo " + s + "\n")


class Pgmc(gdb.Command):
    """Print statistics about the named context and all its descendants
    usage:
        attach postgresql's process first.
        pgmc (memorycontext name) (the number of child contexts shown)
    example:
        (gdb) pgmc TopMemoryContext 500
    """

    def __init__(self):
        super(self.__class__, self).__init__("pgmc", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        if len(argv) == 0:
            gdb.execute("p MemoryContextStatsDetail(TopMemoryContext,200)")
        elif len(argv) == 2:
            gdb.execute("p MemoryContextStatsDetail(" + argv[0] + ", " + argv[1] + ")")
        else:
            raise gdb.GdbError("parameter input error, 'help " + Pgmc.__name__.lower() + "' to get usage")


class Pgst(gdb.Command):
    """Convert structure types by type
    usage:
        attach postgresql's process first.
        pgst (structure variable)
    example:
        (gdb) pgst TopMemoryContext
    """

    def __init__(self):
        super(self.__class__, self).__init__("pgst", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        if len(argv) != 1:
            raise gdb.GdbError("parameter input error, 'help " + Pgst.__name__.lower() + "' to get usage")
        st = gdb.execute("p *" + argv[0], to_string=True)
        match_type = re.match(r'.*{type = ([^,]*),', st, re.M | re.I)
        if not match_type:
            raise gdb.GdbError("struct does not contain type")
        type = match_type.group(1).split("_")[1]
        debug_print("struct type is " + type + " ,start conversion")
        gdb.execute("p (" + type + ")" + argv[0])

Pgmc()
Pgst()
