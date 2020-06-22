import re

countnand=0
fcount=0
list1=[]
list123=[]
list1233=[]
countgate=0
f2=f3=f4=f5=f6=f7=f8=f9=f10=f11=f12=0

with open("c432.v") as fp:
   for num,line in enumerate(fp,1):
       if 'AND2X1' in line:
         countgate=countgate+1
       if 'OR2X1' in line:
         countgate=countgate+1
       if 'BUFX1' in line:
         countgate=countgate+1
       if 'INVX1' in line:
         countgate=countgate+1

           

with open("c432.v") as fp:
   for num,line in enumerate(fp,1):
      #if 'XOR2X1' not in line:
         if 'input' in line:
            x=re.split(r'[,\s;]+', line)
            inputy=len(x)-2
            
with open("c432.v") as fp:
   for num,line in enumerate(fp,1):
       if 'fanout2' in line:
         f2=f2+1
       if 'fanout3' in line:
         f3=f3+1
       if 'fanout4' in line:
         f4=f4+1
       if 'fanout5' in line:
         f5=f5+1
       if 'fanout6' in line:
         f6=f6+1
       if 'fanout7' in line:
         f7=f7+1
       if 'fanout8' in line:
         f8=f8+1
       if 'fanout9' in line:
         f9=f9+1
       if 'fanout12' in line:
         f12=f12+1
fall=(f2*2)+(f3*3)+(f4*4)+(f5*5)+(f6*6)+(f7*7)+(f8*8)+(f9*9)+(f12*12)
lengthh=((countgate+inputy+fall)*2)

print("Total number of stuck at values before equilvalence faults: ",((countgate+inputy+fall)*2))



# --------------------- before equivalent fault calculate ------ 










with open("c432.v") as fp:
   for num,line in enumerate(fp,1):
      #if 'XOR2X1' not in line:
         if 'input' in line:
            x=re.split(r'[,\s;]+', line)
            y=len(x)
            input1=x[1:(y-1)]
            
         if 'AND2X1' in line:
            x=re.split(r'[,\s;]+', line)
            y=x[2:len(x)]
            k=[re.sub('[^c-xC-X0-9]+', '', _) for _ in y]
            list123=list123+k
         
         if 'INVX1' in line:
            x=re.split(r'[,\s;]+', line)
            y=x[2:len(x)]
            k=[re.sub('[^c-xC-X0-9]+', '', _) for _ in y]
            list123=list123+k
            
         if 'OR2X1' in line:
            x=re.split(r'[,\s;]+', line)
            y=x[2:len(x)]
            k=[re.sub('[^c-xC-X0-9]+', '', _) for _ in y]
            list123=list123+k
            
         if 'BUFX1' in line:
            x=re.split(r'[,\s;]+', line)
            y=x[2:len(x)]
            k=[re.sub('[^c-xC-X0-9]+', '', _) for _ in y]
            list123=list123+k
            
         
 
            
while '' in list123:
   list123.remove('')
list123=list123+input1
my_set=set(list123)
#print( len(my_set))
#print(my_set)



w1 = list(map(( lambda x:  x + '(stk0)'), my_set))
w2 = list(map(( lambda x:  x + '(stk1)'), my_set))
w3= w1+w2
w33=w1+w2


with open ("c432_BF.txt","w")as fa:
   for line in w3: 
       fa.write(line+"\n")
   fa.write("\n")
   fa.write("\n")
   fa.write('Total Fault_BF: '+ str(lengthh))
fa.close()



woiA = list(map(( lambda x:  '.A(' + x + ')' ),my_set))
woiB = list(map(( lambda x:  '.B(' + x + ')' ),my_set))
woiAB= woiA+woiB

with open("c432.v") as fp:
    for num,line in enumerate(fp,1):
      #if not 'XOR2X1' in line:
      
      
         if 'AND2X1' in line:
            for n in woiAB:
               #print(n)
               #print(line)
               if n in line:
                  #print(n,line)
                  n1=re.sub('[^C-ZC-z0-9]+','',n)
                  #print(n1)
                  n11='%s(stk0)'% n1
                  list1.append(n11)
                  set1=set(list1)
                  #print(set1)
                  #print("**",n11)
                  w3.remove(n11)
                  #print(iow)
                  #print('******')
       
         if 'NOR2X1' in line:
            for n in woiAB:
               #print(n)
               #print(line)
               if n in line:
                  #print(n,line)
                  n1=re.sub('[^C-ZC-z0-9]+','',n)
                  #print(n1)
                  n11='%s(stk1)'% n1
                  list1.append(n11)
                  set1=set(list1)
                  #print(set1)
                  #print("**",n11)
                  w3.remove(n11)
                  #print(iow)
                  #print('******')     
          
         if 'INVX1' in line:
            for n in woiAB:
               #print(n)
               #print(line)
               if n in line:
                  #print(n,line)
                  n1=re.sub('[^C-ZC-z0-9]+','',n)
                  #print(n1)
                  n11='%s(stk0)'% n1
                  n12='%s(stk1)'% n1
                  list1.append(n11)
                  list1.append(n12)
                  set1=set(list1)
                  #print(set1)
                  #print("**",n11)
                  w3.remove(n11)
                  w3.remove(n12)
                  #print(iow)
                  #print('******')
            
         if 'BUFX1' in line:
            for n in woiAB:
               #print(n)
               #print(line)
               if n in line:
                  #print(n,line)
                  n1=re.sub('[^C-ZC-z0-9]+','',n)
                  #print(n1)
                  n11='%s(stk0)'% n1
                  n12='%s(stk1)'% n1
                  list1.append(n11)
                  list1.append(n12)
                  set1=set(list1)
                  #print(set1)
                  #print("**",n11)
                  w3.remove(n11)
                  w3.remove(n12)
                  #print(iow)
                  #print('******')
                  
      
         
         
                  
      

print("Total number of stuck at values after equilvalence faults: ",len(w3))
aw3=len(w3)
print("Collapse ratio: ", (aw3/((countgate+inputy+fall)*2) ))
#print("Total number of stuck at values that got removed : ",len(set1))

cr=(aw3/((countgate+inputy+fall)*2))
#print(cr)

with open ("c432_AF.txt","w")as fa:
   for line in w3:
       fa.write(line+"\n")
   fa.write("\n")
   fa.write("-------------------------------------------")
   fa.write("\n")
   fa.write('Total Fault_AF: '+ str(aw3))
   fa.write("\n")
   fa.write("-------------------------------------------")
   fa.write("\n")
   fa.write('Collapse Ratio: '+ str(cr))
   fa.write("\n")
   fa.write("\n")
   fa.write("Equivalent Classes: ")
   fa.write("\n")
   for line in w33:
       fa.write(line+"\n")
fa.close()


