import Ticket
import Menu

menu = Menu.Menu_List
Ticket_List = []

while True:
  option = menu.Menu()

  if option == 0:
    print("Thank you for using IT helpdesk system =)")
    break

  elif option == 1:
    while True:
      id = input("Enter your staff ID: ")
      name = input("Enter your name: ")
      email = input("Enter your email: ")
      print("if you require a new password type: Password change")
      description = input("Enter description of problem: ")
      ticket = Ticket.Ticket(id, name, email, description)
      if description == "Password change":
        ticket.closed()
        print("Your new password is", menu.PasswordGenerator(ticket))
      else:
        print("Ticket has been submitted to the helpdesk queue")
      Ticket_List.append(ticket)
      answer = input("Do you have another problem to submit? (Y/N)")
      if answer != 'Y':
        break

  elif option == 2:
    for i in range(len(Ticket_List)):
      response = "Not Yet Provided"
      print("-------------------------------------------")
      print("Ticket Number:", Ticket_List[i].number)
      print("Ticket Creator:", Ticket_List[i].name)
      print("Staff ID:", Ticket_List[i].id)
      print("Email Address:", Ticket_List[i].email)
      print("Description:", Ticket_List[i].description)
      if Ticket_List[i].description == "Password change":
        response = "New password generated: "+menu.PasswordGenerator(Ticket_List[i])
      print("Response:", response)
      print("Ticket Status:", Ticket_List[i].status)
    print("-------------------------------------------")

  elif option == 3:
    ticket_number = int(input("Enter your ticket number: "))
    found = False
    for i in range(len(Ticket_List)):
      if Ticket_List[i].number == ticket_number:
        found = True
        if Ticket_List[i].description == "Password change":
          response = "New password generated: "+menu.PasswordGenerator(Ticket_List[i])
        else:
          response = "Not Yet Provided"
    if found:
      print("Response:", response)
    else:
      print("This ticket number cannot be found")

  elif option == 4:
    ticket_number = int(input("Enter your ticket number: "))
    state = 0
    for i in range(len(Ticket_List)):
      if Ticket_List[i].number == ticket_number:
        if Ticket_List[i].status == "Closed":
          state = 1
          Ticket_List[i].reopened()
        else:
          state = 2
    if state == 1:
      print("Re-open successful")
    elif state == 2:
      print("This ticket is still open")
    else:
      print("This ticket number cannot be found")

  elif option == 5:
    print("Displaying ticket statistics")
    print("-------------------------------------------")
    submitted, resolved, open = Ticket.Ticket.Stats()
    print("Tickets Created:", submitted)
    print("Tickets Resolved:", resolved)
    print("Tickets To Solve:", open)
    print("-------------------------------------------")

  else:
    print("Invalid menu selection!")
    print("Please try again")