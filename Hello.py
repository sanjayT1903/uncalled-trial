import streamlit as st
import os
from transformers import pipeline
from bs4.element import Comment
from bs4 import BeautifulSoup


st.title("Scan your Insta Comments and use AI to keep yourself safe!")
st.subheader("")
"""

"""

import google.generativeai as palm

model = pipeline("sentiment-analysis")
def aiHelper(inputer):
    palm.configure(api_key="AIzaSyCHHmecpNDam9V3qPC52FbcBgHkhLnSOeA")
    
    defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  #'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":4},{"category":"HARM_CATEGORY_TOXICITY","threshold":4},{"category":"HARM_CATEGORY_VIOLENCE","threshold":4},{"category":"HARM_CATEGORY_SEXUAL","threshold":4},{"category":"HARM_CATEGORY_MEDICAL","threshold":4},{"category":"HARM_CATEGORY_DANGEROUS","threshold":4}],
 }
    input = inputer
    prompt = f"""Keep in mind these are old social media comments, You are to rate comments from a 1-10, where 10 is the worst thing a human could say while 1 is normal statements. Anything to be racially offensive for sexual should be above 5 while most other things should be lower!
    input: Out of 1-10 where 10 is the most inappropriate statement 1 being least - @turtleseal Next time I got a post abt the Swim Team I’ll add it
    sanjay_thasma
    Ahhhhhhh
    Gay
    Group A messed up
    lol alex looks gay
    output: 9 - The term gay in this context can be seen as highly offensive
    input: Out of 1-10 where 10 is the most inappropriate statement 1 being least - @turtleseal Next time I got a post abt the Swim Team I’ll add it
    sanjay_thasma
    Eating poop tastes so good
    You are weird
    output: 5- Eating poop is an inappropriate for talking but not necessarily horrible
    input: I would love to see you shirtless
    output: 4 - It is normal to want to see someone shirtless but it is a bit inappropriate to say out loud and can make people uncomfortable
    input: I hate black people
    output: 10 - Hate speech is not tolerated
    input: sanjay_thasma
    Ahhhhhhh
    Gay
    Group A messed up
    lol alex looks gay
    output: 8- Gay is a derogatory term and is offensive to a lot of people
    input: I love eating muffins
    output: 1 - There is nothing wrong with this statement
    input: Am I the only one who noticed how much more fair she looks in the sign. Lol
    output: 2 - It is not appropriate to comment on someone's skin color.
    input: Damn 🔥🔥🔥🔥🔥
    output: 3 - It is not appropriate to objectify a person and make them feel like a piece of meat
    input: I want to see you naked
    output: 7 - It is normal to want to see someone naked but it is a bit inappropriate to say out loud
    input: @shaggy856 stop hating cuz u too lazy and wanna stay broke.
    output: 5 - This is a personal attack and is not appropriate
    input: Why u playing on a phone. Weirdo. Play on anything but that and i will respect u more 
    output: 5 - calling someone a weirdo is not appropriate
    input: So how many of those girls are yours. 🥵🥵🥵
    output: 8 - It is not appropriate to objectify a person and make them feel like a piece of meat
    input: When you start wearing silk jackets, thats going to be the end of fashion. Nothing is more respectable than silk clothes 
    output: 2 - There is nothing wrong with this statement
    input:  can’t believe you called them your boys. I would be ashamed. Smh my head 
    output: 4 - There is nothing wrong with this statement
    input: Fix the description on this post. Colleges don’t tolerate bad language 
    output: 3 - It is not appropriate to use profanity in a professional setting
    input: A is crazy 
    output: 2 - There is nothing wrong with this statement
    input: Always pimpin. #goneclear 
    output: 1 - There is nothing wrong with this statement
    input: @turtleseal U think I can post the infamous chair photo
    sanjay_thasma
    output: 1 - There is nothing wrong with this statement
    input: hey nigga
    output: 10 - This is a racial slur and is offensive
    input: I want to show u my m-16 peronsally
    output: 10 - This is a threat and is not tolerated
    input: kys
    output: 9 - Telling someone to kill themselves is a horrible thing to say
    input: go back to china where u belong
    output: 9 - This is a racial slur and is offensive
    input: I will suck you off
    output: 10 - Sexual harassment is not tolerated
    input: {input}
    output:"""

    response = palm.generate_text(
    **defaults,
    prompt=prompt,
    #safety_settings= [{"category":"HARM_CATEGORY_DEROGATORY","threshold":4},{"category":"HARM_CATEGORY_TOXICITY","threshold":4},{"category":"HARM_CATEGORY_VIOLENCE","threshold":4},{"category":"HARM_CATEGORY_SEXUAL","threshold":4},{"category":"HARM_CATEGORY_MEDICAL","threshold":4},{"category":"HARM_CATEGORY_DANGEROUS","threshold":4}],
    ) 
    print(response.result)
    return response.result

def toxicCheck(inputSent):
    from transformers import pipeline

    # Create a text classification pipeline with the "unitary/toxic-bert" model
    pipe = pipeline("text-classification", model="unitary/toxic-bert")

    # Define the input sentence
    input_sentence = inputSent

    # Use the pipeline to classify the input sentence
    result = pipe(input_sentence)

    # Output the classification result
    print(result)
    return result[0]['score']

def parser(inputs):
    page_name_1 = inputs
    #print("here " + inputs)
   # with open(page_name_1) as f:
    #    single_html_string = f.read()

    # The provided HTML string
    html_segment = page_name_1

    # Parse the HTML segment using BeautifulSoup
    soup = BeautifulSoup(html_segment, 'html.parser')

    # Find all the elements with class "_2pin _a6_q" (or use other suitable class)
    elements = soup.find_all('td', class_='_2pin _a6_q')

    # Extract the comment values and store them in an array
    comment_values = []
    for element in elements:
        comment = element.find('div').text
        comment_values.append(comment)
    i = 0
    string = ""
    bad_values = []

    badWord_list = ["gay", "terrorism", "nigga", "nigger", "chink", "pedophile", "rapist"]

    year_count_map = {}

    # Print the comment values in an array
    for value in comment_values:
        if value.find("PM") != -1 or value.find("AM") != -1:
            if i ==1:
                i=0
                first_index = value.find(',')
                last_index = value.rfind(',')
                if first_index != -1 and last_index != -1:
                    year = value[first_index + 2:last_index].strip()
                if year in year_count_map:
                # If it's already in the hashmap, increment the count
                     year_count_map[year] += 1
                else:
                # If it's not in the hashmap, add it with a count of 1
                    year_count_map[year] = 1
                print(value)
                bad_values.append(string + " -> " + value)
                #print(value)
        elif len(value) <3:
            print("too short")

        else:
            #print(value)
            holder =""
            if any(value.lower() in item for item in badWord_list):
                #st.write('bad single word found')
                string = value
                i = 1
            elif value.count(" ") >0: #change gay wth array of derogatory words
                holder = aiHelper(value)
                #print(str(holder) )
                charVal = str(holder)[0]
                #print(charVal)
                intVal = int(charVal)
                if charVal==1 and  str(holder)[1] == 0:
                    intVal = 10
                #print(intVal)
                if intVal ==5 or intVal ==6 or intVal ==7:
                    #result = model(value)
                    #if result[0]['label'] == "POSITIVE" and result[0]['score'] > 0.85:
                     #   intVal = intVal-1
                      #  st.write('positive in transfoer model found')
                    #if result[0]['label'] == "NEGATIVE" and result[0]['score'] > 0.85:
                     #   intVal = intVal+1
                     #   st.write('negative in transfoer model found')
                     tox = toxicCheck(value)
                     if tox> .9:
                         intVal = intVal+2
                     elif tox>.6:
                         intVal = intVal+1
                     elif tox<.3:
                         intVal = intVal-1
                if intVal>=7:
                    string = value
                    i = 1
            
    print("---------------------------------------" + "\n")
    st.write('**These are comments that may be important to delete prior to applying**')
    for element in bad_values:
        st.write(element)
        print(element)

    #for test
    

    #starting to build data structure 
    lengthOfYear = len(year_count_map)
    keys_list = list(year_count_map.keys())
    early_year = int(keys_list[lengthOfYear-1])
    last_year = int(keys_list[0])


    ordered_year = []
    while early_year != last_year+1:
        ordered_year.append(str(early_year))
        early_year = early_year+1

    er =0 
    for x in ordered_year:
    # st.write('-----------')
    # st.write(x)
     try:
           q =year_count_map[ordered_year[er]]
     except KeyError:
           year_count_map[ordered_year[er]] = 0
     er = er+1    #need to sort the hashmap
     order_val=[]
     
     for y in ordered_year:
        try:
            order_val.append(year_count_map[y])
        except KeyError:
           order_val.append(0)
    import pandas as pd
    import altair as alt

    print(ordered_year)
    print(order_val)

    import numpy as np

    chart_data = {"Occurance" :order_val, "Year" :ordered_year  }
    ready_data = pd.DataFrame(chart_data)
    ready_data = ready_data.set_index("Year")
    st.bar_chart(ready_data)

   # st.altair_chart(line_chart, use_container_width=True)
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
   # st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    parser(string_data)
