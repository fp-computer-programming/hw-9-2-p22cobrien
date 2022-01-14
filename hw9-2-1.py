# Author: CMOB 1/12/2022

#from ast import Delete
#from email.encoders import encode_noop


rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin","Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
last_initials = ["B.","D.","H.","E.","G.","G.","H.","R.","M.","L.","I.","I.","N.","N.","O.","P.","P.","X.","T.","S.","S.","P."]

for row in rows:
    for index, value in enumerate(row):
        row[index] = "{0} {1}".format(value,last_initials[0])
        del last_initials[0]


print(rows)

