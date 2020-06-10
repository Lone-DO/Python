import requests
import json

# read file
with open('mockdata.json', 'r') as mock:
    data = mock.read()

# parse file
obj = json.loads(data)
Sorts = ["top", "new", "rising", "top"]
Times = ['hour', 'day', 'week', 'month', 'year', 'all']

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
    _channel = "r/popular"
    _default = f"https://www.reddit.com/{_channel}"
    Sort = ""
    Url = ""
    data = {}
    comments = {}
    Options = {
        "after": "",
        "t": "",
        "geo_filter": "",
        "call": ""
    }
    head = {
        'User-agent': "console:https://github.com/Lone-DO/Python:v0.0.5 (by u/lone-do)"
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
        if t.lower() in Times:
            self.Options["t"] = t

    def setAfter(self, after):
        self.Options["after"] = after  # Data.Data.After

    def setFetch(self):
        for attr, value in self.Options.items():
            if (self.Options[attr] and attr != "call"):
                self.Options['call'] += f"?{attr}={value}"
        self.Url = f"{self._default}{self.Sort}.json{self.Options['call']}"

    def reset(self):
        for attr, value in self.Options.items():
            if (value != ""):
                self.Options[attr] = ""
        self.fetch()

    def fetch(self):
        print("Loading Data...")
        self.setFetch()

        res = requests.get(self.Url, headers=self.head).json()
        # res = requests.get(mock)
        print("Complete...")
        self.data = res
        # self.data = res['data']['children']

    def fetchComments(self, link):
        Url = f"https://www.reddit.com/{link}.json"
        print("Loading Post...")
        res = requests.get(Url, headers=self.head).json()
        print("...Complete")
        self.comments = res

    def Settings(self):
        self.setFetch()
        print(f"""Settings
        Channel: r/{self._channel}
        Fetching from: {self.Url}
        Sort: {self.Sort}
        Loading content after: {self.Options['after']}
        Posted within the last: {self.Options['t']}
        Content Region: {self.Options["geo_filter"]}
        """)
