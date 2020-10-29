PREDICT = predict.py

TRAIN = train.py

push:
	git add $(PREDICT) $(TRAIN) Makefile ft_linear_regression.ipynb
	git commit -m "ft_linear_regression by darodrig"
	git push

clean:

t:
	./train.py
p:
	./predict.py
