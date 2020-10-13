valid_hits = 0
spurious_hits = 0
# Robin-Karp Algorithm
# a - array
# p - pattern
# q - module
def robin_karp(a, p, q):
    global valid_hits, spurious_hits
    p_mod = int(p) % q
    for i in range(len(a)):
        a_mod = int(a[i:i + len(p)]) % q

        if p_mod == a_mod:
            st = i
            for j in range(len(p)):
                if a[st] != p[j]:
                    spurious_hits += 1
                    break
                st += 1

                if st - i == len(p):
                    valid_hits += 1
                    print("Pattern found at index " + str(i))


array = input("Enter the String : ")
pattern = input("Enter the pattern : ")
module_num = int(input("Enter number for module :"))

robin_karp(array, pattern, module_num)

print("\nValid Hits : " + str(valid_hits))
print(("Spurious Hits : " + str(spurious_hits)))





