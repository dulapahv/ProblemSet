def is_subset(sub, sup):
    for element in sub:
        if element not in sup:
            return False
    return True

sup = set([1, 2, 3, 4])
sub = set([1, 2, 4])
print(is_subset(sub, sup))

sub = set([1, 2, 5])
print(is_subset(sub, sup))