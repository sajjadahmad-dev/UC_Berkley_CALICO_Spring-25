import sys
import threading
sys.setrecursionlimit(1 << 25)
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        blocks = [] 
        for _ in range(N):
            X0, Y0, X1, Y1 = map(int, sys.stdin.readline().split())
            mass = (X1 - X0) * (Y1 - Y0)
            cx = (X0 + X1) / 2
            cy = (Y0 + Y1) / 2
            blocks.append({'X0': X0, 'Y0': Y0, 'X1': X1, 'Y1': Y1, 'mass': mass, 'cx': cx, 'cy': cy})
        
        parent = [-1] * N  
        children = [[] for _ in range(N)] 
        
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if blocks[i]['Y0'] == blocks[j]['Y1']:  
                    if not (blocks[i]['X1'] <= blocks[j]['X0'] or blocks[i]['X0'] >= blocks[j]['X1']):
                        parent[i] = j
                        children[j].append(i)
                        break
        
        stable = True
        
        def dfs(u):
            nonlocal stable
            total_mass = blocks[u]['mass']
            total_cx = blocks[u]['mass'] * blocks[u]['cx']
            total_cy = blocks[u]['mass'] * blocks[u]['cy']
            
            for v in children[u]:
                m, cx, cy = dfs(v)
                total_mass += m
                total_cx += m * cx
                total_cy += m * cy
            
            if parent[u] != -1: 
                p = parent[u]
                center_x = total_cx / total_mass
                if not (blocks[p]['X0'] <= center_x <= blocks[p]['X1']):
                    stable = False
            
            return total_mass, total_cx / total_mass, total_cy / total_mass
        
        for i in range(N):
            if parent[i] == -1 and blocks[i]['Y0'] == 0:
                dfs(i)
        
        print("Stable" if stable else "Unstable")

threading.Thread(target=main).start()