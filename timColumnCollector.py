elFilter = StructuralMaterialTypeFilter(StructuralMaterialType.Wood)
timcols = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_StructuralColumns). \
    WhereElementIsNotElementType(). \
    WherePasses(elFilter). \
    ToElementIds()

toSelection = uidoc.Selection.SetElementIds(timcols)
t = Transaction(doc, 'Isolate Timber Columns')
t.Start()
doc.ActiveView.IsolateElementsTemporary(timcols)
t.Commit()
