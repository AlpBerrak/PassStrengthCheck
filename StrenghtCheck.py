import re
import math


def passwordStrength(password: str):
  length = len(password)
  
  # check the character sets
  hasLower = bool(re.serach(r"[a-z]",password))
  hasUpper = bool(re.search(r"[A-Z]",password))
  hasNum = bool(re.search(r"/d", password))
  hasSymbol = bool(re.search(r"[!@#$%^&*(),.?:{}|<>`~-+_/]",password))
  
  # calculate character space from sets
  charSpace = 0
  
  if hasLower:
    charSpace += 26
  if hasUpper:
    charSpace += 26
  if hasNum:
    charSpace += 10
  if hasSymbol:
    charSpace += 25
  