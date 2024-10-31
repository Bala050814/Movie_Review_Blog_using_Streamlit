import streamlit as st

st.set_page_config(
    page_title="Dark : Review | Movie Box",
    page_icon="http://www.pngmart.com/files/7/Box-PNG-Free-Download.png"
)
st.markdown("<h1 style='color: red;'>DARK REVIEW:ONE OF THE FINEST SERIES IN THE WORLD</h1>",unsafe_allow_html=True)
st.image("https://dark.netflix.io/share/global.png")
st.markdown("""Over the years, with hundreds of shows and thousands of episodes consumed, I’m not sure I’ve ever seen a series as mentally exhausting as Dark, where I just finished three seasons over the course of the 5 days.

Dark is a Netflix series from Germany, and it’s impossible to talk about without discussing its central concept, which is revealed within the first few episodes: time travel.Dark has gone deeper into the concept than any series or movie I have ever seen, and seems determined to craft what has to be the most intricate and detailed time travel sci-fi tale I’ve ever seen.

The series is centered on four main families in a small German town, and when people start to go missing, it seems like this is a crime drama. Instead, most of the missing are wandering into a nearby cave, which has doors open to the past, and occasionally the future.While this starts as a “find the missing kid lost in time” story, it evolves to become much, much more than that. Why is Dark so exhausting?""")
st.write()
st.image("https://filmschoolrejects.com/wp-content/uploads/2020/07/dark-netflix-characters.jpg")
st.markdown("""For every character, you have to keep track of whose father, son, mother, daughter, brother, sister, grandparent or grandchild they might be. And then you have to keep track of that across what ends up being something like six total timelines. 

The show time travels based on a 33 year cycle, so it starts in 2019, goes back to 1986, then to 1953, and 1920 and even the 1800s. It also hops 33 years into the future in 2052. So you have to keep track of all these characters from all these families in essentially three different stages of life, child/teen, young adult/middle age, and old age, and remember how they’re all related to one another. 
            
Those relationships get very complicated due to time travel, though I won’t spoil anything there. And in case that wasn’t enough, the final season throws in the concept of parallel dimensions as well, just in case you weren’t confused before.I cannot explain how hard this show was to keep track of. It never got easier. I was in the final episodes of the third season and still having to count off in my head who was whose father and what this recent plot turn revealed about who was really whose ancestor.
            
The plot mainly runs on 2 character Jonas and Martha.And yet overall, it’s an incredible series, one of Netflix’s best, and one of science fiction’s best, honestly, especially in the time travel genre. I am probably willing to declare it the best time travel story ever told with how much care and intelligence it devotes to the subject. I highly recommend it, but prepare for your brain to be fatigued for the next month or so as you make your way through it.""")
st.write("")
st.write(" ")
table=[["Director","Baran bo Odar"],["Screenwriter","Jantje Friese, Ronny Schalk, Martin Behnke, Marc O. Seng"],["Network","Netflix"],["Genre","Mystery & Thriller, Crime, Drama"],["Release Date","Dec 1, 2017"]]
st.dataframe(table,width=700,height=210)

st.write(" ")
st.write(" ")

st.markdown("**Official Trailer**",unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=ESEUoa-mz2c")

st.markdown("""
**Overall Review** - Time Worthy and a solid 10/10👍    
""" ,unsafe_allow_html=True)

st.write(" ")
st.write(" ")

rating=st.slider("Give Your Review After Watching : ", min_value=0, max_value=10, step=1)

if rating:
    st.write("Your rating:",rating,"/10")
    st.write("Thank you For your Response !!")


st.markdown("### Share your thoughts:")
user_comment = st.text_area("Leave a comment about the series:")
if st.button("Submit"):
    st.write("Thank you for your comment!")
