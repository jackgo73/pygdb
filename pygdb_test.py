import re


def test_case1():
    s = '$3 = {type = T_AllocSetContext, isReset = 0 '', allowInCritSection = 0 '', methods = 0xd43e40 <AllocSetMethods>, parent = 0x0, firstchild = 0x250a3e8, prevchild = 0x0, nextchild = 0x0, name = 0x250a268 "TopMemoryContext", reset_cbs = 0x0}'
    print s

    matchObj = re.match(r'.*{type = ([^,]*),', s, re.M | re.I)
    print matchObj.group()
    print matchObj.group(1).split("_")[1]


test_case1()