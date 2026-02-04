class Instagram:
    def __init__(self, title, description, creator_name, location, comments=None):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        
        if comments is None:
            self.comments = []
        else:
            self.comments = comments

    def display_title(self):
        print("The title of the reel is:", self.title)

    def display_description(self):
        print("The description of the reel is:", self.description)

    def display_creator_name(self):
        print("The creator name is:", self.creator_name)

    def display_location(self):
        print("The location is:", self.location)

    def display_likes(self):
        print("The likes of the reel are:", self.likes)

    def display_comments(self):
        print("Comments on the reel:")
        for comment in self.comments:
            print("-", comment)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)


reel1 = Instagram(
    "dancing",
    "dancing with friends",
    "Chalan",
    "Bangalore",
    ["Nice dance!", "Amazing energy"]
)

reel1.disliked()  
reel1.liked()     


reel2 = Instagram(
    "finance minister conference",
    "finance minister conference with friends",
    "John",
    "New York",
    ["Appreciated"]
)

reel1.liked()      
reel2.liked()      
reel1.disliked()   

reel1.display_likes()
reel2.display_likes()

reel1.display_creator_name()
reel1.display_location()
reel1.display_comments()

reel2.display_creator_name()
reel2.display_location()
reel2.display_comments()

print(id(reel1))
print(id(reel2))
