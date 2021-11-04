people = input()
n = len(people)
double_people = " "
double_people += people*2
psa = [0] * (2*n+1)
psb = [0] * (2*n+1)
psc = [0] * (2*n+1)
for i in range(1, 2*n+1):
    psa[i] += psa[i-1]
    psb[i] += psb[i-1]
    psc[i] += psc[i-1]
    if double_people[i] == "A":
        psa[i] += 1
    elif double_people[i] == "B":
        psb[i] += 1
    elif double_people[i] == "C":
        psc[i] += 1
 
min_swap = float("INF")
 
na = psa[n] 
nb = psb[n]
nc = psc[n]
 
for i in range(1, n+1):
    swap_a = psa[n] - (psa[i+na-1] - psa[i-1])
    swap_b = psb[n] - (psb[i+na+nb-1] - psb[i+na-1])
    swap_c = psc[n] - (psc[i+na+nc-1] - psc[i+na-1])
    swap_a_in_b = psa[i+na+nb-1] - psa[i+na-1]
    swap_a_in_c = psa[i+na+nc-1] - psa[i+na-1]
    swap_b_in_a = psb[i+na-1] - psb[i-1]
    swap_c_in_a = psc[i+na-1] - psc[i-1]
    
    min_swap = min(min_swap, 
                swap_a+swap_b-min(swap_a_in_b, swap_b_in_a), 
                swap_a+swap_c-min(swap_a_in_c, swap_c_in_a)
                )
print(min_swap)
 