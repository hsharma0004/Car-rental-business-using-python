class my_trip():
 global c
 def my_trip1(self):
    global city1
 
    print('Our Serivces available for: ')
    print('Kolhapur, Pune, Mumbai, Goa, Banglore, Indore from Nagpur')
    city = input('Enter your destination for further details: ')
    city1 = city.lower()
    c = ['kolhapur','pune','mumbai','indore','goa','banglore']
    car_list = ['bolero','marazzo','fortuner','innova','venue','scorpio','tavera','creta']
    if c[0] in city1:
        print('Cars available for Kolhapur:')
        print(car_list[3],car_list[4])
        print(f"From Nagpur to Kolhapur the cost of KM's travelling would be : 12,000 INR")
    elif c[1] in city1:
        print('Cars available for Pune:')
        print(car_list[1],car_list[3])
        print(f"From Nagpur to Pune the cost KM's travelling would be : 15,000 INR")
    elif c[2] in city1:
        print('Cars available for Mumbai:')
        print(car_list[0],car_list[2])
        print(f"From Nagpur to Mumbai the cost KM's travelling would be : 20,000 INR")
    elif c[3] in city1:
        print('Cars available for Indore:')
        print(car_list[0],car_list[6])
        print(f"From Nagpur to Indore the cost KM's travelling would be : 14,000 INR")
    elif c[4] in city1:
        print('Cars available for Goa:')
        print(car_list[5],car_list[3])
        print(f"From Nagpur to Goa the cost KM's travelling would be : 21,000 INR")
    elif c[5] in city1:
        print('Cars available for Banglore:')
        print(car_list[2],car_list[7])
        print(f"From Nagpur to Banglore the cost KM's travelling would be : 18,000 INR")
    else:
        print('No Service available for this place')
obj1=my_trip()
#my_trip()
class my_trips(my_trip):

 
 def car(self):
    global rentcar
    car_name = input('Enter the name of car by which you want to travel\n')
    rentcar= car_name.lower()
    car_list = ['bolero','marazzo','fortuner','innova','venue','scorpio','tavera','creta']
    if car_list[0] in rentcar:
       print('Your car expense would be : 4,000')
    elif car_list[1] in rentcar:
       print('Your car expense would be : 5,000')
    elif car_list[2] in rentcar:
        print('Your car expense would be : 8,000')
    elif car_list[3] in rentcar:
        print('Your car expense would be : 7,000')
    elif car_list[4] in rentcar:
        print('Your car expense would be : 5,000')
    elif car_list[5] in rentcar:
        print('Your car expense would be : 3,000')
    elif car_list[6] in rentcar:
        print('Your car expense would be : 5,000')
    elif car_list[7] in rentcar:
        print("Your car expense would be : 6,000")
obj2=my_trips()
#car()

class my_charges(my_trips):
 
 
 def charges(self):
    global rentcar   

    c = ['kolhapur','pune','mumbai','indore','goa','banglore']
    car_list = ['bolero','marazzo','fortuner','innova','venue','scorpio','tavera','creta']
    if c[0] in city1:
        if car_list[3] in rentcar:
             print('Your Total travel expense will be :19,000')
        elif car_list[4] in rentcar:
            print('Your tottal travel expense will be: 17,000')
    elif c[1] in city1:
        if car_list[1] in rentcar:
            print('Your Total travel expense will be : 20,000') 
        elif car_list[3] in rentcar:
            print('Your Total travel expense will be : 23,000')
    elif c[2] in city1:
        if car_list[0] in rentcar:
            print('Your Total travel expense will be : 24,000') 
        elif car_list[2] in rentcar:
            print('Your Total travel expense will be : 28,000')   
    elif c[3] in city1:
        if car_list[0] in rentcar:
            print('Your Total travel expense will be : 18,000')
        elif car_list[6] in rentcar:
            print('Your Total travel expense will be :19,000')
    elif c[4] in city1:
        if car_list[5] in rentcar:
            print('Your Total travel expense will be : 24,000')
        elif car_list[3] in rentcar:
            print('Your Total travel expense will be : 28,000')
    elif c[5] in city1:
        if car_list[2] in rentcar:
            print('Your Total travel expense will be : 26,000')
        elif car_list[7] in rentcar:
            print('Your Total travel expense will be : 24,000')

obj3=my_charges()

obj1.my_trip1()
obj2.car()
obj3.charges()