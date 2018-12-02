from random import randint
from rpw import db

rV_R = randint(0, 256)
rV_B = randint(0, 256)
rV_G = randint(0, 256)

ptn = db.Collector(of_class='FillPatternElement', \
                    where=lambda x: x.GetFillPattern(). \
                    IsSolidFill). \
                    get_element_ids()

with db.Transaction('Testing Override Graphics'):
    for elem in selection:
        org = OverrideGraphicSettings().\
                        SetProjectionFillColor(Color(rV_R,rV_B,rV_G))
        org.SetProjectionFillPatternId(ptn[0])
        doc.ActiveView.SetElementOverrides(elem.Id, org)
