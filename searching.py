## Variables
inputs_so_far = 0
## Functions
def get_input(inputs_already, typeof=None):
  class String(object):
    def __init__(self, string):
      self.string = string
    def integer(self):
      try:
        return float(self.string)
      except:
        try:
          return int(self.string)
        except:
          pass
  if typeof == None:
    typeof = int
  pass
  if typeof == int:
    return typeof
  elif typeof == str:
    return String(typeof).integer()
