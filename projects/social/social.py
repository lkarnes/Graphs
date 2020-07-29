
import random

class User:
    def __init__(self, name):
        self.name = name
        
class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        # this is your adjacency list representation of a graph
        self.friendships = {}
    def add_friendship(self, user_id, friend_id):
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
    def add_user(self, name):
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        
        
    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]
            
            
    def populate_graph(self, num_users, avg_friendships):
        
        
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for user in range(num_users):
            self.add_user(user)
            # starts at 1, up to and including num_users
        # * Hint 1: To create N random friendships, 
        # you could create a list with all possible friendship combinations of user ids, 
        
        friendship_combinations = []
        # O(n^2)
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                friendship_combinations.append((user, friend))
                
        # shuffle the list
        self.fisher_yates_shuffle(friendship_combinations)
        
        # then grab the first N elements from the list. 
        total_friendships = num_users * avg_friendships
        
        friends_to_make = friendship_combinations[:(total_friendships // 2)]
        
        # Create friendships
        for friendship in friends_to_make:
            self.add_friendship(friendship[0], friendship[1])
            
    def get_all_social_paths(self, user_id):
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
