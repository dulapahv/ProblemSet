def find_dup(ListInput):
    if len(ListInput) == len(set(ListInput)):
        return "yes"
    else:
        return "no"


usin = input().split()
print(find_dup(usin))
