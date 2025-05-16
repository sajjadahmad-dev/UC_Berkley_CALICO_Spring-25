import sys
import threading

def main():
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        blocks = [{'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'mass': (x1 - x0) * (y1 - y0), 'cx': (x0 + x1) / 2, 'cy': (y0 + y1) / 2} for _ in range(N) for x0, y0, x1, y1 in [map(int, sys.stdin.readline().split())]]
        
        parent, children = [-1] * N, [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j and blocks[i]['y0'] == blocks[j]['y1'] and not (blocks[i]['x1'] <= blocks[j]['x0'] or blocks[i]['x0'] >= blocks[j]['x1']):
                    parent[i], children[j] = j, children[j] + [i]
                    break
        
        stable = True
        def dfs(u):
            nonlocal stable
            total_mass, total_cx, total_cy = blocks[u]['mass'], blocks[u]['mass'] * blocks[u]['cx'], blocks[u]['mass'] * blocks[u]['cy']
            for v in children[u]:
                m, cx, cy = dfs(v)
                total_mass, total_cx, total_cy = total_mass + m, total_cx + m * cx, total_cy + m * cy
            if parent[u] != -1 and not (blocks[parent[u]]['x0'] <= total_cx / total_mass <= blocks[parent[u]]['x1']):
                stable = False
            return total_mass, total_cx / total_mass, total_cy / total_mass
        
        for i in range(N):
            if parent[i] == -1 and blocks[i]['y0'] == 0:
                dfs(i)
        
        print("Stable" if stable else "Unstable")

threading.Thread(target=main).start()