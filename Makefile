ZIP_NAME = plugin.zip

all: clean $(ZIP_NAME)

$(ZIP_NAME):
	@echo "Zipping..."
	@python build.py
	@echo "Done $(ZIP_NAME)"

test:
	make all
	@cp plugin.zip "C:\Users\Admin\AppData\Roaming\calibre\plugins\Ebook Translator.zip"
	@echo "Done $(ZIP_NAME)"
	@calibre-debug test.py
clean:
	@rm -f $(ZIP_NAME)