def pick():
    l = db.Collector(of_class='Level').get_first().unwrap()
    t = db.Collector( \
            of_category='Structural Framing', is_type=True, \
            where=lambda x: x.name=="P2-C20024").get_first().unwrap()

    __window__.Hide()
    picked_face = uidoc.Selection.PickObject(ObjectType.Face)
    picked_lines = uidoc.Selection.PickObjects(ObjectType.Element)
    face = doc.GetElement(picked_face). \
                                GetGeometryObjectFromReference(picked_face)
    lines = []
    for el in picked_lines:
        lines.append(doc.GetElement(el).GeometryCurve)

    for el in lines:
        p = Line.CreateBound(
        face.Project(el.GetEndPoint(0)).XYZPoint, \
        face.Project(el.GetEndPoint(1)).XYZPoint)
        with db.Transaction('Create beam on Face'):
            doc.Create.NewFamilyInstance(p, t, l, StructuralType.Beam)

pick()