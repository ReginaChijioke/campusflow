import unittest
from campusflow.tickets import create_ticket, calculate_priority   #import function from campusflow 

class TestTicketCreationAndValidation(unittest.TestCase):

    def test_valid_ticket_creation(self):                #  Test that a perfectly valid input successfully builds a ticket dictionary.                                
        ticket = create_ticket("Dorm 3 Wi-Fi is completely down", "Network", "High", 15)
        self.assertEqual(ticket["title"], "Dorm 3 Wi-Fi is completely down")
        self.assertEqual(ticket["status"], "OPEN")
        self.assertIsNone(ticket["assigned_to"])

    def test_empty_title_rejection(self):
        with self.assertRaises(ValueError):
            create_ticket("   ", "Network", "High", 5)

    def test_invalid_category_rejection(self):
        """Reject unapproved categories."""
        with self.assertRaises(ValueError):
            create_ticket("Broken chair", "Furniture", "Low", 1)

    def test_non_positive_users_rejection(self):
        """Reject zero or negative user counts."""
        with self.assertRaises(ValueError):
            create_ticket("Server fire", "Hardware", "High", 0)

    def test_priority_matrix_hierarchy(self):
        """Verify the exact order of operations for priority rules."""
        self.assertEqual(calculate_priority("High", 12), "Critical")
        self.assertEqual(calculate_priority("High", 5), "High")
        self.assertEqual(calculate_priority("Medium", 2), "Medium")
        self.assertEqual(calculate_priority("Low", 1), "Low")

if __name__ == "__main__":
    unittest.main()                                                                                                                         
