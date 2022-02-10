from sys import stdin
input=stdin.readline

for turn in range(int(input())):
    v,pe,ne=map(int,input().split())
    edges=[[] for _ in range(v+1)]
    dist=[float('inf')]*(v+1)
    dist[1]=0

    for plink in range(pe):
        st,dt,w=map(int,input().split())
        edges[st].append([dt,w])

    for nlink in range(ne):
        st,dt,w=map(int,input().split())
        edges[st].append([dt,-w])


    

    for i in range(v-1):
        for via in range(1,v+1):
            links=edges[via]
            for link in links:
                if dist[link[0]]>link[1]+dist[via]:
                    dist[link[0]]=link[1]+dist[via]

                    
    is_neg_cycle=False
    
    for node in range(1,v+1):
        for adj in edges[node]:
            if dist[adj[0]]>dist[node]+adj[1]:
                is_neg_cycle=True

    if is_neg_cycle:
        print("YES")
    else:
        print("NO")
            
