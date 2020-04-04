import random
import math
import numpy as np
from scipy import stats

dosada_zarazeni = [46, 48, 57, 72, 89, 103, 135, 171, 222, 249, 303, 384, 457, 528, 659, 741, 785, 900, 1060, 1171, 1476, 1624]
stari_skok = dosada_zarazeni[-1] - dosada_zarazeni[-2]

def random_old():

    '''
    prvi sklepani random, nema distribucije
    '''
    prosli_dan = int(input())
    for i in range (10):
        prosli_dan = random.randrange(math.ceil((prosli_dan*1.15)), math.ceil(prosli_dan*1.25))
        print(prosli_dan)

'''        
def get_jump_list():
- krenuo sam da budžim nešto ovde pre nego što smo prešli na lognorm


    stari_skok_list = []
    for i in range(1, len(dosada_zarazeni)):
        i  = dosada_zarazeni[-i] - dosada_zarazeni[-i-1]
        stari_skok_list.append(i)

    return(len(stari_skok_list))
'''

def lognormalna(stari_skok=stari_skok,stari_broj=dosada_zarazeni[-1]):

    m=1.20
    s=0.05
    sln=np.sqrt(np.log(1+(s/m)**2))
    mln=np.log(m)-1/2*sln**2
    novi_skok=math.ceil(stari_skok*np.random.lognormal(mln,sln))
    print(stari_broj+novi_skok)
if __name__ == "__main__":
    for num in np.arange(len(dosada_zarazeni)-1):
        lognormalna(dosada_zarazeni[num+1]-dosada_zarazeni[num],dosada_zarazeni[num+1])