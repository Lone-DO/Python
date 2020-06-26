import requests
import json

# read file
# with open('mockdata.json', 'r') as mock:
#     data = mock.read()

# parse file
# obj = json.loads(data)


class client:
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
    _channel = ""
    _default = f"https://www.reddit.com/"
    Sort = ""
    Url = ""
    data = {}
    comments = {}
    Options = {
        "after": "",
        "before": "",
        "t": "",
        "geo_filter": "",
        "call": ""
    }
    head = {
        'User-agent': "console:https://github.com/Lone-DO/Python:v0.0.6 (by u/lone-do)"
    }

    def __init__(self, channel="popular"):
        self._channel = f"r/{channel}"

    def setSort(self, sort):
        if sort in self.Sorts:
            print(f"Sorting by {sort}")
            self.Sort = sort
        else:
            print(f"Invalid Sort, Available: {self.Sorts}")

    def setChannel(self, channel):
        print(f"Changing Channel to {channel}")
        self.Options['after'] = ""
        self.Options["before"] = ""
        if channel[slice(2)] == "r/":
            self._channel = f"{channel}"
        else:
            self._channel = f"r/{channel}/"

    def setFilter(self, filter):
        if filter.upper() in self.Geo_filters:
            print(f"Changing region to {filter}")
            self.Options["geo_filter"] = filter
        else:
            print(f"Invalid Location, {self.Geo_filters}")

    def setTime(self, t):
        if t.lower() in self.Times:
            print(f"Changing Time range to {t}")
            self.Options["t"] = t
        else:
            print(f"Invalid Time, {self.Times}")

    def setAfter(self, after):
        if (after != ""):
            self.setBefore("")
        self.Options["after"] = after

    def setBefore(self, before):
        if (before != ""):
            self.setAfter("")
        self.Options['before'] = before

    def setFetch(self):
        self.Options['call'] = ""
        for attr, value in self.Options.items():
            if (self.Options[attr] and attr != "call"):
                self.Options['call'] += f"?{attr}={value}"
        self.Url = f"{self._default}{self._channel}{self.Sort}.json{self.Options['call']}"

    def reset(self, *args):
        self.setChannel("popular")
        for attr, value in self.Options.items():
            if (value != ""):
                self.Options[attr] = ""
        self.fetch()

    def fetch(self):
        # print("Loading Data...")
        self.setFetch()
        print(self.Url)
        res = requests.get(self.Url, headers=self.head).json()
        # res = requests.get(mock)
        # print("Complete...")
        self.data = res
        # self.data = res['data']['children']

    def fetchComments(self, link):
        Url = f"https://www.reddit.com{link}.json"
        print(f"Loading Post from... {Url}")
        res = requests.get(Url, headers=self.head).json()
        print("...Complete")
        self.comments = res

    def Settings(self):
        self.setFetch()
        print(f"""Settings
        Channel: {self._channel}
        Fetching from: {self.Url}
        Sort: {self.Sort}
        Loading content after: {self.Options['after']}
        Loading content before: {self.Options['before']}
        Posted within the last: {self.Options['t']}
        Content Region: {self.Options["geo_filter"]}
        """)
