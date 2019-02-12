import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS


df = pd.read_csv("erste_150.csv", index_col=1)


# join tweets to a single string
#words = ' '.join(tm.df[1])

words = pd.DataFrame.to_string(df)

# remove URLs, RTs, and twitter handles
no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

wordcloud = WordCloud(
                      #font_path='/Users/sebastian/Library/Fonts/CabinSketch-Bold.ttf',
                      stopwords=STOPWORDS,
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(no_urls_no_tags)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('./my_twitter_wordcloud_1.png', dpi=300)
plt.show()
