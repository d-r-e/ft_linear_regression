PREDICT = predict.py

TRAIN = train.py

push:
	git add $(PREDICT) $(TRAIN) Makefile en.subject.pdf .gitignore README.md
	git commit -m "ft_linear_regression by darodrig"
	git push

clean:

t:
	./train.py
p:
	./predict.py
