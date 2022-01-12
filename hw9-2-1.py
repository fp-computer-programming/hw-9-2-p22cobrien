# Author: CMOB 1/12/2022

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin" "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
last_initials = [["B.","D.","H.","E.","G.","G.","H."],["R.","M.","L.","I.","I."],["N.","N.","O.","P.","P."],["X.","T.","S.","S.","P."]]
x = 0
for row in rows:
    for names in rows:
        names = names + last_initials[x]
        x += 1