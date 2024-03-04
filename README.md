# oms-one
Components of a modern order managment system

## Starter set. Backend view
1. Users table:
    1. ID
    2. Firm
    3. Member_since
2. User events table:
    1. Event ID
    2. Timestamp
    3. Event type
    4. External or master ID
    5. Originator ID
    6. Target ID
Example: An RFQ event: event_id = ABCD, time = 2024_03_4_10_28_35, event_type = RFQ_initital_inquiry, master_id = 1, origantor = Alice,
target = Bob. Here it is imprtant to note, that there is only one target. Events addressed to a group, such as an RFQ inquiry, will be split into individual inquiries and linked by their external ids.        
