from tkinter import *

dfa = {
    0: {'d': 1, 'space' : 0, '.' :0 , 'comma' : 0 },
    1: {'d': 1, 'comma' : 0 , '.':0, 'space':2, 'r':16, 't':16},
    2: {'s':3, 'A':10 , 'm':12, 'y':19},
    3: {'e':4, 'q' : 7},
    4: {'p':5},
    5: {'t':6},
    6: {'sept':6, 'space': 6, 'd':1},
    7: {'u':8, 'space' : 9},
    8: {'square':8,'space':8},
    9: {'sqmi':9},
    10: {'u':11},
    11: {'aug':11 , 'space': 6 , 'd':1},
    12: {'i':13, 'e':17},
    13: {'l':14},
    14: {'l':15},
    15: {'million':15, 'comma':0},
    16: {'d':16, 'h':16, 'space':0},
    17: {'g':18},
    18: {'diverse':18 , 'space' : 0},
    19: {'e':20},
    20: {'years':20, '.':0, 'comma':0}

}

def simulate_dfa(input_string):
    # Start at the initial state of the DFA
    state = 0
    # Keep track of the occurrences of the pattern
    count = 0
    # Initialize the output string
    output = ''

    root = Tk()
    root.title('After DFA')
    root.config(bg='#D9D8D7')
    root.geometry('400x300')
    text = Text(root)
    text.insert(INSERT, "TEXT AFTER DFA\n\n")
    # Iterate through each character in the input string
    for i, c in enumerate(input_string):

        #NUMBERS ONLY (done)
        if c.isdigit():
            state = dfa[state].get('d', -1)

        elif c.isspace():
            state = dfa[state].get('space', -1)

        elif c == ',':
            state = dfa[state].get('comma', -1)

        elif c == '.':
            state = dfa[state].get('.', -1)
      
        #rd & th
        elif state == 1:
            if c == 'r':
                state = dfa[state].get('r', -1)
            if c == 't':
                state = dfa[state].get('t', -1)
        elif state == 16:
            if c == 'd':
                state = dfa[state].get('d', -1)
            elif c == 'h':
                state = dfa[state].get('h', -1)

        #Sept (done)
        elif state == 2:
            if c == 's' or c == 'S':
                state = dfa[state].get('s', -1)
            elif c == 'A':
                state = dfa[state].get('A', -1)
            elif c == 'm':
                state = dfa[state].get('m', -1)
            elif c == 'y':
                state = dfa[state].get('y', -1)
            else:
                state = 0

        elif state == 3:
            if c == 'e':
                state = dfa[state].get('e', -1)
            elif c == 'q':
                state = dfa[state].get('q', -1)

        elif state == 4:
            if c == 'p':
                state = dfa[state].get('p', -1)

        elif state == 5:
            if c == 't':
                state = dfa[state].get('t', -1)

        elif state == 6:
            if c == 'e' or c == 'm' or c == 'b' or c == 'r':
                state = dfa[state].get('sept', -1)
            else:
                state = 0


        #Square (done)

        elif state == 7:
            if c == 'u':
                state = dfa[state].get('u', -1)
        elif state == 8:   
            if c == 'a' or c == 'r' or c == 'e' or c == 'k' or c == 'i' or c == 'l' or c =='o' or c =='m' or c =='t' or c == 's':
                state = dfa[state].get('square', -1)
            else:
                state = 0

        #August (done)
        elif state == 10:
            if c == 'u':
                state = dfa[state].get('u', -1)
        elif state == 11:   
            if c == 'g' or c == 'u' or c == 's' or c == 't':
                state = dfa[state].get('aug', -1)
            else:
                state = 0


        #Million (done)
        elif state == 12:
            if c == 'i':
                state = dfa[state].get('i', -1)
            elif c == 'e':
                state = dfa[state].get('e', -1)
            else:
                state = 0
        elif state == 13:
            if c == 'l':
                state = dfa[state].get('l', -1)
        elif state == 14:
            if c == 'l':
                state = dfa[state].get('l', -1)
        elif state == 15:   
            if c == 'i' or c == 'o' or c == 'n':
                state = dfa[state].get('million', -1)
            else:
                state = 0

        #megadiverse(done)

        elif state == 17:
            if c == 'g':
                state = dfa[state].get('g', -1)
            else:
                state = 0

        elif state == 18:   
            if c == 'a' or c == 'd' or c == 'i' or c == 'v' or c == 'e' or c == 'r' or c == 's' or c == 'e':
                state = dfa[state].get('diverse', -1)
            else:
                state = 0

        #years

        elif state == 19:
            if c == 'e':
                state = dfa[state].get('e', -1)
            else:
                state = 0

        elif state == 20:  
            if c == 'a' or c == 'r' or c == 's':
                state = dfa[state].get('years', -1)
            else:
                state = 0


        #sqmi(done)
        elif state == 9:   
            if c=='m' or c=='i':
                state = dfa[state].get('sqmi', -1)
            else:
                state = 0



        if state == -1:
            output += '\nInput terminated at position {} due to invalid character {}'.format(i, c)
            break

        if state==0:
            text.insert(INSERT, c)

        else:
            count += 1
            text.insert(INSERT, c, 'blue_tag')
            text.tag_configure('blue_tag', foreground='blue')
            
    if count > 0:
        status = 'Accepted'
    else:
        status = 'Rejected'

    text.insert(END, '\n\n')
    text.insert(INSERT, "TEXT BEFORE DFA\n\n")
    text.insert(INSERT, input_string,)
    text.insert(END, '\n\n')
    text.insert(INSERT, 'Status :')
    text.insert(INSERT, status)
    text.insert(INSERT, "\nOccurance of the Pattern :")
    text.insert(INSERT, count)

    text.pack(expand=1, fill =BOTH)

    root.mainloop()

# Test the program with the given sample text
sample_text = 'Malaysia is a federal constitutional monarchy located in Southeast Asia. It consists of thirteen states and three federal territories and has a total landmass of 329,847 square kilometres (127,350 sq mi) separated by the South China Sea into two similarly sized regions, Peninsular Malaysia and East Malaysia (Malaysian Borneo). Peninsular Malaysia shares a land and maritime border with Thailand and maritime borders with Singapore, Vietnam, and Indonesia. East Malaysia shares land and maritime borders with Brunei and Indonesia and a maritime border with the Philippines. The capital city is Kuala Lumpur, while Putrajaya is the seat of the federal government. By 2015, with a population of over 30 million, Malaysia became 43rd most populous country in the world. The southernmost point of continental Eurasia, Tanjung Piai, is in Malaysia, located in the tropics. It is one of 17 megadiverse countries on earth, with large numbers of endemic species. Malaysia has its origins in the Malay kingdoms present in the area which, from the 18th century, became subject to the British Empire. The first British territories were known as the Straits Settlements, whose establishment was followed by the Malay kingdoms becoming British protectorates. The territories on Peninsular Malaysia were first unified as the Malayan Union in 1946. Malaya was restructured as the Federation of Malaya in 1948, and achieved independence on 31 August 1957. Malaya united with North Borneo, Sarawak, and Singapore on 16 September 1963, with is being added to give the new country the name Malaysia. Less than two years later in 1965, Singapore was expelled from the federation. Since its independence, Malaysia has had one of the best economic records in Asia, with its GDP growing at an average of 6.5% per annum for almost 50 years. The economy has traditionally been fuelled by its natural resources, but is expanding in the sectors of science, tourism, commerce and medical tourism. Today, Malaysia has a newly industrialised market economy, ranked third largest in Southeast Asia and 29th largest in the world. It is a founding member of the Association of Southeast Asian Nations, the East Asia Summit and the Organisation of Islamic Cooperation, and a member of Asia-Pacific Economic Cooperation, the Commonwealth of Nations, and the Non-Aligned Movement'
sample_text_two = 'In just a span of 5 years, which is from 2018 to 2023, the once-empty plot of land has transformed into a bustling neighborhood, spanning over 1000 square metres (approx.) and it all began on a sunny September day, precisely on the 15 September 2018, when the groundbreaking ceremony marked the beginning of an ambitious construction project. The air buzzed with excitement and anticipation as the foundation stone was laid, symbolizing the dreams and aspirations that would soon take shape. With each passing year, the site witnessed remarkable progress. Skilled workers and dedicated architects worked tirelessly, their efforts shaping the landscape with precision and artistry. Towering buildings rose from the ground, reaching for the sky, while lush green spaces emerged to provide an oasis amidst the urban chaos. The infrastructure expanded as roads extended, connecting the ever-expanding community and paving the way for seamless movement. As the calendar turned, each September brought a sense of celebration and reflection. Year 1 year, the neighborhood flourished and evolved, welcoming new residents, businesses, and a vibrant mix of cultures. From the humble beginnings of the construction site, it blossomed into a diverse and inclusive community that fostered a sense of belonging and togetherness. Today, on the 5th anniversary in 2023, it is a testament to the collective effort and vision that has shaped this remarkable development. The once-barren land now teems with life, laughter, and the hum of activity. Families stroll along the tree-lined streets, children play in the sprawling parks, and local businesses thrive, serving as the heartbeat of the neighborhood. The journey of these 5 years, from 2018 to 2023, has not been without challenges, but it is the resilience and determination of the community that have propelled this transformation forward. As the sun sets on this memorable day, we look back with gratitude and look forward with anticipation, knowing that the next 5 years, from 2023 to 2028, will bring even more growth, progress, and cherished memories in this vibrant, ever-evolving neighborhood.'
sample_text_three = 'The whimsical cat chased a floating bubble through the sunlit garden, its tail swishing with excitement. The vibrant flowers danced in the gentle breeze, their petals displaying a kaleidoscope of colors. Meanwhile, a group of giggling children gathered around a small lemonade stand, their voices carrying the pure joy of carefree summer days. Nearby, a solitary writer sat beneath the shade of a towering oak tree, scribbling furiously in a weathered notebook, captivated by the flow of ideas. As the day progressed, the sky transformed into a canvas of pink and gold hues, signaling the arrival of a breathtaking sunset. Natures symphony filled the air, as chirping birds bid farewell to the fading light. Amidst this enchanting scene, a sense of tranquility settled upon the surroundings, leaving everyone in awe of the simple yet profound beauty of the world around them.'
simulate_dfa(sample_text_three)