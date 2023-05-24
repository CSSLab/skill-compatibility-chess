from EloPy.elopy import *
import chess
import chess.pgn
import random
import numpy as np
from collections import defaultdict
import sys
import os
from shutil import copyfile
import multiprocessing
import pymongo
import pickle
import math
from types import SimpleNamespace
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import psutil

def allmax(a):
    if len(a) == 0:
        return []
    all_ = [0]
    max_ = a[0]
    for i in range(1, len(a)):
        if a[i] > max_:
            all_ = [i]
            max_ = a[i]
        elif a[i] == max_:
            all_.append(i)
    return all_
def argmax(L):
    return int(np.random.choice(allmax(L)))

class team:
    def __init__(self,player,partner,name="", oracle=False, expector=False):
        self.name=name
        if(name==""):
            self.name=player.name+partner.name
        self.player=player
        self.partner=partner
        self.oracle=oracle
        self.expector=expector
        EloSystem.addPlayer(self.name)
        teams_dic[self.name]=self
    def info(self):
        return {'name':self.name ,'player':self.player.info(), 'partner':self.partner.info()}
    def play(self,board,bit,):
        if(bit=='1'):
            return self.partner.play(board)
        else:
            return self.player.play(board)
    def completed(self,res=True):
        self.player.completed(res)
        self.partner.completed(res)

class agent:
    def __init__(self,name,config,nodes,reset_thresh=1, expector=False):
        self.name=name
        self.config=config
        self.engine=chess.engine.SimpleEngine.popen_uci(config)
        self.reset_thresh=reset_thresh
        self.nodes=nodes
        self.counter=0
        self.reset_thresh=reset_thresh
        self.expector=expector
    def info(self):
        if(self.expector==False):
            return {'name': self.name, 'nodes':self.nodes, 'config':self.config}
        else:
            return {'name': self.name, 'nodes':self.nodes, 'config':self.config, 'expector':self.expector.info()}
    def play(self,board):
        try:
            if(self.expector !=False):
                moves=self.analyze(board, multi=True)
                movesk=[]
                idf=0
                for move in moves:
                    vals=[]
                    boardt=board.copy()
                    boardt.push(move[1])
                    if(boardt.is_game_over()):
                        vals.append((move[0],1)) # we are done, there is nothing left
                    else:
                        vals.append((move[0],0.25)) #that is the pure leela, we do not explictly encode it
                
                        boardLM=boardt.copy()
                        boardLM.push(self.engine.play(boardLM,chess.engine.Limit(nodes=self.nodes), info=2).move)


                        if(boardLM.is_game_over()): 
                            vals.append((move[0],0.25)) #then no such thing as LM, and use LL abs truth in addition to that
                        else:
                            boardLM.push(self.expector.play(boardLM).move)
                            sk=self.analyze(boardLM, noden=300)
                            vals.append((sk,0.25)) #then there is an LM, and it is 25% of the thing

                        boardML=boardt.copy()
                        boardML.push(self.expector.play(boardML).move)

                        xt=self.analyze(boardML, noden=300)
                        if(boardML.is_game_over()): 
                            vals.append((xt,0.5)) #then the M is for both and takes 0.5
                        else:
                            vals.append((xt,0.25)) #that is the ML, the other will have 0.25 coeff
                            boardML.push(self.expector.play(boardML).move) #this is MM
                            sk=self.analyze(boardLM, noden=300)
                            vals.append((sk,0.25))
                    if(sum([x[1] for x in vals])<0.95 or sum([x[1] for x in vals])>1.05 ):
                        print("HALT HALT HALT")
                        sys.exit()
                    score=sum([cptowl(x[0])*x[1] for x in vals])
                    movesk.append((score,idf,move[1]))
                    idf+=1
                movesk.sort()
                #print(movesk)
                #print("AGHA",type(movesk[0][2]))
                if(board.turn==chess.WHITE):
                    return SimpleNamespace(move=max(movesk)[2])
                else:
                    #print(movesk)
                    return SimpleNamespace(move=min(movesk)[2])
                
            return self.engine.play(board,chess.engine.Limit(nodes=self.nodes), info=2)
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        except:
            #sys.exit()
            if(self.expector!=False):
                print("expector crash")
            self.reset(True)
            print(self.name,self.config)
            feny=board.fen()
            print(feny)
            fenyl=feny.split('-')[0]
            print("reset",fenyl)
            #print(board.is_game_over())
            tboard=chess.Board(fen=fenyl)
            return self.play(tboard)
    def reset(self,res):
        if(self.expector!=False):
            self.expector.reset(res)
        self.engine.close()
        if(res):
            self.engine=chess.engine.SimpleEngine.popen_uci(self.config)
    def completed(self,res):
        self.counter+=1
        if(self.counter%self.reset_thresh==0):
            self.reset(res)
    def analyze(self,board,noden=None, multi=False): 
        if(noden is None):
            noden=self.nodes
        if(board.is_game_over()):
            #print(board)
            ok=board.result()
            if(ok=='1-0'):
                return 99999
            elif(ok=='0-1'):
                return -99999
            else:
                return 0
        if(not multi):
            r=self.engine.analyse(board,chess.engine.Limit(nodes=noden))['score'].white().score(mate_score=100000)
            return r
        else:
            r=self.engine.analyse(board,chess.engine.Limit(nodes=noden), multipv=5 )#['score'].white().score(mate_score=100000)
            return [(x['score'].white().score(mate_score=100000),x['pv'][0])for x in r]



def gbitstring(n):
    return ''.join(random.choice('01') for _ in range(n))
def cptowl(feval):
    return 0.5+math.atan(feval/290.680623072)/3.096181612
def freestuff(bitstring,infoarray,van,res):
    agrtot_en=0
    agr_en=0
    agrtot_van=0
    agr_van=0
    delt_van=0
    deltot_van=0
    delt_en=0
    deltot_en=0
    for i in range(len(infoarray)):
        if(i>=2 and bitstring[i]=='1' and bitstring[i-2]=='1' and bitstring[i-1]=='0'):
            if(i%2==van):
                delt_van+=(cptowl(infoarray[i])-cptowl(infoarray[i-2]))*(1 if van==0 else -1)
                deltot_van+=1
            else:
                delt_en+=(cptowl(infoarray[i])-cptowl(infoarray[i-2]))*(1 if van==1 else -1)
                deltot_en+=1
        if(bitstring[i]=='1' and i%2==van):
            agrtot_van+=1
            agr_van+=np.sign(infoarray[i])==res
        if(bitstring[i]=='1' and i%2!=van):
            agrtot_en+=1
            agr_en+=np.sign(infoarray[i])==res
    #print(van,res,wpldelt,wpltot)
    return {'leela_right':(agr_van+1)/(agrtot_van+1),'engine_right':(agr_en+1)/(agrtot_en+1),'loss_van':(delt_van)/(deltot_van+1),'loss_en':(delt_en)/(deltot_en+1)}

        
def suite(boardt, obj, obj1, other, maia):
    try:
        boardy=boardt.copy()
        if(boardt.is_game_over()):
            return -1
        dic={}
        dic['fen']=boardt.fen()
        dic['eval']=obj.analyze(boardt)
        #dic['funcs']=getd(driver,boardt.fen())
        boardt2=boardt.copy()


        dic['obj_move']=obj1.play(boardt).move
        dic['maia_move']=maia.play(boardt).move
        dic['maia_move']=dic['maia_move'].uci()
        boardt.push(dic['obj_move'])
        dic['obj_fen']=boardt.fen()
        dic['obj_move']=dic['obj_move'].uci()

        if(boardt.is_game_over()):
            return -1

        dic['obj_loss']=obj.analyze(boardt)
        #dic['obj_funcs']=getd(driver,boardt.fen())

        dic['obj_maia_move']=maia.play(boardt).move
        boardt.push(dic['obj_maia_move'])
        dic['obj_maia_move']=dic['obj_maia_move'].uci()
        dic['obj_maia_loss']=obj.analyze(boardt)
        


        dic['other_move']=other.play(boardt2).move
        boardt2.push(dic['other_move'])
        dic['other_fen']=boardt2.fen()
        dic['other_move']=dic['other_move'].uci()

        if(boardt2.is_game_over()):
            return -1
        dic['other_loss']=obj.analyze(boardt2)
        #dic['other_funcs']=getd(driver,boardt2.fen())
    
        dic['other_maia_move']=maia.play(boardt2).move
        boardt2.push(dic['other_maia_move'])
        dic['other_maia_move']=dic['other_maia_move'].uci()
        dic['other_maia_loss']=obj.analyze(boardt2)
        return dic
    except KeyboardInterrupt:
        raise KeyboardInterrupt()
    except:
        #sys.exit()
        print("that reset")
        obj.reset(True)
        other.reset(True)
        maia.reset(True)
        
        feny=boardy.fen()
        print(feny)
        fenyl=feny.split('-')[0]
        print("reset",fenyl)
        tboard=chess.Board(fen=fenyl)
        return suite(tboard,obj,other,maia)
    
    
def getd(driver, fen ):
    dres=driver.execute_script("return lf(arguments[0])", fen)
    vals={}
    for el in dres:
        vals[el[0]]=float(el[1])
    return vals


def play(white, black,plystring,obj,obj1,other,maia,ind):
    # options = Options()
    # options.headless = True
    # driver = webdriver.Firefox(options=options)
    
   
    curgame={}
    values=[]
    anarray=[]
    numplies=0
    board = chess.Board()
    game=chess.pgn.Game()
    t=0
    
    while not board.is_game_over():
        ### this is disgusting
        boardt=board.copy()
        anarray.append(suite(boardt,obj,obj1,other,maia))
        # dic={}
        # if(boardt.is_game_over()):
        #     dic['flag']=-1
        # else:
        #     dic={}
        #     dic['fen']=boardt.fen()
        #     dic['eval']=obj.analyze(boardt)
        #     #dic['funcs']=getd(driver,boardt.fen())
        #     boardt2=boardt.copy()


        #     dic['obj_move']=obj.play(boardt).move
        #     boardt.push(dic['obj_move'])
        #     dic['obj_fen']=boardt.fen()
        #     dic['obj_move']=dic['obj_move'].uci()

        #     if(boardt.is_game_over()):
        #         dic['flag']=-1
        #     else:

        #         dic['obj_loss']=obj.analyze(boardt)
        #         #dic['obj_funcs']=getd(driver,boardt.fen())

        #         dic['obj_maia_move']=maia.play(boardt).move
        #         boardt.push(dic['obj_maia_move'])
        #         dic['obj_maia_move']=dic['obj_maia_move'].uci()
        #         dic['obj_maia_loss']=obj.analyze(boardt)
                


        #         dic['other_move']=other.play(boardt2).move
        #         boardt2.push(dic['other_move'])
        #         dic['other_fen']=boardt2.fen()
        #         dic['other_move']=dic['other_move'].uci()

        #     if(boardt2.is_game_over()):
        #         dic['flag']=-1
        #     else:
        #         dic['other_loss']=obj.analyze(boardt2)
        #         #dic['other_funcs']=getd(driver,boardt2.fen())
                
        #         dic['other_maia_move']=maia.play(boardt2).move
        #         boardt2.push(dic['other_maia_move'])
        #         dic['other_maia_move']=dic['other_maia_move'].uci()
        #         dic['other_maia_loss']=obj.analyze(boardt2)
        
        #print(board.fen())
        numplies+=1
        if(t%2==0):
            result = white.play(board,plystring[t])
        else:
            result = black.play(board,plystring[t])
        board.push(result.move)
        if(t==0):
            node=game.add_variation(chess.Move.from_uci(str(result.move)))
        else:
            node=node.add_variation(chess.Move.from_uci(str(result.move)))
        t+=1
        #values.append(result.info['score'].white().score(mate_score=100000))
        
        
    #driver.close()
    ok=board.outcome().winner
    plystring=plystring[0:numplies]
    if(ok==None):
        winner=0
    elif(ok):
        winner=1
    else:
        winner=-1
    curgame['winner']=winner
    curgame['length']=numplies
    curgame['move_identities']=plystring
    curgame['values']=values
    curgame['anarray']=anarray
    exporter = chess.pgn.StringExporter(headers=False, variations=False, comments=False)
    pgn_string = game.accept(exporter)
    pgn_string=pgn_string.replace('\n'," ")
    curgame['pgn']=pgn_string
    #curgame['byproducts']=freestuff(plystring,values,white.partner.name!='s53',winner)
    #print(pgn_string)
    coin=random.uniform(0,1)
    if(coin<0.8):
        settype='tr'
    elif(coin<0.9):
        settype='va'
    else:
        settype='te'
    curgame['set']=settype
    curgame['white']=white.info()
    curgame['black']=black.info()
    curgame['name']=curgame['white']['name']+'x'+curgame['black']['name']+"_5" #REMOVEEE
    print("preret",ind)
    
    return curgame

teams_dic={}
EloSystem=Implementation()
#assumption of defaults
def worker(partner1_name, partner2_name, partner1_weights, partner2_weights,i,q,bitstring):
    print("start",i)
    random.seed()
    plystring=bitstring
    #print(plystring)
    #print(plystring[0:10])
    #sys.stderr = open(name_of_run+'/trash'+str(i), 'w')
    sys.stderr = None
    maiay=agent('m11',["lc0" , "--temperature=0", "--weights=maia-1100.pb.gz","--backend-opts=gpu="+str((i)%4) ],1)
    partnery=agent(partner1_name,["lc0" , "--weights="+partner1_weights,"--backend-opts=gpu="+str((i+1)%4)],1500)   
    team1=team(maiay,partnery)

    maiay=agent('m11',["lc0" , "--temperature=0", "--weights=maia-1100.pb.gz","--backend-opts=gpu="+str((i+2)%4) ],1)

    maiaexp=agent('m11',["lc0" , "--temperature=0", "--weights=maia-1100.pb.gz","--backend-opts=gpu="+str((i+3)%4) ],1)
    partnery=agent(partner2_name,["lc0" , "--weights="+partner2_weights,"--backend-opts=gpu="+str((i+4)%4)],1500,expector=maiaexp)   
    team2=team(maiay,partnery)

    #neutral=play(team1,team1,plystring)

    #team1.completed()


    maiaexp2=agent('m11pp',["lc0" , "--temperature=0", "--weights=maia-1100.pb.gz","--backend-opts=gpu="+str((i+5)%4) ],1)
    obj=agent("anal",["lc0" , "--weights="+partner1_weights,"--backend-opts=gpu="+str((i+6)%4)],1500)
    obj1=agent("anal",["lc0" , "--weights="+partner1_weights,"--backend-opts=gpu="+str((i+7)%4)],1500)
    other=agent("analp",["lc0" , "--weights="+partner2_weights,"--backend-opts=gpu="+str((i+8)%4)],1500,expector=maiaexp2)
    maia2=agent('m11p',["lc0" , "--temperature=0", "--weights=maia-1100.pb.gz","--backend-opts=gpu="+str((i+9)%4) ],1)
    
    r1=play(team1,team2,plystring,obj,obj1,other,maia2,i)
    team1.completed()
    team2.completed()
    obj.completed(True)
    other.completed(True)
    maia2.completed(True)
    r2=play(team2,team1,plystring,obj,obj1,other,maia2,i)
    team1.completed(False)
    team2.completed(False)

    obj.completed(False)
    other.completed(False)
    maia2.completed(False)

    #make sure same place
    r2['set']=r1['set']
    #r3['set']=r1['set']
    print("preput",i)
    q.put((r1,r2,i))
    print("postput",i)
    print("size",q.qsize())
    print("finalpreret", i)

    #p = psutil.Process(pid)
    #p.terminate()  #or p.kill()
    return 
def choosenext(result_matrix,pre_totals_matrix):
    matchup_eligibility=np.zeros((n,n),dtype=int)
    for i in range(1,n):
        matchup_eligibility[0][i]=100000-pre_totals_matrix[0][i]
    selected=(0,np.argmax(matchup_eligibility[0]))
    ind=int(pre_totals_matrix[selected]/2)
    pre_totals_matrix[selected]+=2
    return (selected,ind)

def scorear():
    return [0,0,0]
def controller(num_proc):
    load_path="battle_results/"+"officialfocused"
    pos_path="ranbits_5000.pkl"
    with open(pos_path, 'rb') as f:
        bitstrings = pickle.load(f)[200:]
    team_names=['m11'+x for x in partner_names]
    result_dic=defaultdict(scorear)
    totals_matrix=np.zeros((n,n),dtype=int)
    pre_totals_matrix=np.zeros((n,n),dtype=int)
    perc1=[[] for i in range(n)]
    perc2=[[] for i in range(n)]
    resmat=[[2 for j in range(2*len(bitstrings))] for i in range(n)]
    correctness=[[] for i in range(n)]
    value_after_van=[[] for i in range(n)]
    value_after_en=[[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            totals_matrix[j][i]=totals_matrix[i][j]
            pre_totals_matrix[j][i]=pre_totals_matrix[i][j]
    result_matrix=np.zeros((n,n),dtype=int)
    result_matrix2=np.zeros((n,n,3,3),dtype=int)
    proc_ar=[]
    nowar=[]
    manager=multiprocessing.Manager()
    q=manager.Queue()
    deadproc=np.ones(n)
    
    for i in range(num_proc):
        now,ind=choosenext(result_matrix,pre_totals_matrix)
        p = multiprocessing.Process(target=worker,args=(partner_names[now[0]],partner_names[now[1]],weight_files[now[0]],weight_files[now[1]],i,q,bitstrings[ind]))
        proc_ar.append(p)
        nowar.append((now,ind))
        p.start()
    while(True):
        if(datetime.now().minute%30==0 and datetime.now().second==0 and datetime.now().microsecond<1000):
            print(q.qsize(),datetime.now())
        if(q.qsize()!=0):
            #try:
                #print("trying", q.qsize())
            res=q.get(block=False)
            #except KeyboardInterrupt:
            #    raise KeyboardInterrupt()
            #except:
            #    print("EMPTY TRY", q.qsize())
                #print(q.qsize())
            #    continue
            j=res[2]
            mycol.insert(res[0])
            mycol.insert(res[1])
            print("gotten", j)
            #mycol.insert(res[2])
            ii=nowar[j][0][0]
            jj=nowar[j][0][1]
            totals_matrix[nowar[j][0]]+=2
            totals_matrix[jj][ii]+=2
            result_matrix[ii][jj]+=res[0]['winner']
            result_matrix[ii][jj]-=res[1]['winner']
            result_matrix[jj][ii]-=res[0]['winner']
            result_matrix[jj][ii]+=res[1]['winner']
            result_dic[res[0]['name']][res[0]['winner']]+=1
            result_dic[res[1]['name']][res[1]['winner']]+=1
            perc1[jj].append(result_matrix[jj][ii]/totals_matrix[jj][ii])
            perc2[jj].append((result_matrix2[jj][ii][2][2]-result_matrix2[jj][ii][1][1]+1)/(result_matrix2[jj][ii][2][2]+result_matrix2[jj][ii][1][1]+1))
            result_matrix2[ii][jj][res[0]['winner']][-res[1]['winner']]+=1
            resmat[jj][2*nowar[j][1]+1]=res[1]['winner']
            resmat[jj][2*nowar[j][1]]=-res[0]['winner']
            # correctness[ii].append(res[0]['byproducts']['leela_right'])
            # correctness[ii].append(res[1]['byproducts']['leela_right'])
            # correctness[jj].append(res[0]['byproducts']['engine_right'])
            # correctness[jj].append(res[1]['byproducts']['engine_right'])
            # value_after_van[jj].append(res[0]['byproducts']['loss_van'])
            # value_after_van[jj].append(res[1]['byproducts']['loss_van'])
            # value_after_en[jj].append(res[0]['byproducts']['loss_en'])
            # value_after_en[jj].append(res[1]['byproducts']['loss_en'])
            meancorr=[np.mean(el) for el in correctness]
            meanvalvan=[np.mean(el) for el in value_after_van]
            meanvalen=[np.mean(el) for el in value_after_en]
            #if(res[0]['winner']==-res[1]['winner']):
            #    print(res[0]['winner'])
            #    print(res[0]['move_identities'])
            #    print(res[0]['pgn'])
            #    print(res[1]['move_identities'])
            #print(res[0]['pgn'])
            ff=open(name_of_run+'/results.txt','w')
            ff.write("teams: "+str(team_names)+'\n')
            ff.write("expanded results: "+str(result_dic)+'\n')
            ff.write("matrix results:"+'\n'+str(result_matrix2)+'\n')
            ff.write("simple results:"+'\n'+str(result_matrix)+'\n')
            ff.write("game_totals: "+'\n'+str(totals_matrix)+'\n')
            ff.write("pre_totals:"+'\n'+str(pre_totals_matrix)+'\n')
            #ff.write("metrics:"+'\n'+str(meancorr)+"valaf: "+str(meanvalvan)+" valafen: "+str(meanvalen))
            with open(name_of_run+'/result_dic.pkl',"wb") as g:
                pickle.dump(result_dic, g)
            with open(name_of_run+'/result_matrix.pkl',"wb") as g:
                pickle.dump(result_matrix,g)
            with open(name_of_run+'/result_matrix2.pkl',"wb") as g:
                pickle.dump(result_matrix2,g)
            with open(name_of_run+'/totals_matrix.pkl',"wb") as g:
                pickle.dump(totals_matrix, g)
            with open(name_of_run+'/perc1.pkl', "wb") as g:
                pickle.dump(perc1,g)
            with open(name_of_run+'/perc2.pkl', "wb") as g:
                pickle.dump(perc2,g)
            for w in range(n):
                with open(name_of_run+'/'+pos_path+'_'+partner_names[w]+'.pkl', 'wb') as g:
                    pickle.dump(resmat[w],g)
            ff.close()
            now,ind=choosenext(result_matrix,pre_totals_matrix)
            proc_ar[j].terminate()
            p = multiprocessing.Process(target=worker,args=(partner_names[now[0]],partner_names[now[1]],weight_files[now[0]],weight_files[now[1]],j,q,bitstrings[ind]))
            proc_ar[j]=p
            nowar[j]=(now,ind)
            print([proc_ar[k].is_alive() for k in range(len(proc_ar))],datetime.now())
            p.start()




name_of_run="battle_results/"+"NAME_OF_RUN"
os.makedirs(name_of_run,exist_ok=True)
copyfile('pairconner_stats.py', name_of_run+'/pairconner_stats.py')
partner_names=['s53','hnbf']
#for i in range(1,2):
#    for j in range(8):
#        partner_names.append('rigdb'+str(1+i)+'g1rate4'+'v'+str(j+1))
print(partner_names)
myclient = pymongo.MongoClient("HOST LOCATION")
mydb = myclient["YOUR_DATABASE"]
mycol=mydb["COLUMN NAME"]
weight_files=[
'models/128x10-t60-2-5300.pb.gz',
"models/maia-1100.pb.gz"
]





n=len(partner_names)
controller(8)
