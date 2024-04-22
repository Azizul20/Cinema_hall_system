class Star_Cinema:
    _hall_list = []
    
    def entry_hall(self,hall_obj):
        self._hall_list.append(hall_obj)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) :
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
        
    def entry_show(self,id,movie_name,time):
        show_info = (id,movie_name,time)
        self.__show_list.append(show_info)
        
        seat2D = [[0 for c in range(self._cols)] for r in range(self._rows)]
        self.__seats[id] = seat2D
    
    def book_seats(self,id,seat2d_tuple):
        if id not in self.__seats:
            print("Invalid show id")
            return
        seatmap = self.__seats[id]
        for seat in seat2d_tuple:
            row,col = seat
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print(f"Invalid seat {row},{col}")
                continue
            if seatmap[row-1][col-1] == 1:
                print(f"Seat {row},{col} is already booked")
            else:
                seatmap[row-1][col-1] = 1
                print(f"Seat {row},{col} booked successfully")
                
    def view_show_list(self):
        count = 1
        for show in self.__show_list:
            print(f"show : {count}")
            print("------------------")
            print(f"ID : {show[0]}")
            print(f"Movie : {show[1]}")
            print(f"Time : {show[2]}")
            print()
            count+=1
            
    def view_available_seats(self,id):
        if id not in self.__seats:
            print("Invalid show id")
            return
        count = 0
        seatmap = self.__seats[id]
        print(f"Available seats for show {id}: ")
        for i in range(self._rows):
            for j in range(self._cols):
                if seatmap[i][j]==0:
                    print(f"seat ({i+1}, {j+1}) is available")
                    count+=1
                elif seatmap[i][j]==1:
                    print(f"seat ({i+1}, {j+1}) is already booked")
        print(f"Number of available seats : {count}")
 
        
print()
print("""
        ------------------------
        |   Hall Information   |
        ------------------------
        """)
print()
print("Enter hall information: ")
print()
row = int(input("Enter row of hall : "))
col = int(input("Enter column of hall : "))
hallno = int(input("Enter hall no : "))
hall = Hall(row,col,hallno)
while True:
    print("""
            --------------------------------------------
                1. Enter the shows data
                2. View all shows
                3. View available tickets for a show
                4. Book tickets
                5. Exit
            ---------------------------------------------""")
    choice = input("Press a number : ")
    if choice == "1":
        print()
        print()
        while True:
            print("""
                    --------------------------------------------
                        1. Add Show Information:
                        2. Exit to add show Information
                    ---------------------------------------------""")
            print()
            print()
            c=input("Enter choice: ")
            if c =="1":
                h_id = input("Enter the hall id : ")
                movie = input("Enter the movie name : ")
                time = input("Enter the time of movie : ")
                hall.entry_show(h_id,movie,time)
                print()
                print("Add Show Information done.")
                print()
            else:
                break
    elif choice == "2":
        print()
        print("""
              ------------------------
              |   View Show Data     |
              ------------------------
              """)
        print()
        for show in Star_Cinema._hall_list:
            show.view_show_list()
    elif choice == "3":
        print()
        print("""
              ----------------------------------------
              |   View Available ticket for Show     |
              ----------------------------------------
              """)
        print()
        show_id = input("Enter the show id : ")
        hall.view_available_seats(show_id)
    elif choice == "4":
        print()
        print("""
              ------------------------
              |   Ticket Booking     |
              ------------------------
              """)
        print()
        show_id = input("Enter the ID of the show: ")
        num_seat = int(input("Enter the number of seats to book: "))
        seats_book = []
        for i in range(num_seat):
            row = int(input("Enter the row of the seat: "))
            col = int(input("Enter the column of the seat: "))
            seats_book.append((row, col))
        hall.book_seats(show_id, seats_book)
    elif choice == "5":
        print("Exit the system")
        break
    else:
        print("Invalid choice. Please Enter a valid choice.")
