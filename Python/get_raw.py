# Malik Ikhlef
def get_raw(num_ligne):
    assert type(num_ligne) == int, "The type of num_ligne must be int"
    with open ('data.csv', 'r', encoding= 'CP1252' ) as lng :
        lignes = lng.readlines()
        if 0 < num_ligne < len (lignes) : 
            print(lignes [num_ligne].strip())
        else :
            print ("Index out of range")


get_raw(12)
	
    
    
