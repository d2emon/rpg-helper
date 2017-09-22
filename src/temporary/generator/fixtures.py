class PlanetAtmosphere():
    def __init__(self, title, exist=True):
        self.title = title
        self.exist = exist
        
    def __repr__(self):
        return self.title
    
    
class SunType():
    def __init__(self, title, blue=False):
        self.title = title
        self.image = title
        self.blue = blue
        
    def __repr__(self):
        if self.blue:
            return "%s.blue" % (self.title)
        return self.title


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
    PlanetAtmosphere("None", False),
    PlanetAtmosphere("Thick", True),
    PlanetAtmosphere("Thin", True),
    PlanetAtmosphere("Unknown", True),
    PlanetAtmosphere("Fairly thick", True),
    PlanetAtmosphere("Fairly thin", True),
    PlanetAtmosphere("Very thick", True),
    PlanetAtmosphere("Very thin", True)
]
suns = [SunType("sun%d" % (i + 1), i > 29) for i in range(40)]
    
    
class PlanetType():
    earth = False
    max_moons = 60
        
    def __init__(self, image_id=1):
        self.image = image_id
        
    def __repr__(self):
        return self.image
    
    
class EarthPlanet(PlanetType):
    earth = True
    max_moons = 5
        
    def __repr__(self):
        if self.image < 10:
            image = "0" + str(self.image)
        else:
            image = str(self.image)
        return "earthPlanet%s" % (image)
    
    
class LayerPlanet(PlanetType):
    def __repr__(self):
        return "layerPlanet%s" % (self.image)
    
    
class TerPlanet(PlanetType):
    def __repr__(self):
        return "terplanet%s" % (self.image)
    
    
class MoonPlanet(PlanetType):
    def __repr__(self):
        return "moonPlanet%s" % (self.image)
    
    
class GasPlanet(PlanetType):
    def __repr__(self):
        return "gasPlanet%s" % (self.image)

    
earthPlanets = [EarthPlanet(i + 1) for i in range(40)]
layerPlanets = [LayerPlanet(i + 1) for i in range(40)]
terplanets = [TerPlanet(i + 1) for i in range(40)]
moonPlanets = [MoonPlanet(i + 1) for i in range(40)]
gasPlanets = [GasPlanet(i + 1) for i in range(40)]    

non_earthPlanets = (layerPlanets * 2) + terplanets + moonPlanets + gasPlanets
allPlanets = earthPlanets + non_earthPlanets