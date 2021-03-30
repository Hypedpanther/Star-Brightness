# Crating a record to store the stars
class stars:
    def __init__(self, star_name, star_brightness):
        self.star_name = star_name  # String
        self.star_brightness = star_brightness  # Int


stars_list = []


# getting data from the txt file
def get_data(stars_list):
    text_file = open('star-brightness.txt', 'r')
    for row in text_file:
        #use splitrows to read and append the data from file
        split_row = row.split(",")
        stars_list.append(stars(split_row[0], float(split_row[1])))
       
    return stars_list


# finding the brightest star
def find_brightest_star(stars_list):
    brightest_star = stars_list[0].star_brightness
    brightest_position = 0

    for loop in range(len(stars_list)):
        if brightest_star > stars_list[loop].star_brightness:  # brightest star has lowest number
            brightest_star = stars_list[loop].star_brightness
            brightest_position = loop
    return brightest_star, brightest_position


# display brightest star to output screen
def display_brightest_star(stars_list, brightest_star, brightest_position):
    print("The Brightest Star is:", stars_list[brightest_position].star_name, "With a Brightness of:", brightest_star)


# find the visible stars
def find_visible_stars(stars_list):
    for loop in range(len(stars_list)):
        if float(stars_list[loop].star_brightness) < 4.0:
          #Visible stars have a brightness of 4 or less
            print(stars_list[loop].star_name, stars_list[loop].star_brightness)


# save brightest stars to txt file
def save_to_file(stars_list):
    output_file = open('visiblestars.txt', 'w')
    for loop in range(len(stars_list)):
        if stars_list[loop].star_brightness < 4:
            output_file.writelines(stars_list[loop].star_name)
            output_file.writelines(",")
    print("Visible Stars Saved to File")
    output_file.close()

#main part of the program
stars_list = get_data(stars_list)
brightest_star, brightest_position = find_brightest_star(stars_list)
display_brightest_star(stars_list, brightest_star, brightest_position)
save_to_file(stars_list)
