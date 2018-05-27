from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud


text = open(u'xinlin.txt', encoding='utf-8').read()

alice_mask = np.array(Image.open('alice_mask.png'))
font = 'SourceHanSansSC-Regular.otf'

wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask,
               contour_width=3, font_path=font,
               max_font_size=60)
wc.generate(text)

wc.to_file('my_alice.png')

# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.figure()
# plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
# plt.axis("off")
# plt.show()
