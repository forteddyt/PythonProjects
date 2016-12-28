# Definer.py should be in the same directory as Poller.py
# Definer should only be run manually
# Definer is used to define what search_topics and their search terms
# Definer edits the base.txt file, line 2

import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" # Obtains the scripts file path
