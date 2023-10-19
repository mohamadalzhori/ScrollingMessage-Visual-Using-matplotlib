import matplotlib.pyplot as plt
import time

# Initial values
message = "Welcome-Home !"
output = list(" " * 8)  
LENGTH = len(message)
INDEX = 0
OFFSET = 0
COUNTER = 0
START = 0
i = 0
# Number of columns on the "LCD"
lcd_columns = 8

fig, ax = plt.subplots()
lcd_text = ax.text(0.5, 0.5, "", fontsize=32, ha='center', va='center')
INDEX_text = ax.text(0, 0.1, "INDEX:", fontsize=12, ha='left', va='top')
OFFSET_text = ax.text(0, 0.2, "OFFSET:", fontsize=12, ha='left', va='top')
COUNTER_text = ax.text(0, 0.3, "COUNTER:", fontsize=12, ha='left', va='top')

ax.axis('off')

while OFFSET != 8:
    plt.pause(0.001)
    INDEX_text.set_text(f"INDEX: {INDEX}")
    OFFSET_text.set_text(f"OFFSET: {OFFSET}")
    COUNTER_text.set_text(f"COUNTER: {COUNTER}")
    
    output[INDEX] = message[OFFSET]
    lcd_text.set_text("".join(output))
    plt.savefig(f'images/{i:003}')
    i+=1
    OFFSET += 1
    INDEX +=1

COUNTER = 1
OFFSET = 1
INDEX = 0
while COUNTER+1<LENGTH:
    INDEX_text.set_text(f"INDEX: {INDEX}")
    OFFSET_text.set_text(f"OFFSET: {OFFSET}")
    COUNTER_text.set_text(f"COUNTER: {COUNTER}")

    plt.pause(0.001) 
    output[INDEX] = message[OFFSET]
    lcd_text.set_text("".join(output))
    plt.savefig(f'images/{i:005}', dpi = 100, facecolor = 'white')
    i+=1

    OFFSET += 1
    OFFSET_text.set_text(f"OFFSET: {OFFSET}")

    if OFFSET == LENGTH:
        OFFSET = 0

    INDEX += 1
    INDEX_text.set_text(f"INDEX: {INDEX}")
    if INDEX != lcd_columns:
        continue
    else:
        INDEX = 0
        COUNTER += 1
        COUNTER_text.set_text(f"COUNTER: {COUNTER}")
        if COUNTER == LENGTH:
            COUNTER = 0
        OFFSET = COUNTER
