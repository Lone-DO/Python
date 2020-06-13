import data
from Display import Display

reddit = data.client()


def start():
    reddit.fetch()
    Display('page', reddit.data)


start()
print("""Welcome to the Reddit Console Client
    Enjoy 
    """)
while True:
    data = reddit.data["data"]["children"]
    help = ["help", "-help", "--help", "-h", "--h"]

    print("\nEnter --help for list of options")
    print(f"Currently browsing, {reddit.Url}")

    userInput = input("\t$ ")
    args = userInput.lower().split(" ")
    hasArgs = len(args) > 1 and args[1]
    isLoad = args[0] == "load"
    isChange = args[0] == "change"
    isList = args[0] in ["list", "lists"]
    isOption = args[0] in ["option", "options"]
    isSetting = args[0] in ["setting", "settings"]

    # Return child via num/index
    def getChild(num): return data[num].get("data")["name"]

    # Quit application
    if args[0] in ["q", "quit", "exit", "terminate", "close"]:
        break
    if args[0] == "reset":
        reddit.reset()
        start()
        continue
    if args[0] == 'refresh':
        reddit.fetch()
        start()
    # Show Help List
    if (args[0] in help):
        print(f"""
            The following commands are available,
            {help} to list options
            Load, [optional args: 'prev', 'next']
            List, [optional args: 'array/ post #]
            Settings, to browse settings/ current parameters
            Change (setting), [arg: "Channel", "Sort", "time", "region"]
            Refresh, to reload content (call after changing a setting)
            Reset, restarts application with default settings
        """)
        continue
    # Show current options
    if args[0] == "options":
        reddit.Settings()

    # Load Commands
    if isLoad:
        if (hasArgs and args[1].lower() in ["prev", "last"]):
            reddit.setBefore(getChild(0))
            start()
        elif (hasArgs and args[1].lower() in ["next", "more"]):
            reddit.setAfter(getChild(len(data) - 1))
            start()
        elif (hasArgs):
            print(f"""Invalid input {args}
            Load has the following Arguments:
                "prev", "last", loads previous page
                "next", "more", loads next page
                """)
        else:
            Display('page', reddit.data)
    # List Commands
    if (isList):
        if (hasArgs and args[1].lower() in help):
            print(f"""
            List has the following Arguments:
            input the article number to load content,
                Ex. list 2, loads first article listed
                ---
                [2] GTA through the years. (i.redd.it)
                    submitted 3 minutes ago by u/sabeer777 to r/gaming
                    104977 upvotes with 4270 comments
                ---
            """)
            continue
        elif (hasArgs):
            try:
                index = int(args[1])
            except:
                print(
                    f"{args[1]} Invalid List Argument, use 'list -h' for help")
                continue

            if index < len(Display.list):
                reddit.fetchComments(Display.list[index])
                Display('post', reddit.comments)
            elif index >= len(Display.list):
                print("Page Unavailable, Please try again")
        else:
            print(Display.list)
    # Change Setting Commands
    if (isChange):
        if (len(args) == 1):
            print("""Available Options
                Region, to change feed location based on country Ex. "UK"
                Time, to change feed within set time limit, Ex. "Week"
                Sort, change sort order of feed, Ex. "New"
                Channel, swap reddit channel, default "r/photoshopbattles"
            """)
        elif (len(args) == 2):
            # Show Sort Options
            if (args[1] == "region"):
                print(reddit.Geo_filters)
            # Show Channel Options
            if (args[1] == "channel"):
                print("Pass a existing reddit channel name as an argument")
            # Show Time Options
            if (args[1] == "time"):
                print(reddit.Times)
            # Show Sort Options
            if (args[1] == "sort"):
                print(reddit.Sorts)
        elif (len(args) == 3):
            # Change Region
            if (args[1] == "region"):
                reddit.setFilter(args[2])
            # Change Channel
            if (args[1] in ["channel", "channle"]):
                reddit.setChannel(args[2])
            # Change Time Range
            if (args[1] == "time"):
                reddit.setTime(args[2])
            # Change Sort Range
            if (args[1] == "sort"):
                reddit.setSort(args[2])
        else:
            # Throw Exception if too many options
            print(
                f"Invalid num of arguments, User gave {len(args)}, must be 2 - 3")
        print("Dont forget to input 'refresh' after modifying settings")
    # Show current Settings
    if isSetting:
        reddit.Settings()
print("Goodbye")
