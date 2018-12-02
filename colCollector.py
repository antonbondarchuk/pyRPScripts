def cubFootToCubMeters(arg):
    return arg * 0.0283168

col_filter = ElementCategoryFilter(BuiltInCategory.OST_StructuralColumns)
col_collector = FilteredElementCollector(doc).WherePasses(col_filter)
col_collector = col_collector.OfClass(FamilyInstance)

total_volume = 0.0

for i in col_collector:
    total_volume += i.LookupParameter('Volume').AsDouble()

result = round(cubFootToCubMeters(total_volume), 2)

msg = "Total Concrete Volume of Columns: {}m3".format(result)
TaskDialog.Show('Revit', msg)
