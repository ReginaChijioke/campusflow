import unittest
from campusflow.tickets import create_ticket, calculate_priority   #import function from campusflow 

class TestTicketCreationAndValidation(unittest.TestCase):

    def test_valid_ticket_creation(self):                #  Test that a perfectly valid input successfully builds a ticket dictionary.                                
        empty_list = []
        emptyticket = create_ticket(empty_list, "Cluster 3 Wi-Fi is completely down", "Network", "high", 15)
        self.assertEqual(emptyticket["title"], "Cluster 3 Wi-Fi is completely down")
        self.assertEqual(emptyticket["status"], "open")
        self.assertIsNone(emptyticket["assigned_to"])

    def test_empty_title_rejection(self):
        empty_list = []
        with self.assertRaises(ValueError):
            create_ticket(empty_list, "   ", "Network", "high", 5)

    def test_invalid_category_rejection(self):
        empty_list = []
        with self.assertRaises(ValueError):
            create_ticket(empty_list, "Broken chair", "Furniture", "low", 1)

    def test_non_positive_users_rejection(self):
        empty_list = []
        with self.assertRaises(ValueError):
            create_ticket(empty_list, "Server fire", "Hardware", "high", 0)

    def test_priority_matrix_hierarchy(self):        
        #Verify the exact order of operations for priority rules       
        self.assertEqual(calculate_priority("high", 12), "critical")
        self.assertEqual(calculate_priority("high", 5), "high")
        self.assertEqual(calculate_priority("medium", 2), "medium")
        self.assertEqual(calculate_priority("low", 1), "low")

# ID sequencing tests
    def test_id_empty_list_gives_t001(self):
        existing_tickets = []
        ticket = create_ticket(existing_tickets, "Wi-Fi is down", "Network", "high", 5)
        self.assertEqual(ticket["id"], "T001")

    def test_id_sequential_generation(self):        #A second ticket created after the first one is appended gets T002.
        existing_tickets = []
          # Create and append the first ticket
        ticket1 = create_ticket(existing_tickets, "Wi-Fi down", "Network", "high", 5)
        existing_tickets.append(ticket1)
        # Create the second ticket passing the updated list
        ticket2 = create_ticket(existing_tickets, "Keyboard broken", "Hardware", "medium", 1)
        self.assertEqual(ticket2["id"], "T002")
    
    def test_id_skips_to_next_highest(self):        #A hand-built list with the highest ID T005 gives T006.
    
        existing_tickets = [    
        {"id": "T001", "title": "Old Ticket 1"},
        {"id": "T005", "title": "Old Ticket 5"},
        {"id": "T003", "title": "Old Ticket 3"}
        ]
        ticket = create_ticket(existing_tickets, "New Bug", "Software", "low", 1)
        self.assertEqual(ticket["id"], "T006")


if __name__ == "__main__":
    unittest.main()                                                                                                                         
