text = ""

for i in reversed(range(1, 33)):
    entry = '						<article class="thumb">' + "\n" + '							<a href="images/fulls/' + str(i) + '.JPG" class="image"><img src="images/thumbs/' + str(i) + '.jpg" alt="" /></a>' + '\n' + '							<h2>Title</h2>' + '\n' + '							<p>Description</p>' + '\n' + '						</article>\n'
    text += entry

print(text)