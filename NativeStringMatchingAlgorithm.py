# Native String Matching Algorithm
def nativeStringMatching(string, pattern):
    n = len(string)
    m = len(pattern)
    no_of_matching = 0

    for i in range(n):
        st = i
        no_of_matching += 1

        for j in range(m):
            if string[st] != pattern[j]:
                no_of_matching -= 1
                break
            st += 1

    return no_of_matching


#Get user inputs
string = str(input("Enter the String : "))
pattern = str(input("Enter the pattern : "))

matching = nativeStringMatching(string, pattern)

print("\nNo of Matching : " + str(matching))
