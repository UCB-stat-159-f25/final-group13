.PHONY: env all clean pdf

# Keeping environment extra clean
env:
	conda env update --file environment.yml --prune


#nbconver as the project told us to 
all:
	jupyter nbconvert --to notebook --execute --inplace notebooks/data_prep_1.ipynb
	jupyter nbconvert --to notebook --execute --inplace notebooks/EDA_2.ipynb
	jupyter nbconvert --to notebook --execute --inplace notebooks/Model_3.ipynb

#building the pdfs
pdf:

	myst build notebooks/data_prep_1.ipynb --pdf
	mv _build/exports/data-prep-1.pdf pdf_builds/

	myst build notebooks/EDA_2.ipynb --pdf
	mv _build/exports/eda-2.pdf pdf_builds/

	myst build notebooks/Model_3.ipynb --pdf
	mv _build/exports/model-3.pdf pdf_builds/

	myst build MainNarrative.ipynb --pdf
	mv _build/exports/mainnarrative.pdf pdf_builds/

# Cleaning up
clean:
	rm -rf data/*
	rm -rf images/*
	rm -rf pdf_builds/*
	rm -rf notebooks/_build
	rm -rf _build