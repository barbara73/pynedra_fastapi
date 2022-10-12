class Option:

    def __init__(self,
                 option_name: str,
                 summary: str,
                 description: str,
                 ):
        self.description = description
        self.summary = summary
        self.option = option_name
        self.id = option_name
