# class User:
#     def __init__(self,user_id,user_name):
#         self.id=user_id
#         self.username=user_name
#         self.follower=0
#
#
# # user_1=User()
# # user_1.id="001"
# # user_1.username="angla"
# # print(user_1.username)
# user_1=User("001","angela")
# print(user_1.username)



# class Name:
#     pass
# user3=Name()
# user3.id="001"
# user22=Name()
# user22.id="022"
# user3.name="kevin"
# print(user3.id)


class Name:
        def __init__(self,user_id,name):
            self.id=user_id
            self.name=name
            self.follower=0
            self.following=0
        def follow(self,user):
            user.follower+=1
            self.following+=1


user_1 = Name("003","kevin")
user_2 = Name("004","Angla")

user_1.follow(user_2)
print(user_1.following)
print(user_1.follower)
print(user_2.following)
print(user_2.follower)
