ZIP_NAME = plugin.zip

all: clean $(ZIP_NAME)

$(ZIP_NAME):
	@echo "Zipping..."
	@python build.py
	@echo "Done $(ZIP_NAME)"

clean:
	@rm -f $(ZIP_NAME)