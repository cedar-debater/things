## Variables
inputs_so_far = 0
## Functions
def get_input(prompt, inputs_already):
  class String(object):
    def __init__(self, string):
      self.string = string
    def integer(self):
      try:
        return int(float(self.string))
      except:
        try:
          return int(self.string)
        except:
          raise ValueError("Invalid content in self.string")
    def __str__(self):
      return self.string
  typeof = raw_input(prompt)
  try:
    return [String(typeof).integer()+1, typeof]
  except:
    the_list = list(str(String(typeof)))
    the_list.pop()
    the_list.pop()
    return ["".join(the_list), typeof]
    
## How to use get_input():
## a_list = get_input(<put prompt here>, inputs_so_far)
## inputs_so_far = a_list[0]
## user_returned_text = a_list[1]

## Input and Output
while True:
  a_list = get_input("Welcome to the searching page. To search, type something in!", inputs_so_far)
  inputs_so_far = a_list[0]
  text = a_list[1]
