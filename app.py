import streamlit as st

st.title("Word Unscrambler")

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
  unscrambled_words = []
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
      # st.write(word.upper())
      # placeholder.markdown(word.upper())
      unscrambled_words.append(word.upper())

#!/usr/bin/env python3





# main("VOLIE")

with st.container():

  letter_input = st.text_input("Enter Letters", key="widget", on_change=main)
  st.button("Generate Unscrambled Words", on_click=main)
st.write(unscrambled_words)  
  # placeholder = st.empty()
  

  
# st.write("The current movie title is", title)

#USE lowercase if using popular.txt or words.txt
#USE caps if using scrabble.txt because source words are in caps
