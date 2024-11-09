import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendees, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )
        
    output_filename = f"output_{index}.txt"
    
    if os.path.exists(output_filename):
        print(f"Warning: {output_filename} already exists. It will be overwritten.")
        
    try:
        with open(output_filename, "w") as file:
            file.write(invitation)
        print(f"Generated invitation: {output_filename}")
    except Exception as e:
        print(f"Error writing file {output_filename}: {e}")