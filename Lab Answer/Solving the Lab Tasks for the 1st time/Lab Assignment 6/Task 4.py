book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291))
for i in book_info:
  g,n,v=i
  print(f"{n} won the '{g}' category with {v} votes")