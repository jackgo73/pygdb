# pygdb

gdb python utils for pg and gp debug!

## example
pgmc

```gdb
gdb attach 12345 -x ./pygdb.py

(gdb) help pgmc
Print statistics about the named context and all its descendants
    usage:
        attach postgresql's process first.
        pgmc (memorycontext name) (the number of child contexts shown)
    example:
        (gdb) pgmc TopMemoryContext 500
        
(gdb) pgmc
$1 = void
```
