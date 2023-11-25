IMAGE_NAME = yt-dlp-ffmpeg
DOCKERFILE_PATH = $(CURDIR)/Dockerfile

.PHONY: all build clean help

all: help

build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE_PATH) .

clean:
	docker rmi $(IMAGE_NAME)

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@echo "  build    : Build the image"
	@echo "  clean    : Remove the generated image"
	@echo "  help     : Display this help message"
