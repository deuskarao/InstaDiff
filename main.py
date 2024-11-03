import json
import subprocess


class Main:
    def __init__(self,
                 following_list:list = [],
                 followers_list:list = [],
                 pendings_list:list = [],
                 diff:list = [],
                 get_user = input("USERNAME : ")
                 ) -> None:
        
        self.following_list = following_list
        self.followers_list = followers_list
        self.pendings_list = pendings_list
        self.diff = diff
        self.get_user = get_user
    
    def out_write(self, list_to_write, file_to_write):
        with open(file_to_write, "a") as writer:
            for x in list_to_write:
                writer.writelines(f"<a href='https://www.instagram.com/{x}'>{x}</a>\n")
            
    def get_followers(self):
        with open(f"users/{self.get_user}/in_files/followers.json", "r") as a:
            wers = json.load(a)
            
        for item in wers:
            if "string_list_data" in item:
                for string_data in item["string_list_data"]:
                    self.followers_list.append(string_data["value"])
        
        print(f"FOLLOWERS   : {len(self.followers_list)}")
    
    def get_followings(self):
        with open(f"users/{self.get_user}/in_files/followings.json", "r") as b:
            wings = json.load(b)
        
        if "relationships_following" in wings:
            for relationship in wings["relationships_following"]:
                if "string_list_data" in relationship:
                    for string_data in relationship["string_list_data"]:
                        self.following_list.append(string_data["value"])
        
        print(f"FOLLOWINGS  : {len(self.following_list)}")
    
    def get_pendings(self):
        with open(f"users/{self.get_user}/in_files/pendings.json", "r") as c:
            pendin = json.load(c)
            
        if "relationships_follow_requests_sent" in pendin:
            for request in pendin["relationships_follow_requests_sent"]:
                if "string_list_data" in request:
                    for string_data in request["string_list_data"]:
                        self.pendings_list.append(string_data["value"])
        
        print(f"PENDINGS    : {len(self.pendings_list)}")
        self.out_write(self.pendings_list, f"users/{self.get_user}/out_files/pendings.htm")
        
    def get_diff(self):
        for nick in self.following_list:
            if nick not in self.followers_list:
                self.diff.append(nick)
        
        print(f"DIFFERENCE  : {len(self.diff)}")
        self.out_write(self.diff, f"users/{self.get_user}/out_files/diff.htm")
    
    def open_files(self):
        subprocess.run(f"open users/{self.get_user}/out_files/diff.htm")
        subprocess.run(f"open users/{self.get_user}/out_files/pendings.htm")
        

if __name__ == "__main__":
    starter = Main()
    starter.get_followers()
    starter.get_followings()
    starter.get_diff()
    starter.get_pendings()
    starter.open_files()
