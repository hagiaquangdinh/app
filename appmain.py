
import streamlit as st
from fractions import Fraction

def fract(n):
  """Tính giai thừa của số nguyên dương n."""

  if n < 0:
    return "Không thể tính giai thừa của số âm."
  elif n == 0:
    return 1
  else:
    giai_thua = 1
    for i in range(1, n + 1):
      giai_thua *= i
    return giai_thua

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
        
st.title("Fraction Calculator")
n = st.number_input("Enter a number: ",
                             min_value= 0,
                             max_value= 900
                             )
if st.button("Calculate"):
   r = fact(int(n))
   st.write(f"The fraction of {int(n)} is: {r}")
