for num in range(2, 101):
    eh_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(num, end=" ")
print()