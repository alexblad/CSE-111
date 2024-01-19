import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

def main():

    try: 
        print('Blad\'s Store of Wonder')
        print()

        products_dict=read_dict('products.csv', 0)

   #print(products_dict)

        PRODUCT_INDEX=0
        REQUEST_INDEX=1
        with open('request.csv', "rt") as request_file:
            reader=csv.reader(request_file)
        
            next(reader)
            items=[]
            subtotal=[]
            for row_list in reader:

                product_number=row_list[PRODUCT_INDEX]
                request_number=int(row_list[REQUEST_INDEX])

        

            #if product_number in products_dict: (This causes the exception for KeyValueError not to work)
                product_list=products_dict[product_number]

                price=product_list[2]
                product_name=product_list[1]
                
                print( product_name+ ': ' + str(request_number) +' @ '+price)

                items.append(request_number)
                subtotal.append(float(price)*float(request_number))

            total_items=sum(items)
            pretax=round(sum(subtotal),4)
            salestax=round(pretax*0.06,2)
            total=pretax+salestax


            print()
            print('Number of Items: ' + str(total_items))
            print('Subtotal: ' + str(pretax))
            print('Salestax: ' + str(salestax))
            print('Total: ' + str(total))
            print()
            print('Thank you for shopping at Blad\'s Store of Wonder')
            # Call the now() method to get the current
            # date and time as a datetime object from
            # the computer's operating system.
            current_date_and_time = datetime.now()

            # Print the current day of the week and the current time.
            print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
            #Format like Wed Nov  4 05:10:30 2020
            print()
            print('Tell us how we did today! Fill out a survey at\n'
            'www.surveyisreal.com, and you\'ll recieve a coupon for\n'
            '$5 off of your next purchase of $20 or more!\n')

    except (KeyError) as key_err:
        print('Error: unkown product ID in the request.csv file')
        print(key_err)
    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)

    

def read_dict(filename, key_column_index):
    
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
     # store the data from the CSV file.
    dictionary = {}

    with open(filename, "rt") as csv_file:

         reader = csv.reader(csv_file)


         next(reader)


         for row_list in reader: 

            
            if len(row_list) != 0:

                key=row_list[key_column_index]

                dictionary[key]=row_list

    return dictionary

if __name__ == "__main__":
    main()