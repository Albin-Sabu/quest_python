veg_food_items = {

    1 : 'Mysuru Filter Coffee',

    2 : 'Yummy Idly-vada',

    3 : 'Worlds soft Mysuru Mailari Dosa',

    4 : 'Bhupal Special Poha',

    5 : 'Bengaluru tamato-peanuts Upama'

}
nonveg_food_items = {

    1 : 'Malabar dum Biriyani',

    2 : 'Kerala Porotta and Beef',

    3 : 'Arabic Shavarma'

}
print('Welcome to our hotel Rameshwaram Cafe')

print('For veg orders please enter 1 , for non-veg orders please enter 2')

food_item_number = int(input('Enter the food type item number that you wish:'))

if food_item_number == 1:
    print('1:Coffee 2:Idly-Vada 3:Dosa 4:Poha 5:Upama')
    food_item_code = int(input('Enter the food item number that you wish:'))
    if food_item_code < 1 or food_item_code > 5:
        print('Invalid choice entered')
    else:
        print('Your ' + veg_food_items.get(food_item_code) + ' is here')

elif food_item_number ==2:
    print('1:Biriyani 2:Porotta-beef 3:Shavarma')
    food_item_code = int(input('Enter the food item number that you wish:'))
    if food_item_code < 1 or food_item_code > 3:
        print('Invalid choice entered')
    else:
        print('Your ' + nonveg_food_items.get(food_item_code) + ' is here')

else:
    print('Invalid choice entered')

print('Thank you, Visit again')