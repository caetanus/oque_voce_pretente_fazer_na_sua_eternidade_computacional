all: latex clean

latex:
	pdflatex t3.tex

clean:
	rm -rf *.log *.nav *.snm *.out *.aux *.dvi *.toc

open:
	gnome-open t3.pdf


preview: all open
