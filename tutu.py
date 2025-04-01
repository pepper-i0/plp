# Books = ('who moved my cheese', 'act of war', 'think big', 'purple hibiscus', 'americana')
# for book in Books:
#     print(book)

# user_details = input({"name":"", "age":"", "favorite food":"", "school":""})
# print(f'student information: {user_details}')

# user={'name':'', 'age':'', 'favorite color':''}
# user['name'] = input("Enter your name: ")
# user["age"]= input("Enter your age: ")
# user["favorite color"]= input("Enter your favorite color: ")
# print(f'user info: {user}')
# print(f'hello {user["name"]}')

def digit():
    return set
digits = set(map(int, input('enter first set:').split()))
digits_2 = set(map(int, input('enter second set:').split()))
print(f'common numbers are:', (digits).intersection(digits_2))