
# CSS Coding Standards

We will be using the guidelines provided in the link below as a base:
[Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)

## Additional Coding Standards

Following are additional guidelines to be followed. **Note**: The following rules will override the ones provided in the Google Style Guide.

## CSS Guidelines

### Syntax

- Use soft tabs with two spaces—they're the only way to guarantee code renders the same in any environment.
- When grouping selectors, keep individual selectors to a single line.
- Include one space before the opening brace of declaration blocks for legibility.
- Place closing braces of declaration blocks on a new line.
- Include one space after each <span style="color: #ff9900;">`:`</span> for each declaration.
- Each declaration should appear on its own line for more accurate error reporting.
- End all declarations with a semicolon. The last declaration's semicolon is optional, but your code is more error-prone without it.
- Comma-separated property values should include a space after each comma (e.g., <span style="color: #ff9900;">`box-shadow`</span>).
- Don't include spaces after commas *within* <span style="color: #ff9900;">`rgb()`</span>, <span style="color: #ff9900;">`rgba()`</span>, <span style="color: #ff9900;">`hsl()`</span>, <span style="color: #ff9900;">`hsla()`</span>, or <span style="color: #ff9900;">`rect()`</span> values. This helps differentiate multiple color values (comma, no space) from multiple property values (comma with space).
- Don't prefix property values or color parameters with a leading zero (e.g., <span style="color: #ff9900;">`.5`</span> instead of <span style="color: #ff9900;">`0.5`</span> and <span style="color: #ff9900;">`-.5px`</span> instead of <span style="color: #ff9900;">`-0.5px`</span>).
- Lowercase all hex values, e.g., <span style="color: #ff9900;">`#fff`</span>. Lowercase letters are much easier to discern when scanning a document as they tend to have more unique shapes.
- Use shorthand hex values where available, e.g., <span style="color: #ff9900;">`#fff`</span> instead of <span style="color: #ff9900;">`#ffffff`</span>.
- Quote attribute values in selectors, e.g., <span style="color: #ff9900;">`input[type="text"]`</span>. [They’re only optional in some cases](https://mathiasbynens.be/notes/unquoted-attribute-values#css), and it’s a good practice for consistency.
- Avoid specifying units for zero values, e.g., <span style="color: #ff9900;">`margin: 0;`</span> instead of <span style="color: #ff9900;">`margin: 0px;`</span>.

**Bad**

```css
.selector, .selector-secondary, .selector[type=text] {
  padding:15px;
  margin:0px 0px 15px;
  background-color:rgba(0, 0, 0, 0.5);
  box-shadow:0px 1px 2px #CCC,inset 0 1px 0 #FFFFFF
}
```

**Good**

```css
.selector,
.selector-secondary,
.selector[type="text"] {
  padding: 15px;
  margin-bottom: 15px;
  background-color: rgba(0,0,0,.5);
  box-shadow: 0 1px 2px #ccc, inset 0 1px 0 #fff;
}
```

### Declaration Order

Related property declarations should be grouped together following the order:

1. Positioning
2. Box model
3. Typographic
4. Visual

Positioning comes first because it can remove an element from the normal flow of the document and override box model-related styles. The box model comes next as it dictates a component's dimensions and placement.

Everything else takes place *inside* the component or without impacting the previous two sections, and thus they come last.

```css
.declaration-order {
  /* Positioning */
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 100;

  /* Box-model */
  display: block;
  float: right;
  width: 100px;
  height: 100px;

  /* Typography */
  font: normal 13px "Helvetica Neue", sans-serif;
  line-height: 1.5;
  color: #333;
  text-align: center;

  /* Visual */
  background-color: #f5f5f5;
  border: 1px solid #e5e5e5;
  border-radius: 3px;

  /* Misc */
  opacity: 1;
}
```

### Don't Use <span style="color: #ff9900;">`@import`</span>

Compared to <span style="color: #ff9900;">`<link>`</span>s, <span style="color: #ff9900;">`@import`</span> is slower, adds extra page requests, and can cause other unforeseen problems. Avoid them and instead opt for an alternate approach:

- Use multiple <span style="color: #ff9900;">`<link>`</span> elements
- Compile your CSS with a preprocessor like Sass or Less into a single file
- Concatenate your CSS files with features provided in Rails, Jekyll, and other environments

```html
<!-- Use link elements -->
<link rel="stylesheet" href="core.css">

<!-- Avoid @imports -->
<style>
  @import url("more.css");
</style>
```

### Media Query Placement

Place media queries as close to their relevant rule sets whenever possible. Don't bundle them all in a separate stylesheet or at the end of the document. Doing so only makes it easier for folks to miss them in the future. Here's a typical setup.

```css
.element { ... }
.element-avatar { ... }
.element-selected { ... }

@media (min-width: 480px) {
  .element { ...}
  .element-avatar { ... }
  .element-selected { ... }
}
```

### Prefixed Properties

When using vendor-prefixed properties, indent each property such that the declaration's value lines up vertically for easy multi-line editing.

```css
/* Prefixed properties */
.selector {
  -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.15);
          box-shadow: 0 1px 2px rgba(0,0,0,.15);
}
```

### Single Declarations

In instances where a rule set includes **only one declaration**, consider removing line breaks for readability and faster editing. Any rule set with multiple declarations should be split into separate lines.

The key factor here is error detection—

e.g., a CSS validator stating you have a syntax error on Line 183. With a single declaration, there's no missing it. With multiple declarations, separate lines are a must for your sanity.

```css
/* Single declarations on one line */
.span1 { width: 60px; }
.span2 { width: 140px; }
.span3 { width: 220px; }

/* Multiple declarations, one per line */
.sprite {
  display: inline-block;
  width: 16px;
  height: 15px;
  background-image: url(../img/sprite.png);
}
.icon           { background-position: 0 0; }
.icon-home      { background-position: 0 -20px; }
.icon-account   { background-position: 0 -40px; }
```

### Shorthand Notation

Strive to limit the use of shorthand declarations to instances where you must explicitly set all the available values. Common overused shorthand properties include:

- <span style="color: #ff9900;">`padding`</span>
- <span style="color: #ff9900;">`margin`</span>
- <span style="color: #ff9900;">`font`</span>
- <span style="color: #ff9900;">`background`</span>
- <span style="color: #ff9900;">`border`</span>
- <span style="color: #ff9900;">`border-radius`</span>

Often times we don't need to set all the values a shorthand property represents. For example, HTML headings only set top and bottom margin, so when necessary, only override those two values. Excessive use of shorthand properties often leads to sloppier code with unnecessary overrides and unintended side effects.

**Bad**

```css
.element {
  margin: 0 0 10px;
  background: red;
  background: url("image.jpg");
  border-radius: 3px 3px 0 0;
}
```

**Good**

```css
.element {
  margin-bottom: 10px;
  background-color: red;
  background-image: url("image.jpg");
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}
```

### Nesting in CSS

**Do not nest selectors more than three levels deep!**

```css
.page-container {
  .content {
    .profile {
      /* STOP! */
    }
  }
}
```

When selectors become this long, you're likely writing CSS that is:

- Strongly coupled to the HTML (fragile) *—OR—*
- Overly specific (powerful) *—OR—*
- Not reusable

Again: **never nest ID selectors!**

If you must use an ID selector in the first place (and you should really try not to), they should never be nested. If you find yourself doing this, you need to revisit your markup, or figure out why such strong specificity is needed. If you are writing well-formed HTML and CSS, you should **never** need to do this.

### Nesting in Less and Sass

Avoid unnecessary nesting. Just because you can nest, doesn't mean you always should. Consider nesting only if you must scope styles to a parent and if there are multiple elements to be nested.

```scss
// Without nesting
.table > thead > tr > th { … }
.table > thead > tr > td { … }

// With nesting
.table > thead > tr {
  > th { … }
  > td { … }
}
```

### Operators in Less and Sass

For improved readability, wrap all math operations in parentheses with a single space between values, variables, and operators.

**Bad**

```scss
.element {
  margin: 10px 0 @variable*2 10px;
}
```

**Good**

```scss
.element {
  margin: 10px 0 (@variable * 2) 10px;
}
```

### Comments

Code is written and maintained by people. Ensure your code is descriptive, well-commented, and approachable by others. Great code comments convey context or purpose. Do not simply reiterate a component or class name.

Be sure to write in complete sentences for larger comments and succinct phrases for general notes.

Comments have to be used to group specific CSS for a particular section of the page.

**Bad**

```css
/* Modal header */
.modal-header {
  ...
}
```

**Good**

```css
/* Wrapping element for .modal-title and .modal-close */
.modal-header {
  ...
}
```

### Class Names
Follow BEM convention: https://www.freecodecamp.org/news/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849/#the-bem-naming-convention
- Keep classes lowercase and use dashes (not underscores or camelCase). Dashes serve as natural breaks in related class (e.g., <span style="color: #ff9900;">`.btn`</span> and <span style="color: #ff9900;">`.btn-danger`</span>).
- Avoid excessive and arbitrary shorthand notation. <span style="color: #ff9900;">`.btn`</span> is useful for *button*, but <span style="color: #ff9900;">`.s`</span> doesn't mean anything.
- Keep classes as short and succinct as possible.
- Use meaningful names; use structural or purposeful names over presentational.
- Prefix classes based on the closest parent or base class.
- Use <span style="color: #ff9900;">`.js-*`</span> classes to denote behavior (as opposed to style) or classes that are added by JavaScript, but keep these classes out of your CSS.
- Follow modularity and specificity: https://docs.ckan.org/en/2.9/contributing/css.html#modularity-and-specificity

It's also useful to apply many of these same rules when creating Sass and Less variable names.

**Bad**

```css
.t { ... }
.red { ... }
.header { ... }
```

**Good**

```css
.tweet { ... }
.important { ... }
.tweet-header { ... }
```

### Selectors

- Use classes over a generic element tag for optimum rendering performance.
- Avoid using several attribute selectors (e.g., <span style="color: #ff9900;">`[class^="..."]`</span>) on commonly occurring components. Browser performance is known to be impacted by these.
- Keep selectors short and strive to limit the number of elements in each selector to three.
- Scope classes to the closest parent **only** when necessary (e.g., when not using prefixed classes).

**Bad**

```css
span { ... }
.page-container #stream .stream-item .tweet .tweet-header .username { ... }
.avatar { ... }
```

**Good**

```css
.avatar { ... }
.tweet-header .username { ... }
.tweet .avatar { ... }
```

Reference: [http://codeguide.co/#css](http://codeguide.co/#css)

# Enforcing Tool and Config

- Use Stylelint for linting. [https://stylelint.io/user-guide/get-started](https://stylelint.io/user-guide/get-started)

- `.stylelintrc` config
```json
{
  "extends": "stylelint-config-standard",
  "rules": {
    "indentation": 2,
    "selector-list-comma-newline-after": "always",
    "block-opening-brace-space-before": "always",
    "block-closing-brace-newline-after": "always",
    "declaration-colon-space-after": "always",
    "declaration-block-semicolon-newline-after": "always",
    "value-list-comma-space-after": "always",
    "number-leading-zero": "never",
    "color-hex-case": "lower",
    "color-hex-length": "short",
    "selector-attribute-quotes": "always",
    "length-zero-no-unit": true,
    "order/properties-alphabetical-order": true,
    "selector-max-specificity": "0,3,1",
    "max-nesting-depth": 3,
    "selector-nested-pattern": "^&"
  }
}
```