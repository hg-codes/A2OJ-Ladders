import sys
sys.setrecursionlimit(2000)

def solve():
    s = input()
    m = int(input())
    
    wei = [i + 1 for i, ch in enumerate(s) if ch == '1']
    visited = set()
    path = []

    def dfs(bal, last_w, step):
        if step > m:
            return True
        
        state = (bal, last_w, step)
        if state in visited:
            return False
        
        is_odd = (step % 2 != 0)
        for w in wei:
            if w == last_w: continue
            
            new_bal = bal + w if is_odd else bal - w
            if is_odd and 0 < new_bal <= 10:
                path.append(w)
                if dfs(new_bal, w, step + 1):
                    return True
                path.pop()
            elif not is_odd and -10 <= new_bal < 0:
                path.append(w)
                if dfs(new_bal, w, step + 1):
                    return True
                path.pop()
        
        visited.add(state)
        return False

    if dfs(0, 0, 1):
        print("YES")
        print(*(path))
    else:
        print("NO")

if __name__ == '__main__':
    solve()