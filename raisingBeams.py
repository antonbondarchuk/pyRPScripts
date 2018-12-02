from rpw import db

with db.Transaction('Rising beams by 350mm'):
    for i in selection:
        startV = i.LookupParameter('Start Level Offset').AsDouble()
        endV = i.LookupParameter('End Level Offset').AsDouble()
        i.LookupParameter('Start Level Offset').Set(startV + 1.148293963254593)
        i.LookupParameter('End Level Offset').Set(endV + 1.148293963254593)
