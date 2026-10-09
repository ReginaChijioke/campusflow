import uuid

# These are the official choices allowed by the rules
VALID_CATEGORIES = {"Network", "Hardware", "Software", "Other"}
VALID_URGENCIES = {"Low", "Medium", "High"}


def calculate_priority(urgency, affected_users):         # Calculates ticket priority based on both info provided by user
    if urgency == "High" and affected_users >= 10:
        return "Critical"
    elif urgency == "High" or affected_users >= 10:
        return "High"
    elif urgency == "Medium" or affected_users >= 3:
        return "Medium"
    else:
        return "Low"

def create_ticket(title, category, urgency, affected_users):
    #check user inputs before creating ticket
    
    if not title or not title.strip():         # Check1: Reject empty or whitespace-only titles
        raise ValueError("Ticket title cannot be empty or whitespace-only.")
    
    if category not in VALID_CATEGORIES:       # Check2: Reject unsupported categories
        raise ValueError(f"Invalid category. Must be one of {VALID_CATEGORIES}")
 
    if urgency not in VALID_URGENCIES:          #Check3: Reject invalid urgency values
        raise ValueError(f"Invalid urgency. Must be one of {VALID_URGENCIES}")
        
    if not isinstance(affected_users, int) or affected_users <= 0:
        raise ValueError("Affected users must be a positive integer greater than zero.")   
    
    priority_level = calculate_priority(urgency, affected_users)   #using the func to calc.  priority level
    
    return {                                #Assemble and return the complete 8-key dictionary contract
        "id": str(uuid.uuid4())[:8],
        "title": title.strip(),
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority_level,
        "status": "OPEN",
        "assigned_to": None
    }
