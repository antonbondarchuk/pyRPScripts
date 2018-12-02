frame = db.Collector(of_category='Structural Framing', is_type=True)
col = db.Collector(of_category='Structural Columns', is_type=True)


with db.Transaction("Set Framing Type Marks"):
    for el in frame:
        name = el.LookupParameter('Type Name').AsString()
        tMark = name.split("-")[0]
        i.LookupParameter('Type Mark').Set(tMark)

with db.Transaction("Set Column Type Marks"):
    for el in col:
        name = el.LookupParameter('Type Name').AsString()
        tMark = name.split("-")[0]
        i.LookupParameter('Type Mark').Set(tMark)