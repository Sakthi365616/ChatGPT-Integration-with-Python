import openai # to interact with chatGPT generative chatbot
import speech_recognition as sr # speech to text
import streamlit as st



rec=sr.Recognizer()# Recognizing voice input
openai.api_key='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'
model='text-davinci-002' # Language model used to get the result from chatGPT


def Generative(prompt):
    response = openai.Completion.create(engine=model, prompt=prompt, n=1, stop=None, max_tokens=1024, temperature=0.7)
    message = response.choices[0].text.strip()
    return message


st.sidebar.header('CHAT_GPT')
add_input_format=st.sidebar.selectbox('Choose an option', ('Text to Text','Speech to Text'))
if add_input_format=='Text to Text':
    txt_in = st.text_input('**Input:**')
    hit = st.button('**SUBMIT**')
    if hit:
        content = Generative(txt_in)# Calling the Generative function with text input
        st.write(content)
        
        

            
if add_input_format=='Speech to Text':
    with sr.Microphone() as Input: # accessing the system microphone
            s_n=st.button('speak now')
            if s_n:
                audio = rec.listen(Input)    # getting the audio input 
                try:
                    text = rec.recognize_google(audio) # converting the voice into text
                    st.write(text)
                    content_a=Generative(text) #Calling the Generative function
                    st.write(content_a) # printing the generated response                    
                       
                except sr.UnknownValueError:
                    print('I cannot understand you')
                except sr.RequestError:
                    print('I could not get the request')               
                

    
              


    
        


   
        




    
    

    
    





    


    