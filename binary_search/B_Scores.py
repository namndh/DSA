n, m = list(map(int, input().split(" ")))
classes_scores = [[] for i in range(n+1)]
classes = list(map(int, input().split(" ")))
scores = list(map(int, input().split(" ")))
 
for i in range(m):
    classes_scores[classes[i]].append(scores[i])
 
for i in range(n+1) :
    classes_scores[i] = sorted(classes_scores[i])
 
 
def binary_search(scores, low, high, score):
    while high - low > 1:
        mid = (high+low) // 2
        if scores[mid] > score:
            high = mid
        else:
            low = mid
    return high
 
for i in range(m):
    n = len(classes_scores[classes[i]])
    a = binary_search(classes_scores[classes[i]], -1, n, scores[i])
    b = binary_search(classes_scores[classes[i]], -1, n, scores[i]-1)
 
    print(a - b - 1, n - a)