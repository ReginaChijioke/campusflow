def assign_ticket(ticket_list, ticket_id, worker_name):
    if worker_name is None or not worker_name.strip():
        return None
    for ticket in ticket_list:
        if ticket["id"] == ticket_id:
            ticket["assigned_to"] = worker_name.strip() 
            return True
    return None   

