# Author: Cui Qiaoxu qfc5036@psu.edu
# Collaborator: John O'Toole Jbo5232@psu.edu
# Collaborator: Ching-Ju Chen cxc6001@psu.edu
# Section: 8
# Breakout: 11
def getlettergrade(numbergrade):
  if numbergrade >= 93.0:
    lettergrade = "A"
  elif numbergrade >= 90.0:
    lettergrade = "A-"
  elif 90 >= numbergrade >= 87.0:
    lettergrade = "B+"
  elif 87 > numbergrade >= 83.0:
   lettergrade = "B"
  elif 83 > numbergrade >= 80:
   lettergrade = "B-"
  elif 80 > numbergrade >= 77:
   lettergrade = "C+"
  elif 77 > numbergrade >= 70:
   lettergrade = "C"
  elif 70 > numbergrade >= 60:
   lettergrade = "D"
  elif 60 > numbergrade >= 0:
   lettergrade = "F"
  return lettergrade

def run():
 numbergrade = float(input("Enter your CMPSC 131 grade: "))
 print(f"Your letter grade for CMPSC 131 is {getlettergrade(numbergrade)}.")

if __name__ == "__main__":
  run()