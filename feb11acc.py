#make list
accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455",
"xjhd53e", "45da", "de37dp"]
#contains number 5
for acc in accs:
    if re.search(r"5", acc):
        print("\t" + acc)
#contain letter d or e
for acc in accs:
    if re.search(r"(e|d)", acc):
        print("\t" + acc)
#contain letters d and e in that order
for acc in accs:
    if re.search(r"e.*d", acc):
        print("\t"+acc)
#contain the letters d and e in that order with a single letter between them
for acc in accs:
    if re.search(r"e.d", acc):
        print("\t"+acc)
#contain both the letters d and e in any order
for acc in accs:
    if re.search(r"e.*d|d.*e", acc):
        print("\t"+acc)
#start with x or y
for acc in accs:
    if re.search(r"^(x|y)", acc):
        print("\t" + acc)
#start with x or y and end with e
for acc in accs:
    if re.search(r"^(x|y).*e$", acc):
        print("\t" + acc)
#contain three or more numbers in a row
for acc in accs:
    if re.search(r"\d{3,}", acc):
        print("\t" + acc)
#end with d followed by either a, r or p
for acc in accs:
    if re.search(r"d[arp]$", acc):
        print("\t" + acc)