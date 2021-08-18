usin = int(input("How many seconds have passed? "))
second = usin % 60
minute = (usin // 60) % 60
hour = (usin // 3600)
print(f"That is equal to {hour} hour(s) {minute} minute(s) and {second} second(s).")