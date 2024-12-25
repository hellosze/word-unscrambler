import streamlit as st


st.title("Word Unscrambler")


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

  # col1, col2, col3 = st.columns(3)
  tab5, tab4, tab3 = st.tabs(["5-6 letter words" ,"4 letter words", "3 letter words"])
  with tab5:
    for word in result_5_letter:
      st.write(word.upper())
  with tab4:
    for word in result_4_letter:
      st.write(word.upper())
  with tab3:
    for word in result_3_letter:
      st.write(word.upper())
 
#USE lowercase if using popular.txt or words.txt
#USE caps if using scrabble.txt because source words are in caps

st.latex(r'''
    \text{Fill Rate} =
    \left(\frac{\text{Impressions}}{\text{Total Code Served}}\right)
    ''')

st.latex(r'''
    \frac{1}{2} =
    \frac{2}{\text{"___"}} =
    \frac{4}{8}
    ''')

numbers_input = st.text_input("Enter First In Math Numbers", "1,2,3,4,5,6")
if numbers_input:
  numbers_array = numbers_input.split(",")
  for i in range(0, len(numbers_array), 2):
      st.write(int(numbers_array[i])/int(numbers_array[i+1]))

