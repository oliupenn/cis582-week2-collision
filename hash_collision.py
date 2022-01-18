import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    collided = False
    while not collided:
        x = os.urandom(2)
        y = os.urandom(2)
        if x != y:
            hashed_x = hashlib.sha256(x).hexdigest()
            hashed_y = hashlib.sha256(y).hexdigest()
            if k % 4 == 0:
                num_digits_hex = int(k/4)
            else:
                num_digits_hex = int(k/4)+1
            hashed_trimmed_x = hashed_x[-num_digits_hex:]
            hashed_trimmed_y = hashed_y[-num_digits_hex:]
            collided = is_collided(hex_to_bin(hashed_trimmed_x),hex_to_bin(hashed_trimmed_y),k)
    return(x,y)

def is_collided(x,y,k):
    res = True
    for i in range(k):
        if (x[len(x)-i-1] != y[len(y)-i-1]):
            res = False
    return res

def hex_to_bin(x):
    length = len(x)
    res = int(x,16)
    res = bin(res)
    res = res[2:]
    length_diff = length*4 - len(res)
    if length_diff != 0:
        for i in range(length_diff):
            res = '0'+res       
    return res


if __name__ == "__main__":
    print(hash_collision(20))
    
