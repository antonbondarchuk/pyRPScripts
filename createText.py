with db.Transaction('test'):
...     test = TextNote.Create(doc, doc.ActiveView.Id, XYZ(0,0,0), 'Anton Bondarchuk', TextNoteOptions(doc.GetDefaultElementTypeId(ElementTypeGroup.TextNoteType)))