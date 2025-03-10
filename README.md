# Static Site Generator

A custom-built static site generator that transforms Markdown files into a full HTML website. Originally created as part of the Boot.dev curriculum.

## Features

- Converts Markdown content to HTML
- Automatically generates navigation between pages
- Supports custom theming via CSS
- Creates a clean, organized site structure
- Fast build times with no dependencies on external services

## How It Works

This static site generator takes Markdown files as input and generates a complete website with HTML, CSS, and properly linked pages. The generator handles:

1. Parsing Markdown syntax
2. Converting to semantic HTML
3. Building a navigation structure
4. Maintaining proper links between pages
5. Applying consistent styling

## Usage

To use this generator:

1. Clone the repository
2. Add your Markdown content to the `content` directory
3. Run the build script:

```
python build.py
```

4. The generated website will be available in the `public` directory

## Customization

You can customize your site by:
- Modifying the CSS files in the `static` directory
- Adjusting the HTML templates 
- Creating new Markdown content

## Project Structure

- static-site-generator/
- ├── build.py # Main build script
- ├── src/ # Source code
- ├── content/ # Markdown content files
- ├── static/ # CSS, JS, and other static assets
- └── public/ # Generated site (output)


## Future Improvements

Some potential enhancements:
- Add support for blog posts with dates
- Implement tags/categories
- Create a search feature
- Add RSS feed generation
