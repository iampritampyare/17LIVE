Create an input.json file with the input data in JSON format
Run the script using: python file_name.py
Check the output in output.json


Test Cases
The solution should handle these key cases:

Streams repeated within the same section
Streams appearing in the top 3 positions of multiple sections
Sections with fewer than 3 streams
Cases where no valid replacements are available


Limitations
This is an intentionally naive approach that prioritizes simplicity over efficiency. Some limitations:

It may not find the optimal solution when there are many duplicates across sections
If no replacements are found, some duplicates may remain in the top 3 positions
The approach is sequential and doesn't try to find a globally optimal solution


If needed, the solution could be enhanced by:

Using a more sophisticated algorithm to find optimal replacements
Adding comprehensive error handling and validation
Better handling edge cases where duplicates cannot be resolved
Adding detailed logging for debugging and monitoring