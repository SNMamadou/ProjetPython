# Copyright (C) 2012  Jean-Vincent Loddo

# Cette oeuvre est mise à disposition sous licence Paternité - Partage
# à l'Identique 3.0 non transposé. Pour voir une copie de cette licence,
# visitez http://creativecommons.org/licenses/by-sa/3.0/ ou écrivez à
# Creative Commons, 444 Castro Street, Suite 900, Mountain View, California,
# 94041, USA.

all: 
	make pdf
	make tex

pdf:
	@for i in *.lyx; do lyx -e pdf $${i%%.*}.lyx; done

tex:
	@for i in *.lyx; do lyx -e pdflatex $${i%%.*}.lyx; done

ps:
	@for i in *.lyx; do lyx -e ps $${i%%.*}.lyx; done

ps--std: ps
	@for i in *.lyx; do pstops "2:0L@.7(21cm,0)+1L@.7(21cm,14.85cm)" $${i%%.*}.ps $${i%%.*}--.ps; done

ps--: ps
	@for i in *.lyx; do pstops "2:0L@.75(21.5cm,0)+1L@.75(21.5cm,14cm)" $${i%%.*}.ps $${i%%.*}--.ps; done

html:
	@for i in *.lyx; do elyxer $${i%%.*}.lyx $${i%%.*}.html; done

clean:
	@for i in *.lyx; do rm -f $${i%%.*}.tex $${i%%.*}.pdf $${i%%.*}.ps; done
