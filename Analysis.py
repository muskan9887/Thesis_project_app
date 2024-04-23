import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analysis", layout="wide")
st.markdown("<h1 style='text-align: center; color: #336699; background-color: #f0f2f6; padding: 10px;'>ESTATE "
            "ANALYTICS</h1>", unsafe_allow_html=True)
st.write("")
st.write("")

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl','rb'))






st.header('Features Wordcloud')

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='black',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot()

st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

# Create the distplot directly within Streamlit
fig, ax = plt.subplots(figsize=(10, 4))

sns.distplot(new_df[new_df['property_type'] == 'house']['price'], ax=ax, label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], ax=ax, label='flat')
ax.legend()

# Display the plot using st.pyplot() with the figure argument
st.pyplot(fig)

st.set_option('deprecation.showPyplotGlobalUse', False)
