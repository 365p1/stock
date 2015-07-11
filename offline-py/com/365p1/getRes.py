#!/usr/bin/env python
import json
if __name__ == "__main__":
    f = open("//home/chen/extend/data/2015-7-7/res")
    lines = f.readlines()
    ss = []
    i = 0
    for line in lines:
        l = unicode(line, "gb18030").encode("utf8")
        arr = l.split('\t')
        if i == 0:
            print arr[0], arr[1], arr[2], arr[3], arr[5], arr[7], arr[9]
            i += 1
            continue
        print arr[0], arr[1], arr[2], arr[3], arr[5], arr[7], arr[9]
        code = arr[0]
        name = arr[1]
        if arr[2].strip() == "--":
            cp = 0.0
        else:
            try:
                cp = float(arr[2])
            except:
                continue

        if arr[3].strip() == "--":
            sy = 10000000
        else:
            try:
                sy = float(arr[3])
            except:
                continue
        zg = float(arr[5])
        jz = float(arr[7])
        fz = float(arr[9])
        p1 = cp / sy * 15 + (30 - fz)/100 * jz / zg
        p2 = jz / zg * 1.2
        if p1 > p2:
            p = p1
        else:
            p = p2
        rat = cp / p
        print arr[0], arr[1], cp, p, rat
        ss.append((arr[0], arr[1], cp, p, rat))
        i += 1
    ss.sort(key=lambda x: x[3])
    res = []
    for t in ss:
        res.append(t)
    out = json.dumps(res)
    print(out)