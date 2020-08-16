import instagramBot

action=input("Select action:\n 1-Follow \n 2-Unfollow\n")
if (int(action)==1):
    page=input("Enter the username that you want to follow it's followers:")
    followcount=input("Enter how many users you want to follow:")
    instagramBot.follow(page,int(followcount))
elif(int(action)==2):
    unfollowcount=input("Enter how many users you want to unfollow:")
    instagramBot.unfollow(int(unfollowcount))
else:
    print("Enter 1 or 2")
    
