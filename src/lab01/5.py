FCS = input()
initials = ""
len_FCS = len(FCS)
k = len_FCS - FCS.count(" ")
if FCS[0] != " ":
    initials += FCS[0]
for i in range(1, len_FCS):
    if FCS[i] != " " and FCS[i - 1] == " ":
        initials += FCS[i]
print(initials)
print(k + 2)
