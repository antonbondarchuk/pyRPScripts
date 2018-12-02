def feet_to_mm(feet):
    return feet * 304.8

def column_length(base, top):
    return abs(base) + abs(top)




col_collector = FilteredElementCollector(doc).\
            OfCategory(BuiltInCategory.OST_StructuralColumns).\
            OfClass(FamilyInstance).\
            ToElements()

col_collector = [column for column in col_collector if \
                column_length(feet_to_mm(
                column.LookupParameter('Base Offset').AsDouble()
                ), feet_to_mm(
                column.LookupParameter('Top Offset').AsDouble()
                )) > 3000]

t = Transaction(doc, 'Delete Columns')
t.Start()

for elem in col_collector:
    doc.Delete(elem.Id)

TaskDialog.Show("Delete Columns", "Columns longer than 3.0m deleted.")

t.Commit()
