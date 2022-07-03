n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
n = list(map(str, n))
#answer = '('
# for i in n[:3]:
#    answer += i
#answer += ') '
# for i in n[3:6]:
#    answer += i
#answer += '-'
# for i in n[6:]:
#    answer += i
print("("+"".join(a for a in n[:3])+") " +
      "".join(b for b in n[3:6])+"-"+"".join(c for c in n[6:]))
