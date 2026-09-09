#Exercise 1 : Student Grade Summary

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}

for student, grades in student_grades.items():
    
    average = round(sum(grades) / len(grades), 2)
    student_averages[student] = average

    if average >= 90:
       student_letter_grades[student] = "A"

    elif 80 <= average <= 89:
       student_letter_grades[student] = "B"

    elif 70 <= average <= 79:
        student_letter_grades[student] = "C"

    elif 60 <= average <= 69:
        student_letter_grades[student] = "D"

    else:
        student_letter_grades[student] = "E"
   
all_averages = student_averages.values()
total_sum = sum(all_averages)
total_students = len(student_averages)
class_average = round(total_sum / total_students, 2)

print(f"Class average is {class_average}")
print("\nStudent Reports:")

for student in student_averages:
    average = student_averages[student]
    letter  = student_letter_grades[student]

    
    print(f"{student}: Average = {average}, Grade = {letter}")


#Exercise 2 : Advanced Data Manipulation and Analysis

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

product_sales = {}

for sale in sales_data:
    product = sale["product"]
    price = sale["price"]
    quantity = sale["quantity"]
    revenue = price * quantity

    if product in product_sales:
       product_sales[product] += revenue

    else:   
       product_sales[product] = revenue

print(product_sales)

