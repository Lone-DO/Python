import data

from Display import Display

Leave = ["q", "quit", "exit", "terminate", "close"]
reddit = data.client()

reddit.fetch()

while True:
    print("""Welcome to the Reddit Console Client
    Enter --help for list of options
    Enjoy
    """)
    userInput = input("\t")
    args = userInput.lower().split(" ")

    if (userInput.lower() in Leave):
        break
    if (args[0] == "load"):
        Display('page', reddit.data)
    if (args[0] == "list"):
        if len(args) > 1 and args[1]:
            index = int(args[1])
            if index < len(Display.list):
                reddit.fetchComments(Display.list[index])
                Display('post', reddit.comments)
            elif index >= len(Display.list):
                print("Page Unavailable, Please try again")
        else:
            print(Display.list)
print("Goodbye")
