environments = [
    "Hospitable",
    "Gentle",
    "Moderate",
    "Fairly gentle",
    "Fairly hospitable",
    "Unknown",
    "Quite hostile",
    "Hostile",
    "Very hostile",
    "Dangerous",
    "Very dangerous",
    "Deadly",
    "Unsafe",
    "Treacherous",
    "Unstable"
]
maps = [
    "Yes",
    "No",
    "Outdated version"
]
atmospheres = [
    ("None", False),
    ("Thick", True),
    ("Thin", True),
    ("Unknown", True),
    ("Fairly thick", True),
    ("Fairly thin", True),
    ("Very thick", True),
    ("Very thin", True)
]
suns = [["sun%d" % (i + 1), i > 29] for i in range(40)]
