table = [["The", "Quick", "Brown"], ["Fox", "Jumps", "Over"], ["The", "Lazy", "Dog"]]
ans = ""
for row in table:
    for i in range(len(row)-1):
        if len(row[i]) < len(row[i+1]):
            ans = ans + row[i]
        else:
            ans = ans + row[i+1]
print(ans)