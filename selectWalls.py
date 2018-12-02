"""Select all walls in active project that have 'Unconnected Height' over 3000.
Report TaskDialog msg with number of wall selected and time stamp.
Use 'WherePasses' method.
"""

# EVALUATOR:
fnrv = FilterNumericGreaterOrEqual()

# PROVIDER:
pvp = ParameterValueProvider(ElementId(
                    BuiltInParameter.WALL_USER_HEIGHT_PARAM))
# FILTER RULE:
rule_val = FilterDoubleRule(pvp, fnrv, (3000/304.8), 1E-6)

# ELEMENT FILTER:
filter_wall = ElementParameterFilter(rule_val)

# APPLY FILTER:
wall_col = FilteredElementCollector(doc).WherePasses(filter_wall)\
            .ToElementIds()

# SELECTION:
uidoc.Selection.SetElementIds(wall_col)
