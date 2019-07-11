
import gdb

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
            raise gdb.GdbError("parameter input error, 'help pgmc' to get usage")

Pgmc()

