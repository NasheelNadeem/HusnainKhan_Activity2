#Nasheel's Github: https://github.com/NasheelNadeem/Activity2
#Husnain's Github: https://github.com/Iblamehussi/HusnainKhan_Activity2
import turtle

#Function to get color from character
def get_color(char):
    if char == '0':
        return 'black'
    elif char == '1':
        return 'white'
    elif char == '2':
        return 'red'
    elif char == '3':
        return 'yellow'
    elif char == '4':
        return 'orange'
    elif char == '5':
        return 'green'
    elif char == '6':
        return 'yellowgreen'
    elif char == '7':
        return 'sienna'
    elif char == '8':
        return 'tan'
    elif char == '9':
        return 'gray'
    elif char == 'A':
        return 'darkgray'
    return None  # Return None if character is not recognized

#Function to draw a colored pixel
def draw_color_pixel(color, turta):
    turta.fillcolor(color)
    turta.begin_fill()
    for _ in range(4):  # Draw pixel
        turta.forward(20)
        turta.right(90)
    turta.end_fill()
    turta.forward(20)  # Draw the next pixel

#Function to draw a coloured pixel
def draw_pixel(char, turta):
    color = get_color(char)
    if color:
        draw_color_pixel(color, turta)

#Function to draw a line from a string of characters
def draw_line_from_string(color_string, turta):
    for char in color_string:
        if get_color(char):
            draw_pixel(char, turta)
        else:
            return False  # Stop if invalid character
    return True

#Function to read the file and draw a shape from the file
def draw_shape_from_file(turta, filename):
    try:
        with open(filename, 'r') as f:
            y = 0  # Starting y-position offset
            for line in f:
                line = line.strip()  #Remove whitespaces
                if not draw_line_from_string(line, turta):
                    print("Invalid character in file, stopping.")
                    break
                
                # Moving turtle down after each line
                turta.penup()
                y += 20  # Move down by 20 units for each row
                turta.goto(-200, 200 -y)  # Reset to next line starting position
                turta.pendown()
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please ensure it is in the same directory as this script.")


def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)  #canvas size
    
    turta = turtle.Turtle()
    turta.speed(0)  #Fast speed for turtle
    turta.penup()
    turta.goto(-200, 200)  # Starting position
    turta.pendown()

    # Prompt for the filename
    filename = input("Enter the file name: ")
    draw_shape_from_file(turta, filename)

    turtle.done()  # Keeps the turtle window open

if __name__ == "__main__":
    main()
