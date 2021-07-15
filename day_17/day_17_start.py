class User:
    
    def __init__(self,id, username):
        self.id = id
        self.username = username
        self.follower = 0
        
user_1 = User("001", "Siddhesh")
user_2 = User("002", "Teju")
user_3 = User("003", "Shardul")

for i in [user_1, user_2, user_3]:
    print(i.username)
