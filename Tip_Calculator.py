print("Welcone to the tip calculator")
bill=float(input("what is your bill?\n$"))
tip=int(input("what is your tip?\n$"))
split=int(input("what is your split?\n"))
tip_as_persents=tip/100
total_tip_amount=bill*tip_as_persents
total_bill=bill+total_tip_amount
bill_per_person=total_bill/split
final_split_amount=round(bill_per_person,2)
print(f"Each person should pay :${final_split_amount}")
