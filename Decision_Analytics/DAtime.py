import pandas as pd
from pprint import pprint
def makedata(path = 'time.csv'):
    t = pd.read_csv(path,index_col=1)
    t = t.fillna(-1)
    assert t.shape[0] == t.shape[1]-1
    PI = {}
    for index in range(t.shape[0]):
        for n in range(t.shape[0]):
            if t.loc[index,str(n)] != -1:
                PI[(index,n)] = round(t.loc[index,str(n)] * t.loc[index,'D'],0)
    D = {}
    for i in range(t.shape[0]):
        D[i] = t.loc[i,'D']
    return t,PI, D
t,PI,D = makedata('time.csv')
end = t.shape[0] - 1
start = 0
def ped(n,PI=PI):
    return [x[0] for x in list(PI.keys()) if x[-1] == n]
    
def suc(n,PI=PI):
    return [x[1] for x in list(PI.keys()) if x[0] == n]
es = {}
ls = {}
def allin(y,dic = es,back = False):
    if back:
        a = all([x in dic.keys() for x in suc(y)])
    else:
        a =all([x in dic.keys() for x in ped(y)]) 
    return a


def cal_es(start = 0,end =12,PI = PI, D =D):
    es = {}
    es[start] = (0,0)
    batch = [start]
  
    while batch != [end]:
        new_batch = []
        for idd in batch:
            a = suc(idd)
            new_batch += a
            for i in a:
                if allin(i,es):
                    p = ped(i)
                    new = max([PI[(x,i)]+es[x][0] for x in p])
                    es[i] = (new,new+D[i])
        batch = [x for x in set(new_batch)]
    return es

# ls
def cal_ls(es,start = 0,end = 12,PI =PI,D = D):
    iid = 0
    ls = {}
    ls[end] = es[end]
    batch = [end]
    while batch != [start]:
        new_batch = []
        for iid in batch:
            cc = ped(iid)
            new_batch+= cc
            for i in cc:
                if allin(i,ls,True):
                    s = suc(i)
                    new = min([-PI[(i,x)]+ls[x][0] for x in s])
                    ls[i] = (new,new+D[i])
    #                 print(i,ls[i])
        batch = [x for x in set(new_batch)]
    return ls

def cal_cri_path(es,ls,t=t):
    aaa = []
    for i in range(t.shape[0]):
        if ls[i] == es[i]:
            aaa.append(i)
    return aaa
    
def total_slack(es, ls,t=t):
    aa={}
    for i in range(t.shape[0]):
        aa[i] = - es[i][0] + ls[i][0]
    return aa

def free_slack(es=es,D=D,PI = PI,t=t):
    aa = {}
    for i in range(t.shape[0]-1):
        aa[i]= min([es[x][0] - es[i][0] - PI[i,x] for x in suc(i)])
    return aa

    
if __name__ == '__main__':
    
    end = t.shape[0] - 1
    start = 0
    es = cal_es()
    ls = cal_ls(es)
    pprint('es:')
    pprint(es)
    pprint('ls:')
    pprint(ls)
    pprint('cal_cri_path')
    pprint(cal_cri_path(es, ls))
    pprint('total_slack')
    pprint(total_slack(es, ls))
    pprint('free_slack')
    pprint(free_slack(es))
    