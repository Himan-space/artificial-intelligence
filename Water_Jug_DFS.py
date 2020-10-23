def DFS(a,b,ta=0,tb=0):
    hm={}
    flag,e2=False,False
    path,stack=[],[]
    stack.append((0,0))
    t,target=0 if ta else -1,ta if ta else tb
    while stack:
        cs=stack[-1]#current state
        stack.pop()
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
                path,stack=[],[]
                stack.append((0,0))
                continue
            break

        if e2:
            stack.append((cs[0],b))
            stack.append((a,cs[-1]))       
        else:
            stack.append((a,cs[-1]))
            stack.append((cs[0],b))       

        for ap in range(max(a,b)+1):
            c,d=cs[0]+ap,cs[-1]-ap
            if c==a or (d==0 and d>=0):
                stack.append((c,d))
            c,d=cs[0]-ap,cs[-1]+ap
            if (c==0 and c>=0) or d==b:
                stack.append((c,d))

        if e2:
            stack.append((0,cs[-1]))
            stack.append((cs[0],0))  
        else:
            stack.append((cs[0],0))
            stack.append((0,cs[-1]))
              
    if not flag:
        print('No Soluton')

DFS(4,3,2)
