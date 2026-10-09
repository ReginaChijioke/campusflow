from workflow import assign_ticket 
ticket_list = [
    {
        "id": 1,
        "title": "Cannot connect to campus Wi-Fi",
        "category": "Network",
        "urgency": "high",
        "affected_users": 15,
        "priority": "critical",
        "status": "open",
        "assigned_to": None
    },
    {
        "id": 2,
        "title": "Printer not working",
        "category": "Hardware",
        "urgency": "medium",
        "affected_users": 2,
        "priority": "low",
        "status": "open",
        "assigned_to": None
    },
    {
        "id": 3,
        "title": "Unable to access student portal",
        "category": "Software",
        "urgency": "high",
        "affected_users": 8,
        "priority": "high",
        "status": "open",
        "assigned_to": "Ada"
    }
]
assign_ticket(ticket_list, 1, "    ")
print(assign_ticket(ticket_list, 1, "    "))
print(ticket_list)