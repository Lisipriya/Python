
def format_name(first_name, last_name):
  formatted_firstname = first_name.title() 
  formatted_lastname = last_name.title()
  return f"{formatted_firstname} {formatted_lastname}"

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(format_name(first_name, last_name))
