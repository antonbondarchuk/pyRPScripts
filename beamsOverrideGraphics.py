from random import randint

randValueR = randint(0, 256)
randValueB = randint(0, 256)
randValueG = randint(0, 256)

pattern = FilteredElementCollector(doc).OfClass(FillPatternElement)
pattern = [solid for solid in pattern if solid.GetFillPattern().IsSolidFill]
solidFillId = pattern[0].Id

# org = OverrideGraphicSettings().\
#                 SetProjectionFillColor(Color(randValueR,randValueB,randValueG))
# org.SetProjectionFillPatternId(solidFillId)

cols = FilteredElementCollector(doc).\
        OfCategory(BuiltInCategory.OST_StructuralColumns).\
        OfClass(FamilyInstance)

# - - - - -
t = Transaction(doc, 'Override Graphics')
t.Start()
for elem in cols:
    org = OverrideGraphicSettings().\
                    SetProjectionFillColor(Color(randValueR,randValueB,randValueG))
    org.SetProjectionFillPatternId(solidFillId
    doc.ActiveView.SetElementOverrides(elem.Id, org)
t.Commit()
