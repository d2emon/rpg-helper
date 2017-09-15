class GameSystem():
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', "RPG")
        self.website = kwargs.get('website', "")

    def __repr__(self):
        return self.title

    @property
    def url(self):
        # url_for('select_rpg', rpg_id=rpg.id)
        return "/"


games = [
    GameSystem(title="Game", website="http://127.0.0.1:5000/"),
    GameSystem(title="Game1", website="http://127.0.0.1:8000/"),
    GameSystem(title="Pathfinder"),
    GameSystem(title="GURPS"),
    GameSystem(title="Tunels & Trolls"),
]
