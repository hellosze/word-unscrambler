import streamlit as st
from PyMultiDictionary import MultiDictionary
dictionary = MultiDictionary()


st.title("Word Unscrambler")
# input_slot = st.empty()
# button_slot = st.empty()


unscrambled_words = []

def can_spell(letters, word):
  # reverse sort to get the blanks ('?') to the end of letters string,
  # so that the greedy algorithm works
  letters = sorted(letters, reverse=True)
  word = list(word)

  for letter in letters:
      if len(word) == 0:
          return True
      elif letter == '?':
          word.pop()
      elif letter in word:
          word.remove(letter)

  return len(word) == 0

def main():
  letters = st.session_state.widget.upper()

  result = []

  with open('true-txt.csv', 'r') as words_file:
      for line in words_file:
          word = line.strip()
          if len(word) == 1:
            continue
          if can_spell(letters, word):
              result.append(word.lower())

  result = sorted(result, key=lambda w: len(w), reverse=True)
  for word in result:
      # print(word)
      st.write(word.upper())
      # text_slot.write(word.upper())
      # placeholder.markdown(word.upper())
      # unscrambled_words.append(word.upper())

#!/usr/bin/env python3





# main("VOLIE")

# with st.container():

letter_input = st.text_input("Enter Letters", key="widget")
button = st.button("Generate Unscrambled Words")

if button  or letter_input:

  letters = st.session_state.widget.upper()

  result = []
  result_5_letter = []
  result_4_letter = []
  result_3_letter = []
  with open('true-txt.csv', 'r') as words_file:
      for line in words_file:
          word = line.strip()
          if len(word) == 1 or len(word) == 2:
            continue
          if can_spell(letters, word):
              result.append(word.lower())
          if can_spell(letters, word) and len(word) == 6:
              result_5_letter.append(word.lower())
          if can_spell(letters, word) and len(word) == 5:
              result_5_letter.append(word.lower())
          if can_spell(letters, word) and len(word) == 4:
              result_4_letter.append(word.lower())
          if can_spell(letters, word) and len(word) == 3:
              result_3_letter.append(word.lower())

  result = sorted(result, key=lambda w: len(w), reverse=True)
  result_3_letter = sorted(result_3_letter, key=lambda w: len(w), reverse=True)
  result_4_letter = sorted(result_4_letter, key=lambda w: len(w), reverse=True)
  result_5_letter = sorted(result_5_letter, key=lambda w: len(w), reverse=True)

  col1, col2, col3 = st.columns(3)

  with col1:
    for word in result_5_letter:
      st.write(word.upper())
      with st.popover("Get Synonym"):
        meaning = dictionary.meaning('en', word.upper())
        if meaning[2]:
          st.write(meaning[2])
  with col2:
    for word in result_4_letter:
      st.write(word.upper())
  with col3:
    for word in result_3_letter:
      st.write(word.upper())
  # for word in result:
      # print(word)
      # st.write(word.upper())
  # st.write(button)
  # word_output = st.empty()
  # word_output.text(unscrambled_words)  
  # placeholder = st.empty()
# words_state = st.text("Generating words")
# words_state.text(""

  
# st.write("The current movie title is", title)

#USE lowercase if using popular.txt or words.txt
#USE caps if using scrabble.txt because source words are in caps

st.latex(r'''
    \text{Fill Rate} =
    \left(\frac{\text{Impressions}}{\text{Total Code Served}}\right)
    ''')
