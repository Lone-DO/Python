import data
from Display import Display

reddit = data.client()


def start():
    reddit.fetch()
    Display('page', reddit.data)


start()

while True:
    print("""Welcome to the Reddit Console Client
    Enter --help for list of options
    Enjoy
    """)
    userInput = input("\t$")
    args = userInput.lower().split(" ")
    hasArgs = len(args) > 1 and args[1]
    isLoad = args[0] == "load"
    isList = args[0] == "list"
    isOption = args[0] == "option"
    data = reddit.data["data"]["children"]

    def getChild(num): return data[num].get("data")["name"]

    if (userInput.lower() in ["q", "quit", "exit", "terminate", "close"]):
        break

    if (isLoad):
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

    if (isList):
        if (hasArgs and args[1].lower() in ["help", "-help", "--help", "-h", "--h"]):
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
            index = int(args[1])
            if index < len(Display.list):
                reddit.fetchComments(Display.list[index])
                Display('post', reddit.comments)
            elif index >= len(Display.list):
                print("Page Unavailable, Please try again")
        else:
            print(Display.list)


print("Goodbye")
