import re
import math


def passwordStrength(password: str):
  length = len(password)
  
  # check the character sets
  hasLower = bool(re.search(r"[a-z]",password))
  hasUpper = bool(re.search(r"[A-Z]",password))
  hasNum = bool(re.search(r"/d", password))
  hasSymbol = bool(re.search(r"[!@#$%^&*(),.?:{}|<>`~\-+_/]",password))
  
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
    
  # entropy estimate
  entropy = length * math.log2(charSpace) if charSpace > 0 else 0
  
  # estimate crack time 
  # assume 1e9 guesses per second
  guesses = charSpace ** length if charSpace > 0 else 0
  crackTimeSec = guesses / 1e9 if guesses > 0 else 0
  
  # Strength rating
  if entropy < 28:
    strength = "Very Weak"
  elif entropy < 36:
    strength = "Weak"
  elif entropy < 63:
    strength = "Reasonable"
  elif entropy < 128:
    strength = "Strong"
  else:
    strength = "Very Strong"
    
  return {
    "length": length,
    "LowercaseChars": hasLower,
    "UppercaseChars": hasUpper,
    "NumberChars": hasNum,
    "SymbolChars": hasSymbol,
    "EntropyBits": round(entropy, 2),
    "CrackTimeSeconds": crackTimeSec,
    "Strength": strength
  }
 
def displayInfo(result):
  print(f"\nPassword Length: {result['length']}")
  print(f"\nContains Lowercase: {result['LowercaseChars']}")
  print(f"\nContains Uppercase: {result['UppercaseChars']}")
  print(f"\nContains Numbers : {result['NumberChars']}")
  print(f"\nContains Symbols: {result['SymbolChars']}")
  print(f"\nEntropy: {result['EntropyBits']}")
  print(f"\nEstimated Crack time: {result['CrackTimeSeconds']}")
  print(f"\nOverall Strength: {result['Strength']}")
 
def main():
  pwd = input("Enter a password: ")
  result = passwordStrength(pwd)
  displayInfo(result)
  
if __name__ == "__main__":
  main()
  
  