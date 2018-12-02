refPlan_col = FilteredElementCollector(doc).  \
            OfClass(ReferencePlane).  \
            ToElements()

for i in refPlan_col:
    print i.Name, i.Id
