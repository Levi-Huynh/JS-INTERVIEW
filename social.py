import random
from util import Stack, Queue
"""
nodes: users
edges: friendships
undirected: friends relationship 2 way.. Cyclic
shortest path being asked,  BFT/BFS

hint:
-Think relationships/adj list
-avg: total number for friendships / total users 
    - 10 users, 2 friends each ==> 20 total friendships 
"""


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):  # loooks like adjacency list
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            # undirectional. add friends_id here to this user_id key in friendship set
            self.friendships[user_id].add(friend_id)
            # adds friends/ user_id to this friend_id key in friendships set
            self.friendships[friend_id].add(user_id)
            # this is why we half, were creatingin bidrection for this function/ creating 2 friendships

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        # in set of self.users key is user_id, value is Username
        self.users[self.last_id] = User(name)
        # in set friendships, create a new set for the [user_id] key
        self.friendships[self.last_id] = set()

    # writing var more explicitly helps see new maneuvers
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        for i in range(num_users):
            self.add_user(f"User{i+1}")  # add a user for len of num_user arg
        possible_friendshps = []
        for user_id in self.users:  # for each id in self.user set {}
            # self.user set {} has last_id as [key]
            # 1-2, 1-3, 1-4, 1-5, 1-6, ... 1-10 ,// 2-3, 2-5, 2-6, 2-7 ..//3-4, 3-5, 3-6, 2-7
            # #becomes half of list, and one num later in range. for permutations we dont need repeats, start at next num
            # for every user_id in self.users set{}, range starts at the next user id (dont need duplicates), and range ends at the last_id +1 (since index starts 0)
            for friend_id in range(user_id + 1, self.last_id+1):
                # append the user id for each user in self.users (all users) set {}, & append its friend_id to possible
                possible_friendshps.append((user_id, friend_id))
                # ^ this is literally every possible friendship
        print("unrandom all possible", possible_friendshps)
        # random distribution, 1 users with no or few, 1 users with many
        random.shuffle(possible_friendshps)
        print("randommized order", possible_friendshps)
        # slice off right amount/ half
        # everytime creating friendship (you're creating 2 friendships)
        # slice off first 10 from list
        # create n friendships where n = avg_friendships * num_users //2
        # avg _friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users

        # half b/c for each add frienship operation we created bidirectional/2 friendships  #range here is is the average
        for i in range(num_users * avg_friendships // 2):
            # set temp var to possibl_frienships[i] (as iterates through this list)
            friendship = possible_friendshps[i]
            # add frienship(element[0], element[1]) to actualy __create__ the friendships
            self.add_friendship(friendship[0], friendship[1])
        print("halved possible random", possible_friendshps)

        # n * (n/2) = .5 * n^2 = O(n^2)

        # Add users
        # write a for loop that calls create user the right amount of times
        # Create friendships
        # create list of all poss firendship combinations
        # shuffle the list, then grab the first N elements from the list
        # youll need to import random to shuffle

    def get_mutual(user_id):
    """     
     a = [1, 2, 3, 4, 5]
        b = [1, 2, 4]

        print(all(i in a for i in b)) # Checks if all items are in the list
        print(any(i in a for i in b)) # Checks if any item is in the list
        Takes a user's user_id as an argument

      ^ for all the users in friendships set, find the shortest path between each user & the given user_id 
                        # other users, only in user_id's network, if [user_id]: {friend, friend1, friend2} 
                        # self.friendship[user_id] values are in self.friendship[other_users] 

        #iterate through self.friendship set
         friend_values = self.friendships.items()

         for k,v friend_values:    
            first_connection=friendship[user_id] #list of all user_id's direct friends (1st connection)
            mutal_friends = v.intersection(first_connection)
            if  k in first_connection:
                append/return k #this is int 
            if mutal_friends is not None:
                for elem in mutal_friends: #this is set
                    append/return mutal friends #this is integer/ element in set 

            #check elem in each friend_id's set (v)  is in mutal_friend, or their value's values are 
            in mutal friends
            if so, so, append to path that mutal, pop off the child, up to the parent  
    """
    first_connection = self.friendships[user_id]
    all_friends = self.friendships.items()
    for user, friends in all_friends:
        for friend in friends:
            return friend

    def get_all_social_paths(self, user_id):
        """

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.


        BFS

        The key is the friend's ID and the value is the path.

        visited[user_id] : [path to 1] #user_id
         """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([user_id])

        while s.size() > 0:
            path = q.dequeue()
            print("dequeue", path)
            user = path[-1]
            if user not in visited:
                print("mark user as visited", user)
                visited[user] = [path]  # create user key, path list value pair
            for mutual in self.get_mutual(user):
                pathcopy = path.copy()
                pathcopy.append(mutual)  # 1, 8, => search for mutal
                q.enqueue(mutual)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("friend", sg.friendships)
    #connections = sg.get_all_social_paths(1)
    # print(connections)
