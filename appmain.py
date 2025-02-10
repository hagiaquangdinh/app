
import streamlit as st
from fractions import Fraction
def main():
    st.title("Fraction Calculator")
    number = st.number_input("Enter a number: ",
                             min_value= 0,
                             max_value= 900
                             )
    if st.button("Calculate"):
      result = Fraction(str(number))
      st.write(f"The fraction of {number} is: {result}")

if __name__ == "__main__":
    main()
