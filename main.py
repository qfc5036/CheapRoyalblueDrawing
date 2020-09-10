# Author: Cui Qiaoxu qfc5036@psu.edu
# Collaborator: John O'Toole Jbo5232@psu.edu
# Collaborator: Ching-Ju Chen cxc6001@psu.edu
# Section: 8
# Breakout: 11
def getlettergrade(numbergrade):
  numbergrade = float(numbergrade)
  if numbergrade >= 93.0:
    out = "A"
  elif numbergrade >= 90.0:
    out = "A-"
  elif 90 >= numbergrade >= 87.0:
    out = "B+"
  elif 87 > numbergrade >= 83.0:
    out = "B"
  elif 83 > numbergrade >= 80:
    out = "B-"
  elif 80 > numbergrade >= 77:
    out = "C+"
  elif 77 > numbergrade >= 70:
    out = "C"
  elif 70 > numbergrade >= 60:
    out = "D"
  else:
    out = "F"
  return out

def run():
 numbergrade = float(input("Enter your CMPSC 131 grade: "))
 print(f"Your letter grade for CMPSC 131 is {getlettergrade(numbergrade)}.")

if __name__ == "__main__":
  run()