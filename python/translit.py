
def letters():
    letters_az = 'a,b,c,ç,d,e,ə,f,g,ğ,h,x,i,ı,j,k,l,m,n,o,ö,p,'\
                'q,r,s,ş,t,u,ü,v,y,z,A,B,C,Ç,D,E,Ə,F,G,Ğ,H,X,İ,I,'\
                'J,K,L,M,N,O,Ö,P,Q,R,S,Ş,T,U,Ü,V,Y,Z, '
    letters_translit = 'a,b,c,ch,d,e,e,f,g,gh,h,x,i,i,j,k,l,m,n,o,o,p,'\
                'q,r,s,sh,t,u,u,v,y,z,A,B,C,CH,D,E,E,F,G,GH,H,X,I,I,'\
                'J,K,L,M,N,O,O,P,Q,R,S,SH,T,U,U,V,Y,Z,-'
    
    return {az : tr for az, tr in zip(letters_az.split(','), letters_translit.split(','))}


def translit(text: str, alphabet_dict):
    mkt = str.maketrans(alphabet_dict)
    return text.translate(mkt)

print(translit('Mənim adım Mətindir. 20 yaşım var.', letters()))