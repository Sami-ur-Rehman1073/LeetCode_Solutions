def categorizeBox(length, width, height, mass):
    volume = length * width * height
    bulky = False
    heavy = False

    if ((length >= 10**4) or (width >= 10**4) or (height >= 10**4)) or (volume >= 10**9):
        bulky = True
    
    if mass >= 100:
        heavy = True

    if bulky and heavy:
        return "Both"
    if not bulky and not heavy:
        return "Neither"
    if bulky:
        return "Bulky"
    if heavy:
        return "Heavy"
    
print(categorizeBox(1000, 35, 700, 300))
        