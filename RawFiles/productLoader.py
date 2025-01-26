import sys
import csv

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


import mysql.connector


mydb = None
try:
    mydb = mysql.connector.connect(host='sql12.freesqldatabase.com',
        user='sql12759402',
        passwd='A5uyVKksjj',
        db='sql12759402'
    )
    print('Executed Correctly')
except:
    print('Files')

columns = [x for x in """timestamp,title,seller_name,brand,description,initial_price,final_price,currency,availability,reviews_count,categories,asin,
    ,buybox_seller,number_of_sellers,root_bs_rank,answered_questions,domain,images_count,url,video_count,image_url,item_weight,
    ,rating,product_dimensions,seller_id,date_first_available,discount,model_number,manufacturer,department,plus_content,upc,
    ,video,top_review,variations,delivery,features,format,buybox_prices,parent_asin,input_asin,ingredients,origin_url,bought_past_month,
    ,is_available,root_bs_category,bs_category,bs_rank,badge,subcategory_rank,amazon_choice,images,product_details,prices_breakdown,country_of_origin,
""".split(',') if '\n' not in x]

placeHolders = [ x for x in '''
    ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%f,
    ,%s,%s,%s,%f,%f,%f,%s,%d,%s,%d,%s,
    ,%s,%f,%s,%s,%s,%s,%s,%s,%s,%d,%s,
    ,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    ,%f,%s,%s,%s,%f,%s,%s,%s,%s,%f,%f,
    ,

'''.split(',') if '\n' not in x]

print(columns,len(columns))
print(placeHolders,len(placeHolders))

cursor = mydb.cursor()
# sql = # SQL INSERT statement for PRODUCT_TABLE
sql = """
INSERT INTO PRODUCT_TABLE (
    timestamp,
    title,
    seller_name,
    brand,
    description,
    initial_price,
    final_price,
    currency,
    availability,
    reviews_count,
    categories,
    asin,
    buybox_seller,
    number_of_sellers,
    root_bs_rank,
    answered_questions,
    domain,
    images_count,
    url,
    video_count,
    image_url,
    item_weight,
    rating,
    product_dimensions,
    seller_id,
    date_first_available,
    discount,
    model_number,
    manufacturer,
    department,
    plus_content,
    upc,
    video,
    top_review,
    variations,
    delivery,
    features,
    format,
    buybox_prices,
    parent_asin,
    input_asin,
    ingredients,
    origin_url,
    bought_past_month,
    is_available,
    root_bs_category,
    bs_category,
    bs_rank,
    badge,
    subcategory_rank,
    amazon_choice,
    images,
    product_details,
    prices_breakdown,
    country_of_origin
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)

"""

print(sql)

csv_data = ''
with open('./amazon-products.csv','r',encoding = "utf-8") as file:
    csv_data = csv.reader(file)
    for line in csv_data:
        cursor.execute(sql,line)

mydb.commit()
# for row in csv_data:

#     cursor.execute(sql.query)

#     cursor.execute('INSERT INTO testcsv(names, \
#           classes, mark )' \
#           'VALUES("%s", "%s", "%s")', 
#           row)
# #close the connection to the database.
# mydb.commit()
# cursor.close()
# # print "Done"

