import requests
Sorts = ["top", "new", "rising", "top"]
Time = ['hour', 'day', 'week', 'month', 'year', 'all']
Geo_filters = [
    "GLOBAL",  # Everywhere
    "US",  # United States
    "AR",  # Argentina
    "AU",  # Australia
    "BG",  # Bulgaria
    "CA",  # Canada
    "CL",  # Chile
    "CO",  # Columbia
    "HR",  # Croatia
    "CZ",  # Czech Republic
    "FL",  # Finland
    "GR",  # Greece
    "HU",  # Hungary
    "IS",  # Iceland
    "IN",  # India
    "IE",  # Ireland
    "JP",  # Japan
    "MY",  # Malaysia
    "MX",  # Mexico
    "NZ",  # New Zealond
    "PH",  # Philippines
    "PL",  # Poland
    "PT",  # Portgal
    "PR",  # Puerto Rico
    "RO",  # Romania
    "RS",  # Servia
    "SG",  # Singapore
    "SE",  # Sweden
    "TW",  # Taiwan
    "TH",  # Thailand
    "TR",  # Turkey
    "UK",  # United Kingdom
]


class client:
    _channel = "popular"
    _default = f"https://www.reddit.com/r/{_channel}"
    Sort = ""
    Url = ""

    Options = {
        "after": "",
        "t": "",
        "geo_filter": "",
        "call": ""
    }

    def __init__(self, channel="popular"):
        self._channel = channel

    def setSort(self, sort):
        if sort in Sorts:
            self.Sort = sort

    def setFilter(self, filter):
        if filter.upper() in Geo_filters:
            self.Options["geo_filter"] = filter

    def setTime(self, t):
        if t.lower() in Time:
            self.Options["t"] = t

    def setAfter(self, after):
        self.Options["after"] = after
        print(after)

    def setFetch(self):
        for attr, value in self.Options.items():
            if (self.Options[attr] and attr != "call"):
                self.Options['call'] += f"?{attr}={value}"
        self.Url = f"{self._default}{self.Sort}.json{self.Options['call']}"

    def fetch(self):
        print("Fetching Data...")
        self.setFetch()
        head = {
            'User-agent': "console:https://github.com/Lone-DO/Python:v0.0.5 (by u/lone-do)"
        }
        res = requests.get(self.Url, headers=head).json()
        print("Complete...")
        print(res)


reddit = client()
reddit.fetch()
