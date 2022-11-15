class Ticket(object):
    count_number = 0
    count_submitted = 0
    count_resolved = 0
    count_open = 0

    def __init__(self, id, name, email, description):
        Ticket.count_number = Ticket.count_number + 1
        self.number = 2000 + Ticket.count_number
        self.id = id
        self.name = name
        self.email = email
        self.description = description
        self.opened()
        Ticket.count_submitted = Ticket.count_submitted + 1

    def Stats():
        return Ticket.count_submitted, Ticket.count_resolved, Ticket.count_open

    def opened(self):
        Ticket.count_open = Ticket.count_open + 1
        self.status = "Open"

    def reopened(self):
        Ticket.count_resolved = Ticket.count_resolved - 1
        Ticket.count_open = Ticket.count_open + 1
        self.status = "Reopened"

    def closed(self):
        Ticket.count_open = Ticket.count_open - 1
        Ticket.count_resolved = Ticket.count_resolved + 1
        self.status = "Closed"
