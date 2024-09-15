from django.http import HttpResponse
from django.shortcuts import render, redirect
import time
import random
import barcode
# import EAN13 from barcode module 
from barcode import EAN13 
  
# import ImageWriter to generate an image file 
from barcode.writer import ImageWriter 

from . import models
con = models.mydb
cursor = con.cursor()


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def generate_unique_barcode():
    while True:
        barcode_number = ''.join(random.choices('0123456789', k=12))
        cursor.execute("SELECT barcode_number FROM register WHERE barcode_number = %s", (barcode_number,))
        if cursor.fetchone() is None:
            return barcode_number


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"output": ""})
    else:
        name = request.POST.get("name")
        buying_prize = request.POST.get("buying_prize")
        address = request.POST.get("address")
        city = request.POST.get("city")
        selling_prize = request.POST.get("selling_prize")
        info = time.asctime()

        # Generate a unique 12-digit barcode number
        barcode_number = generate_unique_barcode()

        # Now, let's create an object of EAN13 class and  
        # pass the barcode_number with the ImageWriter() as the writer 
        my_code = EAN13(barcode_number, writer=ImageWriter()) 
        
        # Our barcode is ready. Let's save it.
        file_path = f"./mydjapp/media/barcodes/barcode_{barcode_number}"
        my_code.save(file_path)
        print(barcode_number)
        sql = "INSERT INTO register VALUES(NULL, %s, %s, %s, %s, %s, 0, 'user', %s, %s)"
        val = (name, buying_prize, address, city, selling_prize, info, barcode_number)

        try:
            # execute query
            cursor.execute(sql, val)

            # commit changes in database
            con.commit()

            return render(request, "register.html", {"output": "User registered successfully....", "barcode_image_path": file_path, "barcode_number": barcode_number})
        except Exception as e:
            return render(request, "register.html", {"output": f"Error: {e}"})
        
def search(request):
    if request.method == "GET":
        return render(request, "search.html", {"output": ""})
    else:
        # extract form data
        barcode_number = request.POST.get("barcode")

        # query to fetch user details from the database
        sql = "SELECT * FROM register WHERE barcode_number=%s"
        val = (barcode_number,)

        cursor.execute(sql, val)
        user = cursor.fetchone()

        if user:
            # If a user with the provided barcode number exists in the database
            userhome= {
                "name": user[1],
                "buying_prize": user[2],
                "address": user[3],
                "city": user[4],
                "selling_prize": user[5],
                "info": user[8],
                # Add more fields as needed
            }
            return render(request, "userhome.html", {"userhome": userhome})
        else:
            # If no user with the provided barcode number is found
            return render(request, "search.html", {"output": "Invalid barcode number. Please try again."})




def myadmin(request):
    return render(request, "adminhome.html")


def manageusers(request):
    sql = "SELECT * FROM register WHERE role='user'"
    cursor.execute(sql)
    userDetails = cursor.fetchall()
    return render(request, "manageusers.html", {"userDetails": userDetails})


def user(request):
    return render(request, "userhome.html")
