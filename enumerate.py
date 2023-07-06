import sys


def numerate(arq_error, arq_pad, h):
  
  with open(arq_error, 'r') as f:
    lines = f.readlines()
    no_header = lines[17:]   
    y = []
    for n in no_header:
        w = n.split()
        y.append(w)
    #print(y)

  with open(arq_pad, 'r') as f:
    h = int(h)
    lines = f.readlines()
  
    
    no_header = lines[h:-3]   
    x = []
    for n in no_header:
        g = n.split()
        x.append(g)
    for n in x:
       n.pop(0)
       n.pop(0)
       n.pop(0)
       n.pop(1)
    
    l = len(n)
    
    while l > 2:
        for n in x:      
            n.pop(2)
        l = l - 1
    #print(x)   

    res = []
    res_n = []
    vals = {}

    for n in x:
       p = n[0]
       if p not in res:
            res.append(p)

    for n in x:
       p = n[1]
       if p not in res_n:
            res_n.append(p)

    z = []
    b = []

    for n in res:
      vals.update({n:z})
        
    for n in vals.keys():
       for m in x:
          if n == m[0]:
             #vals[n].append(m[1])
                #with open(f'arq_{n}.txt', 'w') as f:
             print(f'{n}   {m[1]}', end='\n')
    
            
       

    



'''
  atom_group1 = no_header[:end_atom]
  print(atom_group1)

  atom_group2 = no_header[end_atom:]
  #print(atom_group2)
  #atom_group2 = ''.join(atom_group2).split()

  novos_grupos = [] 
  for line in atom_group2:
     if line != '\n':
        novos_grupos.append(line)
     else:
        break   

  with open(output_file_1, 'w') as f:
    f.writelines([str(atom) for atom in atom_group1])
   
  with open(output_file_2, 'w') as f1:
    f1.writelines([str(atom) for atom in novos_grupos])
'''
if __name__ == '__main__':
   if len(sys.argv) < 4:
        print("Usage: python extract_coordinates.py <gjf_file> <file1_name> <file2_name> <range1> <range2>")
   else:
        arq_error = sys.argv[1]
        arq_pad = sys.argv[2]
        h = sys.argv[3]
        #arq_fix = sys.argv[3]
        numerate(arq_error, arq_pad, h)
