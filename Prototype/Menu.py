# This class contains menu text and password change function
class Menu_List(object):

  def __init__():
    pass

# Function generates a new user password
  def PasswordGenerator(ticket):
    return ticket.id[0:2]+ticket.name[0:3]

# Displays menu options and input prompt
  def Menu():
    print("-------------------------------------------")
    print("Select from the following choices:")
    print("0: Exit")
    print("1: Submit helpdesk ticket")
    print("2: Show all tickets")
    print("3: Respond to ticket by number")
    print("4: Re-open resolved ticket")
    print("5: Display ticket stats")
    print("-------------------------------------------")
    option = int(input("Enter menu selection 0 - 5 : "))
    return option
