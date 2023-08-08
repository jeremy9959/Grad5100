# Render the quarto web page

publish: 
	quarto render
	git add .
	git commit -m 'updating published version'
	git push uconn devel
