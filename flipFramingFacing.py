with db.Transaction('Flipping Facing'):
    for el in selection:
        el.flipFacing()
