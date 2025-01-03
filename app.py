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
  result_6_letter = []
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
              result_6_letter.append(word.lower())
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
  result_6_letter = sorted(result_6_letter, key=lambda w: len(w), reverse=True)

  # col1, col2, col3 = st.columns(3)
  tab6, tab5, tab4, tab3 = st.tabs(["6 letters", "5 letters" ,"4 letters", "3 letters"])
  with tab6:
    for word in result_6_letter:
      st.write(word.upper())
  with tab5:
    uppercase_5 = [s.upper() for s in result_5_letter]
    st.write("     ".join(uppercase_5))
    # for word in result_5_letter:
    #   st.write(word.upper())
  with tab4:
    uppercase_4 = [s.upper() for s in result_4_letter]
    st.write("     ".join(uppercase_4))

    # for word in result_4_letter:
    #   st.write(word.upper())
  with tab3:
    uppercase_3 = [s.upper() for s in result_3_letter]
    st.write("     ".join(uppercase_3))
    # for word in result_3_letter:
      # st.write(word.upper())
 
#USE lowercase if using popular.txt or words.txt
#USE caps if using scrabble.txt because source words are in caps

st.latex(r'''
    \text{Fill Rate} =
    \left(\frac{\text{Impressions}}{\text{Total Code Served}}\right)
    ''')

st.latex(r'''
    \frac{1}{2} =
    \frac{2}{4} =
    \frac{4}{8}
    ''')

st.latex(r'''
    3\frac{1}{2} =
    3\frac{}{4} =
    3\frac{4}{}
    ''')

st.latex(r'''
    3\le 5 \le 7
    ''')

st.latex(r'''
      \sqrt{x^2+1}
    ''')

st.latex(r'''
      \begin{pmatrix}
         a & b \\
         c & d
      \end{pmatrix}
    ''')

st.latex(r'''
      \begin{array}
        &  1123 \\
      + &    10 \\
      \end{array}
    ''')

st.latex(r'''
x_{1} = \frac{A-A_{0}}{\frac{1}{2}\cdot \left( A_{\mathrm{A}} - A_{\mathrm{a}} \right)}
\qquad
    ''')

st.latex(r'''
      \begin{align*} 
      2x - 5y &=  8 \\ 
      3x + 9y &=  -12
      \end{align*}
    ''')

st.latex(r'''
      \begin{align*} 
         8  \\ 
       + 3  \\
      \overline { 11 }
      \end{align*}
    ''')

st.latex(r'''
      \begin{align*} 
         8  \\ 
       \times 3  \\
      \overline { 24 }
      \end{align*}
    ''')

st.latex(r'''
      \begin{align*} 
         8  \\ 
       \cdot 3  \\
      \overline { 24 }
      \end{align*}
    ''')

st.latex(r'''
      \begin{align*} 
         9  \\ 
       \div 3  \\
      \overline { 3 }
      \end{align*}
    ''')

st.write('This is an example of an elementary, grade school, primary school math expression')

st.latex(r'''
      \begin{align*} 
         1088  \\ 
       +  203  \\
      \overline { 1291 }
      \end{align*}
    ''')

st.latex(r'''
      \begin{center*}
      Example 1: The following paragraph (given in quotes) is an 
      example of centred alignment using the center environment. 
      
      ``La\TeX{} is a document preparation system and document markup 
      language. \LaTeX{} uses the \TeX{} typesetting program for formatting 
      its output, and is itself written in the \TeX{} macro language. 
      \LaTeX{} is not the name of a particular (executable) typesetting program, but 
      refers to the suite of commands (\TeX{} macros) which form the markup 
      conventions used to typeset \LaTeX{} documents."
      \end{center*}
      ''')

numbers_input = st.text_input("Enter First In Math Numbers", "1,2,3,4,5,6")
if numbers_input:
  numbers_array = numbers_input.split(",")
  for i in range(0, len(numbers_array), 2):
      st.write(int(numbers_array[i])/int(numbers_array[i+1]))

