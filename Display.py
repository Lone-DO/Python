from ConvertTime import ConvertTime

def Display(data):
    index = 0
    children = data["data"]["children"]
    for child in children:
        data = child.get("data")
        
        Name = data.get("name") #Pass Last child to Pages Array
        Title =  data.get("title")
        Author =  data.get("author")
        ID =  data.get("id")
        # Url =  data.get("url")
        Link = data.get("permalink")
        Created =  data.get("created")
        # Thumbnail =  data.get("title")
        Score =  data.get("score")
        numComments =  data.get("num_comments")
        Domain = data.get("domain")
        Prefix = data.get("subreddit_name_prefixed")
        if Name is not None:
            Body = f"""
            [{index}] {Title} ({Domain})
            submitted {ConvertTime(Created)} by u/{Author} to {Prefix}
            {Score} upvotes with {CommentCount(numComments)} comments
            """
            print (Body)
        index += 1
       

def CommentCount(integer):
    if integer <= 0: return "no"
    else: return integer