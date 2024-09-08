import streamlit as st
#st. title: displays text in title formatting
st.title("This is a title m8")
st.title("_Streamlit_ is lit :blue[cool] :sunglasses:")
st.title("_Streamlit_ with an anchor :anchor:", "lit_anchor")

# st.header: displays text in header formatting
st.header("This is a header m8")
st.header("_header_ is lit :blue[cool] :sunglasses:")
st.header("one header", divider="violet")
st.header("two header", divider=True)
st.header("three header", divider=True)
st.header('I am a header and I have an anchor: :anchor:', "header_with_anchor")

#st.subheader: displays text in subheader formatting
st.subheader("This is a subheader m8")
st.subheader("_subheader_ is lit :blue[cool] :sunglasses:")
st.subheader("subheader with rainbow divider :rainbow: and anchor :anchor:", "subheader_rainbow_anchor", divider="rainbow")

#st.markdown display string formatted as markdown
st.markdown("<h1>Html H1 using st.markdown yay!</h1>", unsafe_allow_html=True)
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will

result in a hard return.    

hello you \t\t \n bye bye bye
'''
st.markdown(multi)



