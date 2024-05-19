#import pandas as pd


#print(pd.Series([1,2,3,4,5,6,7,8,9,10],index=[i for i in range(1,len([1,2,3,4,5,6,7,8,9,10])+1)]))
# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)

#import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

#load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df.loc[0,1])
# #print(df.loc[[0, 1]])
def user(password,username):
  print(f"welcome {username}! it's your password {password}")
d={'username': 'john', 'password': 'secret'}
print(d)
user(**d)