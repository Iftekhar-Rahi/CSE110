book_info = ( ("Best Mystery & Thriller","The Silent Patient",68821),
              ("Best Horror","The Institute",75717),
              ("Best History & Biography","The five",31783 ),
              ("Best Fiction","The Testaments",98291) )
#The Silent Patient won the 'Best Mystery & Thriller' category with 68821 votes
for i in book_info:
    g,b,v=i
    print(f"{b} won the '{g}' category with {v} votes")