from ConvertTime import ConvertTime
from tqdm import tqdm

class Display:
    data = []
    list = []

    def setData(self, data):
        self.data = data
        self.show("page", self.data)

    def setList(self, data):
        self.list = data
        # print(self.list)

    def getList(self):
        return self.list

    def loop(self, call, data):
        items = []
        for index, child in tqdm(enumerate(data, 0), total=len(data)):
            data = child.get("data")
            Name = data.get("name")  # Pass Last child to Pages Array
            Title = data.get("title")
            Author = data.get("author")
            # ID = data.get("id")
            # Url = data.get("url")
            Link = data.get("permalink")
            Created = data.get("created")
            # Thumbnail =  data.get("title")
            Score = data.get("score")
            numComments = data.get("num_comments")
            Domain = data.get("domain")
            Prefix = data.get("subreddit_name_prefixed")
            Name = data.get("name")
            Title = data.get("title")
            Text = data.get("selftext")

            if Name is not None:
                if call == "posts":
                    # if self.getList() and index == 0:
                    #     self.list = []
                    #     print(f"Clearing list, {self.list}")

                    print(f"""
                    [{index}] {Title} ({Domain})
                    submitted {ConvertTime(Created)} by u/{Author} to {Prefix}
                    {Score} upvotes with {self.CommentCount(numComments)} comments
                    Link: {Link}
                    """)
                    items.append(Link)
                if call == "post":
                    # print("Loading post")
                    print(f"""
                    Title: {Title}
                    Text: {Text}
                """)
                if call == "comments":
                    print("Rendering Comments")
        return items

    def show(self, call, data):
        if call == 'page':
            children = data["data"]["children"]
            self.setList(self.loop('posts', children))

        elif (call == "post"):
            children = data[0]["data"]["children"]
            self.loop('post', children)

    def CommentCount(self, integer):
        if integer <= 0:
            return "no"
        else:
            return integer
