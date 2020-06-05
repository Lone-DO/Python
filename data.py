content = {
    "default": "https:# www.reddit.com/r/popular",
    
    "sort" : "", #[hot, new, top, rising]
    "t" : "", # [hour | day | week | month | year | all]
    "geo_filter" : [
        "GLOBAL", # Everywhere
        "US", #  United States
        "AR", #  Argentina
        "AU", #  Australia
        "BG", #  Bulgaria
        "CA", #  Canada
        "CL", #  Chile
        "CO", #  Columbia
        "HR", #  Croatia
        "CZ", #  Czech Republic
        "FL", #  Finland
        "GR", #  Greece
        "HU", #  Hungary
        "IS", #  Iceland
        "IN", #  India
        "IE", #  Ireland
        "JP", #  Japan
        "MY", #  Malaysia
        "MX", #  Mexico
        "NZ", #  New Zealond
        "PH", #  Philippines
        "PL", #  Poland
        "PT", #  Portgal
        "PR", #  Puerto Rico
        "RO", #  Romania
        "RS", #  Servia
        "SG", #  Singapore
        "SE", #  Sweden
        "TW", #  Taiwan
        "TH", #  Thailand
        "TR", #  Turkey
        "UK", #  United Kingdom
    ],

    "options" : {
        "after": "t3",
        "t": "",
        "geo_filter": "US",
        "call": ""
    },
    "url" : "",
}



content["url"] = f"{content['default']}{content['options']['call']}.json"
print(content['url'])

#  Loop through options, if any are set, append to call
# for attr, value in content['options'].__dict__.items():
#     print(attr, value)
#     if (content.options[attr] and attr != "call"):
#         content.options.call += f"?{value}"