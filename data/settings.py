class Settings:

    def __init__(self,
                 option: str,
                 summary: str,
                 description: str,
                 ):

        self.description = description
        self.summary = summary
        self.option = option
        self.id = option
