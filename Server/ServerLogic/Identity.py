class Identity:
    # more attributes will be added as the database grows
    def __init__(self, location="not available", flagged="not flagged", provider="unknown"):
        self.location = location
        if not self.location:
            self.location = "not available"
        self.flagged = flagged 
        if not self.flagged:
            self.flagged = "not flagged"
        self.provider = provider
        if not self.provider:
            self.provider = "unknown"
    
    def __str__(self):
        return f"""The caller's location is {self.location} 
        \nThe caller is {self.flagged}
        \nThe caller's provider is {self.provider}
        """