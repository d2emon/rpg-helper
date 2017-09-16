class GameSystem():
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', "RPG")
        self.website = kwargs.get('website', "")
        # url_for('select_rpg', rpg_id=rpg.id)
        self.url = kwargs.get('url', "/")

    def __repr__(self):
        return self.title

    @property
    def edit_url(self):
        return False
