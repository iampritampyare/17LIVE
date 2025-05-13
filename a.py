import json

def deduplicate_streams(input_json):
    """
    Deduplicate streams in the top 3 positions across different sections.
    
    Args:
        input_json (str): JSON string containing sections and their streams
        
    Returns:
        str: JSON string with deduplicated streams
    """
    # Parse the input JSON
    sections = json.loads(input_json)
    
    # Result dictionary to store the deduplicated streams by section
    result = {}
    
    # Set to track streams already used in top 3 positions
    top_streams_used = set()
    
    # First pass: Create the basic structure and prepare the data
    for section in sections:
        section_id = section["sectionID"]
        streams = []
        
        # Extract streamer IDs from the section data
        for streamer in section["sectionData"]:
            streams.append(streamer["streamerID"])
            
        # Store in result with section ID as key
        result[section_id] = streams
    
    # Second pass: Handle duplicates in top 3 positions across sections
    for section in sections:
        section_id = section["sectionID"]
        current_streams = result[section_id]
        
        # Create a new list for deduplicated streams
        deduplicated_streams = []
        
        # Process top 3 positions (or fewer if section has less than 3 streams)
        top_count = 0
        index = 0
        
        # Process the top 3 positions
        while top_count < 3 and index < len(current_streams):
            current_stream = current_streams[index]
            
            # If this stream is already used in top 3 of another section
            if current_stream in top_streams_used:
                # Look for a replacement from later in the list
                found_replacement = False
                
                # Try to find a replacement from position 3 onwards
                for i in range(3, len(current_streams)):
                    potential_replacement = current_streams[i]
                    
                    # If this stream is not already in top 3 of any section
                    if potential_replacement not in top_streams_used:
                        # Use this replacement
                        deduplicated_streams.append(potential_replacement)
                        top_streams_used.add(potential_replacement)
                        found_replacement = True
                        break
                
                # If no replacement found, use the original stream
                # This is a fallback when we can't find any suitable replacement
                if not found_replacement:
                    deduplicated_streams.append(current_stream)
            else:
                # This stream is not used in top 3 of any section, so use it
                deduplicated_streams.append(current_stream)
                top_streams_used.add(current_stream)
            
            top_count += 1
            index += 1
        
        # Add remaining streams (after top 3)
        for i in range(index, len(current_streams)):
            # Skip streams already included in our deduplicated list
            if current_streams[i] not in deduplicated_streams:
                deduplicated_streams.append(current_streams[i])
        
        # Update the result with deduplicated streams
        result[section_id] = deduplicated_streams
    
    # Return the deduplicated result as a JSON string
    return json.dumps(result, indent=2)

def main():
    try:
        # Read input JSON file
        with open('input.json', 'r') as file:
            input_json = file.read()
        
        # Process the streams to remove duplicates in top 3 positions
        output_json = deduplicate_streams(input_json)
        
        # Write the result to an output file
        with open('output.json', 'w') as file:
            file.write(output_json)
        
        print("Processing complete. Output written to output.json")
        
    except FileNotFoundError:
        print("Input file not found. Please create an input.json file.")
    except json.JSONDecodeError:
        print("Invalid JSON format in input file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()