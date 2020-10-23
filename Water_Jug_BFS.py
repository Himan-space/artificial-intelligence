def BFS(a,b,ta=0,tb=0):
    hm={}
    flag,e2=False,False
    path,queue=[],[]
    queue.append((0,0))
    t,target=0 if ta else -1,ta if ta else tb
    while queue:
        #print(queue)
        cs=queue[0]#current state
        queue.pop(0)
        if hm.get(cs,0)==1:
            continue
        if cs[0]>a or cs[-1]>b or cs[0]<0 or cs[-1]<0:
            continue
        path.append(cs)
        hm[cs]=1
        if cs[t]==target:
            flag=True
            for p in path[:-1]:
                print(p,end='->')
            print(path[-1])
            if not e2:
                print('Or')
                e2=1
                hm={}
                flag=False
                path,queue=[],[]
                queue.append((0,0))
                continue
            break

        
        if not e2:
            queue.append((cs[0],b))
            queue.append((a,cs[-1]))       
        else:
            queue.append((a,cs[-1]))
            queue.append((cs[0],b))
        

        for ap in range(max(a,b)+1):
            c,d=cs[0]+ap,cs[-1]-ap
            if c==a or (d==0 and d>=0):
                queue.append((c,d))
            c,d=cs[0]-ap,cs[-1]+ap
            if (c==0 and c>=0) or d==b:
                queue.append((c,d))

        
        if not e2:
            queue.append((0,cs[-1]))
            queue.append((cs[0],0))  
        else:
            queue.append((cs[0],0))
            queue.append((0,cs[-1]))

    if not flag:
        print('No Soluton')

BFS(4,3,2)
                
