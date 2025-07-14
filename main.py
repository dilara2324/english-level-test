import streamlit as st

# Savollar va to'g'ri javoblar
savollar = [
  (" What is the English word for 'olma'?","apple"),
  ("Complete: I ___ a student.","am"),
  ("What is the plural of book?", "books"),
  ("Translate: Men har kuni suv ichaman.","I drink water every day."),
  ("There ___ two cats in the room.","are"),
  ("Past tense of go?","went"),
  ("Translate: Ular televizor kurishayotgan edilar.","They were watching tv."),
  ("She is ___ honest person. (a/an)","a"),
  ("What is the opposite of always?","never"),
  ("Synonym of important?","essential"),
  ("If I ___ rich, I woul travel the world.","were"),
  ("Who writes the book?","author"),
]

# Session states
if "index" not in st.session_state:
  st.session_state.index = 0
  st.session_state.score = 0
  st.session_state.done = False

st.title("🧠 English Level Test 🎓")

# Agar test tugamagan bo‘lsa
if not st.session_state.done:
  savol, togrijavob = savollar[st.session_state.index]
  st.subheader(f"{st.session_state.index + 1}. {savol}")
  javob = st.text_input("Your answer:")

  if st.button("Next"):
    if javob.strip().lower() == togrijavob.lower():
      st.session_state.score += 1
    st.session_state.index += 1

    if st.session_state.index >= len(savollar):
      st.session_state.done = True
    st.rerun()

# Agar test tugamagan bo‘lsa
else:
  ball = st.session_state.score
  if ball >= 11:
    level = "C1+ 🔥 Excellent!"
  elif ball >= 9:
    level = "B2 💪 Great!"
  elif ball >= 7:
    level = "B1 👏 Well done!"
  elif ball >= 4:
    level = "A2 💜🫰 Keep going!"
  else:
    level = "A1 🥸 You can do better!"
 
 # DARAJANI SHU YERDA KO‘RSAT
  st.success(f"✅ Test Completed!\n\nYou got  {ball}/12.\nLevel: {level}")

  if  st.button("Restart"):
   st.session_state.index = 0
   st.session_state.score = 0
   st.session_state.done = False
   st.rerun()
    


  

