class Tree:
    def __init__(self,root):
        self.root=root
        self.pr=None
        self.children=[]
    def addNode(self,obj):
        self.children.append(obj)
        
class Node:
    def __init__(self,data,level,fscore,pr):
        self.data = data
        self.level = level
        self.fscore = fscore
        self.pr=pr
        self.children=[]

    def new_node(self,parent):
        pos=[(i,j.index('_')) for i,j in enumerate(self.data) if "_" in j]
        x,y = pos[0][0],pos[0][1]
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0,parent)
                self.children.append(child_node)
                
        return self.children
        
    def shuffle(self,puz,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = [i[:] for i in puz[:]]
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None    
            

class Puzzle:
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,start,goal):
        return self.h(start.data,goal)+start.level

    def h(self,start,goal):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
    def printd(self,v):
        if len(v)<13:
            for i in range(3):
                for j in range(len(v)):
                    if j!=len(v)-1:
                        print(v[j].data[i][0],v[j].data[i][1],v[j].data[i][2],end="\t")
                    else:
                        print(v[j].data[i][0],v[j].data[i][1],v[j].data[i][2])
            for j in range(len(v)):
                if j!=len(v)-1:
                    print('n(f):'+str(v[j].fscore),end=" "*(3-len(str(v[j].fscore))))
                else:
                    print('n(f):'+str(v[j].fscore))
        else:
            srt,end=0,13
            while end<=len(v):
                for i in range(3):
                    for j in range(srt,end):
                        if j!=len(v)-1:
                            print(v[j].data[i][0],v[j].data[i][1],v[j].data[i][2],end="\t")
                        else:
                            print(v[j].data[i][0],v[j].data[i][1],v[j].data[i][2])
                for j in range(srt,end):
                    if j!=len(v)-1:
                        print('n(f):'+str(v[j].fscore),end=" "*(2-len(str(v[j].fscore))))
                    else:
                        print('n(f):'+str(v[j].fscore))
                        
                if end==len(v):
                    break
                srt=end
                end+=len(v)-srt
                end=srt+13 if end-srt>13 else end                       
                print('')
      
    def process(self):
        print("Enter the start state matrix")
        starts = self.accept()        
        goal = [['1','2','3'],['8','_','4'],['7','6','5']]

        start = Node(starts,0,0,None)
        root=Tree(start)
        start.fscore = self.f(start,goal)
        self.open.append(start)
        optimal=[]
        cnt={}
        tre={}
        tre[start.level]=[start]
        
        while True:
            cur = self.open[0]
            cnt[cur.level]=cnt.get(cur.level,0)+1
            k=sorted(cnt)
            if cnt[k[-1]]>1000:
                print('Not Solvable')
                return 0
            #print(" → ")            
            if(self.h(cur.data,goal) == 0):
                break
            
            for i in cur.new_node(cur):
                root.addNode(i)
                if i.data not in self.closed:
                    tre[i.level]=tre.get(i.level,[])+[i]
                    i.fscore = self.f(i,goal)
                    self.open.append(i)
            self.closed.append(cur)    
            del self.open[0]
            self.open.sort(key = lambda x:x.fscore)
            #if cur.level>=self.open[0].level:
            #   print("Local Maximum: Problem cannot be solved using HillClimbing")
            #   return
        temp=cur
        try:
            while root.children[root.children.index(temp)].pr:
                optimal.insert(0,temp)
                temp=root.children[root.children.index(temp)].pr
        except:
            pass
        optimal.insert(0,start)
        
        for k,v in list(tre.items())[:-1]:
            print('')
            print('-'*10,'LEVEL',k,'-'*10,'n(f)=n(g)+n(h)')
            self.printd(v)
        for k,v in list(tre.items())[-1:]:
            v.sort(key = lambda x:x.fscore)
            print('')
            print('-'*10,'LEVEL',k,'-'*10,'n(f)=n(g)+n(h)')
            self.printd(v)    
                    
        
        '''print('\n')
        for i in range(3):
            for j in range(len(optimal)):
                if i==2 and j==len(optimal)-1:
                    print(optimal[j].data[i][0],optimal[j].data[i][1],optimal[j].data[i][2],"Goal State")
                elif i==1 and j!=len(optimal)-1:
                    print(optimal[j].data[i][0],optimal[j].data[i][1],optimal[j].data[i][2],end=" → ")
                elif j!=len(optimal)-1:
                    print(optimal[j].data[i][0],optimal[j].data[i][1],optimal[j].data[i][2],end="\t")
                else:
                    print(optimal[j].data[i][0],optimal[j].data[i][1],optimal[j].data[i][2])
                
        for j in range(len(optimal)):
            if j!=len(v)-1:
                print('n(f):'+str(optimal[j].fscore),end="  ")
            else:
                print('n(f):'+str(optimal[j].fscore))'''      
            
        '''for lvl in optimal:
            print("  ↓  ")
            for i in lvl:
                for j in i:
                    print(j,end=" ")
                print(" ")'''
        print('↥ Goal State')
        
puz = Puzzle(3)
puz.process()

