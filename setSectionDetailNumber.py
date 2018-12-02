with db.Transaction('Rename Section Views'):
    for el in selection:
        el.LookupParameter('Detail Number').Set(el.Name)