import re
import math


def passwordStrength(password: str):
  length = len(password)
  
  # check the character sets
  hasLower = bool(re.serach(r"[a-z]",password))
  hasUpper = bool(re.search(r"[A-Z]",password))
  hasNum = bool(re.search(r"/d", password))
  has_symbol = bool(re.search(r"[!@#$%^&*(),.?:{}|<>]",password))
  