import io
import TV
# Lovisa Colérus
# 2015

#läser in filen för att ha grundinfo när programmet startas. Skapar en hashtabell över tv-objekten för att underlätta menyvalen senare
def las_sparad_TV_fil():
    file = open ('Tv-lista.txt', 'r')
    TV_fil = []
    TV_apparater = []
    tv_namn_lista = []
    j =0
    
    for i in file: 
        TV_fil.append(i.strip())
        
    while(j < len(TV_fil)-2):
        tv = TV.TV(TV_fil[j], TV_fil[j+1], TV_fil[j+2])
        TV_apparater.append(tv)        
        tvNamn = TV_fil[j]        
        tv_namn_lista.append(tvNamn)
        j=j+3
               
    parvis = zip(tv_namn_lista, TV_apparater)
    TV_hashtabell = dict(parvis)
    file.close()
    return TV_hashtabell
    
    
    
#Sparar all ny info till filen innan programmet avslutas
def spara_till_fil(TV_hashtabell):
    file = open ('Tv-lista.txt', 'w')
    TV_lista = TV_hashtabell.values()
    
    for i in TV_lista:
        file.write(str(i))
    
    file.close()

#för inmatning av menyval för att undvika duplicerad kod    
def val_av_siffra():
    while(True):
    
        try:
            menyVal = int(input("Välj en siffra: "))
            break
        except ValueError:
            print('Måste vara ett valbart heltal!')
            
    return menyVal        
    
#Skriver ut listan över valbara kanaler
#return lista över kanalerna    
def skriv_kanaler():
    kanaler = ['MTv: Music is life', 'Tv 3: Har du tur i kärlek?', 'Svt 1: Pengar är inte allt', 'Kanal 4: Vem vill inte bli miljonär?']
        
    for i in range(len(kanaler)):
        #j = i+1
        print((i+1), kanaler[i])
        
    return kanaler
        
      
        
#huvudmenyn, main som kör programmet
def huvud_meny():
    TV_hashtabell = las_sparad_TV_fil()  
    
    while(True):
        print ('***Välkommen till TV-simulatorn, vi har två TV-apparater som kan användas i simuleringen**** \n'+'1: VardagsrumsTV \n'+'2: KöksTV \n'+'3: Avsluta')
        
        menyVal = val_av_siffra()
        if menyVal == 1:
            tv = TV_hashtabell.get('VardagsrumsTV')
            print(tv)
            under_meny(tv)
        elif menyVal == 2:
            tv = TV_hashtabell.get('KöksTV')
            print(tv)
            under_meny(tv)
        elif menyVal == 3:
            spara_till_fil(TV_hashtabell)
            print('Simuleringen avslutas')
            break
        else:
            print('Fel val, försök igen!')
            
#Undermenyn till ett tv-objekt        
def under_meny(TV):
    while(True):
        print ('1: Byt Kanal \n'+'2: Sänk Ljudvolym \n'+'3: Höj Ljudvolym \n'+'4: Gå till huvudmenyn')
        
        menyValUndermeny = val_av_siffra()
        if menyValUndermeny == 1:
            kanaler = skriv_kanaler()
            while(True):
                try:
                    ny_kanal = int(input('Välj: '))
                except ValueError:
                   pass
                
                if TV.byt_kanal(ny_kanal, kanaler):
                    print('kanalen har bytts')
                    break
                print('fel inmatning')    
        elif menyValUndermeny == 2:
            TV.sank_volym()
            print('Volymen är nu ', TV.volym)
        elif menyValUndermeny == 3:
            TV.hoj_volym()
            print('Volymen är nu ', TV.volym)
        elif menyValUndermeny == 4:
            break
        else:
            print('Fel val, försök igen!')
    

huvud_meny()    
        
