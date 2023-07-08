### O codigo ta feio mas funcional, precisa ser realizado a mudança de residuos modificados no .txt (HIE tem que ser trocado para HIS e CYX para CIS).
### Problemas: o arquivo novo ta saindo com o nome da variavel h deveria sair com o nome fornecido em arq_fix.


def numerate(arq_error, arq_pad, h, arq_fix):

  ARG = []
  HIS = []
  LYS = []
  ASP = []
  GLU = []
  SER = []
  THR = []
  ASN = []
  GLN = []
  CYS = []
  SEC = []
  GLY = []
  PRO = []
  ALA = []
  VAL = []
  ILE = []
  LEU = []
  MET = []
  PHE = []
  TYR = []
  TRP = []

  with open(arq_error, 'r') as f:
    lines = f.readlines()
    new_arq = str(lines[:17])
    new_arq = new_arq.replace("'", "")
    new_arq = new_arq.replace("]", "")
    new_arq = new_arq.replace("[", "")
    new_arq = new_arq.replace("\\n", "")
    new_arq = new_arq.replace(",", "\n")
    no_header = lines[17:]  
    y = []
    for n in no_header:
        w = n.split()
        y.append(w)
    y.pop(-1)
    
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

    for m in x:
        if m[0] == "ARG":
            if m[1] not in ARG:   
               ARG.append(m[1])
        elif m[0] == "HIS":
            if m[1] not in HIS:
               HIS.append(m[1])
        elif m[0] == "LYS":
            if m[1] not in LYS:
               LYS.append(m[1])
        elif m[0] == "ASP":
            if m[1] not in ASP:
               ASP.append(m[1])  
        elif m[0] == "GLU":
            if m[1] not in GLU:
               GLU.append(m[1])
        elif m[0] == "SER":
            if m[1] not in SER:
               SER.append(m[1])
        elif m[0] == "THR":
            if m[1] not in THR:
               THR.append(m[1])
        elif m[0] == "ASN":
            if m[1] not in ASN:
               ASN.append(m[1])
        elif m[0] == "GLN":
            if m[1] not in GLN:
               GLN.append(m[1])
        elif m[0] == "CYS":
            if m[1] not in CYS:
               CYS.append(m[1])
        elif m[0] == "SEC":
            if m[1] not in SEC:
               SEC.append(m[1])
        elif m[0] == "GLY":
            if m[1] not in GLY:
               GLY.append(m[1])
        elif m[0] == "PRO":
            if m[1] not in PRO:
               PRO.append(m[1])
        elif m[0] == "ALA":
            if m[1] not in ALA:
               ALA.append(m[1])
        elif m[0] == "VAL":
            if m[1] not in VAL:
               VAL.append(m[1])
        elif m[0] == "ILE":
            if m[1] not in ILE:
               ILE.append(m[1])
        elif m[0] == "LEU":
            if m[1] not in LEU:
               LEU.append(m[1])
        elif m[0] == "MET":
            if m[1] not in MET:
               MET.append(m[1])
        elif m[0] == "PHE":
            if m[1] not in PHE:
               PHE.append(m[1])
        elif m[0] == "TYR":
            if m[1] not in TYR:
               TYR.append(m[1])
        else:
            if m[1] not in TRP:
               TRP.append(m[1])
      
    q_1 = 0
    q_2 = 0
    q_3 = 0 
    q_4 = 0
    q_5 = 0
    q_6 = 0
    q_7 = 0
    q_8 = 0
    q_9 = 0
    q_10 = 0
    q_11 = 0
    q_12 = 0
    q_13 = 0
    q_14 = 0
    q_15 = 0
    q_16 = 0
    q_17 = 0
    q_18 = 0
    q_19 = 0
    q_20 = 0
    q_21 = 0

    for m in y:
        if m[0] == "ARG":
            m[1] = ARG[q_1]
            q_1 = q_1 + 1    
    for m in y:    
        if m[0] == "HIS":
            m[1] = HIS[q_2]
            q_2 = q_2 + 1
    for m in y:    
        if m[0] == "LYS":
            m[1] = LYS[q_3]
            q_3 = q_3 + 1
    for m in y:    
        if m[0] == "ASP":
            m[1] = ASP[q_4]
            q_4 = q_4 + 1
    for m in y:    
        if m[0] == "GLU":
            m[1] = GLU[q_5]
            q_5 = q_5 + 1
    for m in y:    
        if m[0] == "SER":
            m[1] = SER[q_6]
            q_6 = q_6 + 1
    for m in y:    
        if m[0] == "THR":
            m[1] = THR[q_7]
            q_7 = q_7 + 1
    for m in y:    
        if m[0] == "ASN":
            m[1] = ASN[q_8]
            q_8 = q_8 + 1
    for m in y:    
        if m[0] == "GLN":
            m[1] = GLN[q_9]
            q_9 = q_9 + 1
    for m in y:    
        if m[0] == "CYS":
            m[1] = CYS[q_10]
            q_10 = q_10 + 1
    for m in y:    
        if m[0] == "SEC":
            m[1] = SEC[q_11]
            q_11 = q_11 + 1
    for m in y:    
        if m[0] == "GLY":
            m[1] = GLY[q_12]
            q_12 = q_12 + 1
    for m in y:    
        if m[0] == "PRO":
            m[1] = PRO[q_13]
            q_13 = q_13 + 1
    for m in y:    
        if m[0] == "ALA":
            m[1] = ALA[q_14]
            q_14 = q_14 + 1
    for m in y:    
        if m[0] == "VAL":
            m[1] = VAL[q_15]
            q_15 = q_15 + 1
    for m in y:    
        if m[0] == "ILE":
            m[1] = ILE[q_16]
            q_16 = q_16 + 1
    for m in y:   
        if m[0] == "LEU":
            m[1] = LEU[q_17]
            q_17 = q_17 + 1
    for m in y:    
        if m[0] == "MET":
            m[1] = MET[q_18]
            q_18 = q_18 + 1
    for m in y:    
        if m[0] == "PHE":
            m[1] = PHE[q_19]
            q_19 = q_19 + 1
    for m in y:    
        if m[0] == "TYR":
            m[1] = TYR[q_20]
            q_20 = q_20 + 1
    for m in y:    
        if m[0] == "TRP":
            m[1] = TRP[q_21]
            q_21 = q_21 + 1

    y = str(y)
    y = y.replace("[", "")
    y = y.replace(",", "")
    y = y.replace("'", "")
    y = y.replace(" ", "     ")
    y = y.replace("]", "\n")
    y = y.split()
       
  with open(arq_fix, 'w') as f:
     f.write(" {}".format(new_arq))
     t = ["ARG",  "HIS",  "LYS",  "ASP",  "GLU",  "SER",  "THR",  "ASN",  "GLN",  "CYS",  "SEC",  "GLY",  "PRO",  "ALA",  "VAL",  "ILE",  "LEU",  "MET",  "PHE",  "TYR",  "TRP"]
     for n in y:
         for m in t:
             if m == n:
                 f.write("\n")
         if len(n) == 3:
             f.write("     {}".format(n))
         elif len(n) == 2:
             f.write("      {}".format(n))
         elif len(n) == 1:
             f.write("       {}".format(n))
         elif len(n) == 9:
             f.write("   {}".format(n))    
         elif len(n) == 10:
             f.write("  {}".format(n))         
         else:
             f.write("    {}".format(n))

if __name__ == '__main__':
   if len(sys.argv) < 4:
        print("Usage: python extract_coordinates.py <gjf_file> <file1_name> <file2_name> <range1> <range2>")
   else:
        arq_error = sys.argv[1]
        arq_pad = sys.argv[2]
        h = sys.argv[3]
        arq_fix = sys.argv[3]
        numerate(arq_error, arq_pad, h, arq_fix)

