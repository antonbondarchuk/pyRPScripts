zL = 8.858267716535433

startL = XYZ(selection[0].Location.Point.X, selection[0].Location.Point.Y, zL)
endL = XYZ(selection[1].Location.Point.X, selection[1].Location.Point.Y, zL)


lineL = Line.CreateBound(startL, endL)

l = doc.GetElement(selection[0].LevelId)
t = db.Collector( \
        of_category='Structural Framing', is_type=True, \
        where=lambda x: x.name == 'WH2-200x45LVL').get_first().unwrap()

with db.Transaction('Create Lintel & Sill'):
    doc.Create.NewFamilyInstance(lineL, t, l, StructuralType.Beam)