import streamlit as st
import random

st.set_page_config(page_title="لعبة تخمين الأرقام", page_icon="🎮")

st.title("🎮 لعبة تحدي التخمين")
st.write("مرحباً بك! حاول تخمين الرقم السري من 1 إلى 20 في أقل عدد من المحاولات!")

# تهيئة المتغيرات في الجلسة
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.game_over = False

guess = st.number_input("أدخل رقمك المتوقع (1 - 20):", min_value=1, max_value=20, step=1)

if st.button("تخمين 🚀") and not st.session_state.game_over:
    st.session_state.attempts += 1
    
    if guess < st.session_state.secret_number:
        st.warning("🔻 الرقم السري أكبر من ذلك! حاول مرة أخرى.")
    elif guess > st.session_state.secret_number:
        st.warning("🔺 الرقم السري أصغر من ذلك! حاول مرة أخرى.")
    else:
        st.balloons()
        st.success(f"🎉 إجابة صحيحة! أحسنت، عرفت الرقم ({st.session_state.secret_number}) بعد {st.session_state.attempts} محاولات!")
        st.session_state.game_over = True

if st.session_state.game_over or st.button("إعادة اللعبة 🔄"):
    st.session_state.secret_number = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()