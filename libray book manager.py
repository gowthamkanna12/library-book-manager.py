libray=[]
while True:
 print("library book manager opition:")
 print("1.add book")
 print("2.view book")
 print("3.search book")
 print("4.remove book")
 print("5.count book")
 print("6.save book to file")
 print("7.load book from file")
 print("8.exit")
 count=0
 try:
  choise=int(input("enter your choise:"))
 except:
  print("wrong input")
  print("try again")
  continue
 if choise==1:
  print("adding a book")
  book_name=input("enter the book name:")
  libray.append(book_name)
  print("book added")
 elif choise==2:
  print("viewing book")
  for lib in libray:
   print(lib)
 elif choise==3:
  print("searching book")
  data=input("enter book name:")
  for lib in libray:
   if data==lib:
    print("found")
    break
  else:
    print("not found")
 elif choise==4:
  print("removing book")
  name=input("enter book name:")
  for lib in libray:
   if name==lib:
    libray.remove(lib)
    print("removed")
    break
  else:
   print("not found")
   continue
 elif choise==5:
  print("counting")
  print("count:",len(libray))
 elif choise==6:
  print("saving book to file")
  file=open("data.txt","w")
  for book in libray:
   file.write(book + "\n")
  file.close()
  print("book saved successfully")
 elif choise==7:
   libary.clear()
   file = open("data.txt", "r")
   for line in file:
    libray.append(line.strip())
   print(libray)
   file.close()
   print("Books loaded successfully")
 else:
  if choise==8:
   print("thank you for using library book manager")
   break
 
   