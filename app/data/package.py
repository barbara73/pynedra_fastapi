class Package:

    def __init__(self,
                 package_name: str,
                 summary: str,
                 description: str,
                 ):
        self.description = description
        self.summary = summary
        self.package = package_name
        self.id = package_name
