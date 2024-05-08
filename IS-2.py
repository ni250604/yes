import math

key=input("Enter Key:")

def encrypt(msg):
 key_index=0
 cipher=""
 msg_list=list(msg)
 col=len(key)
 row=int(math.ceil(len(msg_list)/col))
 fill_null=int((col*row)-len(msg_list))
 msg_list.extend('_'*(fill_null))
 sort_key=sorted(key)
 matrix=[]

 for i in range(0,len(msg_list),col):
  sub=msg_list[i:i+col]
  matrix.append(sub)

 for _ in range(col):
  curr_char=sort_key[key_index]
  curr_index=key.index(curr_char)
  cipher+=''.join([row[curr_index] for row in matrix])
  key_index+=1
 return cipher


def decrpyt(c):
 key_index=0
 plain_text=0
 msg_index=0
 c_list=list(c)
 sort_key=sorted(key)
 col=len(key)
 row=int(math.ceil(len(c_list)/col))
 dec_cipher=[]
 for _ in range(row):
  dec_cipher+=[[None]*col]

 for _ in range (col):
  curr_char=sort_key[key_index]
  curr_index=key.index(curr_char)
  for j in range(row):
   dec_cipher[j][curr_index]=c_list[msg_index]
   msg_index+=1
  key_index+=1

 plain_text=''.join(sum(dec_cipher,[]))
 null_count=plain_text.count('_')
 if(null_count>0):
  plain_text=plain_text[:-null_count]
 return plain_text


msg=input("Enter Message: ")
c=encrypt(msg)
print(c)
# plain_text=(decrpyt(c))
# print(plain_text)











