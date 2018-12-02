from rpw import db

viewId = elem.ViewId

lvls = db.Collector(view=elem.ViewId, of_class='Level')

with db.Transaction('Hide level bubbles'):
    for i in  lvls:
        i.HideBubbleInView(DatumEnds.End0, doc.GetElement(viewId))
        i.HideBubbleInView(DatumEnds.End1, doc.GetElement(viewId))
