# HTML coding standards
We will be using the guidelines provided in the link below as base
[Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)

# Additional coding standards
Following are additional guidelines to be followed.
**Note**: The following rules will override the ones provided in google style guide.

## General
**HTML is a Markup Language**:
HTML is used to markup your document and not style it. We have CSS for styling. This means it is not advisable to use h1, h2 to size your content.

**Always Specify a DOCTYPE**:
Always specify the doctype at the top of the page. Ideally, this should be:

```html
<!DOCTYPE html>
```

### IE Compatibility Mode

Internet Explorer supports the use of a document compatibility tag to specify what version of IE the page should be rendered as. Unless circumstances require otherwise, it's most useful to instruct IE to use the latest supported mode with edge mode.

```html
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
```

### Add Lang Attribute

**Example**

```html
<html lang="en-US">
```

### Don't Mix Quotation Marks

**Bad**

```html
<input type="text" id='txt-name'>
```

**Good**

```html
<input type="text" id="txt-name">
```

### Document Metadata and Character Encoding

- Add a title element.
- Add the `<meta charset="UTF-8">`, this tells the browser the character encoding for the HTML document.

```html
<head>
  <meta charset="UTF-8">
  <title>HTML Best Practices</title>
</head>
```

### Specify MIME Type of Minor Linked Resources

For example, when linking a CSS file, specify stylesheet as the MIME type.

```html
<link href="/pdf" rel="alternate" type="application/pdf">
<link href="/feed" rel="alternate" type="application/rss+xml">
<link href="/css/screen.css" rel="stylesheet">
```

**Avoid Inline Styles**: Only use inline styles as a last resort.

**Avoid Inline Scripts**: Only use inline scripts as a last resort.

### Use Classes for CSS

It is a good habit to associate CSS with classes rather than ID. This allows styles to be easily reused without changing the CSS file.

```html
<input type="text" id="txt-firstName" class="form-textbox">
```

**Bad**

```css
#txtFirstName {
    width: 80%;
}
```

**Good**

```css
.form-textbox {
    width: 80%;
}
```
## Tags

**Tags in Lower Case**: Tag names are to be kept in lower case.

### Do Not Use `<center>` Tag
Do NOT use the `<center>` tag, it has been deprecated and browser support might be dropped at any time. Instead, give a width to your element and then `margin:auto`.

### Avoid Using `<br>` Tags for Indentation
Do NOT use `<br>` tags to add margin or padding. Instead, use CSS. If you find yourself using the `<br>` tag more than twice in succession, you should probably use CSS instead.

**Do Not Omit Closing Tags**: Although HTML5 allows you to omit closing tags, always close your tags.

### Write One List Item per Line

**Bad**
```html
<ul>
  <li>General</li><li>The root Element</li><li>Sections</li>...
</ul>
```

**Good**
```html
<ul>
  <li>General</li>
  <li>The root Element</li>
  <li>Sections</li>
  ...
</ul>
```

### Avoid Ending `/` for Empty Elements
For empty elements, avoid ending the tag with a `/`.

**Bad**
```html
<img alt="HTML Best Practices" src="/img/logo.png" />
<br />
```

**Good**
```html
<img alt="HTML Best Practices" src="/img/logo.png">
<br>
```

### Proper Progression of Heading Tags
A page should always have an `h1` tag that describes what that page is about. Ideally, a page should have only a single `h1` tag. The page should then progressively go from `h1` to `h2` and then to `h3` and so on.

**Bad**
```html
<h1>My Page</h1>
<h3>Joe Black</h3>
<h4>Jon Doe</h4>
```

**Good**
```html
<h1>My Page</h1>
<h2>Joe Black</h2>
<h3>Jon Doe</h3>
```

## Attributes

### Attribute Order
HTML attributes should come in this particular order for easier reading of code.
- class
- id, name
- data-\*
- src, for, type, href, value
- title, alt
- role, aria-\*

Classes make for great reusable components, so they come first. Ids are more specific and should be used sparingly (e.g., for in-page bookmarks), so they come second.

### Use `download` Attribute for Downloading Resources
This will ensure that the resource is downloaded rather than opened. This works on IE 10+, and for lower browsers, it doesn't make any difference.
```html
<a download href="/downloads/offline.zip">offline version</a>
```

### Omit Boolean Attribute Value

**Bad**
```html
<audio autoplay="autoplay" src="/audio/theme.mp3">
<input type="text" disabled="disabled" name="txtFirstName">
```

**Good**
```html
<audio autoplay src="/audio/theme.mp3">
<input type="text" disabled name="txtFirstName">
```

### Do Not Use `id` Attribute Unnecessarily
Unless needed avoid giving ID attributes to every element that you create.

### Boolean Attributes
A boolean attribute is one that needs no declared value. XHTML required you to declare a value, but HTML5 has no such requirement. In short, don't add a value.

**Bad**
```html
<input type="text" disabled="true">
<input type="checkbox" value="1" checked="true">
<select>
  <option value="1" selected="true">1</option>
</select>
```

**Good**
```html
<input type="text" disabled>
<input type="checkbox" value="1" checked>
<select>
  <option value="1" selected>1</option>
</select>
```

### Forms

## Wrap Labels or Use `for` Attribute
While writing forms with controls inside them, the labels should either:
#### Wrap the Control
This is useful if you do not wish to specify the `ID` attribute for the control.
```html
<p>
  <label>Query: <input name="txtSearch" type="text"></label>
</p>
```

#### Use the `for` Attribute and Attach the Label with a Control
```html
<label for="txtSearch">Query: </label><input id="txt-search" name="txtSearch" type="text">
```

### Wrap Your Controls Inside a 'form' Tag
This is a good practice and should be followed, even if the control(s) data is submitted via AJAX. This allows end users to press enter to submit the data to the server.

### Form Should Have Input Type 'submit'
Every form should have an input with type submit, even if the control(s) data is submitted via AJAX. One of the benefits of this is that it will automatically be clicked when the user presses the enter button.

### Specify `maxlength` for Every Textbox
Ensure that you specify a `maxlength` for every textbox control that you use.

### Use Proper Input Type
If the field takes a number, please use `type="number"`, if it takes email use `type="email"`. This is especially useful in mobile devices as the type of keyboard that appears due to this will change.

## Naming guideline

### General

- Always specify a <span style="color: #ff9900;">`DOCTYPE`</span>, in our case it will almost always be <span style="color: #ff9900;">``</span>, if you think anything else is more appropriate please contact your mentor.
- The document character set is to be specified as UTF-8. Example : <span style="color: #ff9900;">`<meta charset="utf-8">`</span>
- HTML should not be mixed with presentation logic.
    - Do not use <span style="color: #ff9900;">`<center>`</span> and <span style="color: #ff9900;">`<marquee>`</span> tags or other tags or attributes that are associated with presentation.
    - Do not use <span style="color: #ff9900;">`align`, `width`, `height`</span> attributes in HTML. Use CSS attributes instead.

### Tags

- HTML tags should always be in lower case.
- For self closing tags, do **NOT** use a closing tags or a slash at the end. Eg: <span style="color: #ff9900;">`img`, `br`</span> and <span style="color: #ff9900;">`hr`</span>

#### Example :

**Correct**

```html
<input type="text">
<img src="hello.png" alt="Hello World">
```

**Incorrect**

```html
<input type="text" />
<img src="hello.png" alt="Hello World"/>
```

### Attributes

- Attribute names should always be in lower case.
- Attribute values should always be enclosed in double quotes.
- **Class** attributes should be in all **LOWER** case, with each word separated by a hyphen.
- Image tags should always be accompanied by an <span style="color: #ff9900;">`alt`</span> attribute.
- For input controls **ID** should be prefixed with the type of control.
- Following prefix should be used when using element of given type -

   <table>
  <thead>
    <tr>
      <th>Control</th>
      <th>Prefix</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Label</td>
      <td>lbl</td>
    </tr>
    <tr>
      <td>TextBox</td>
      <td>txt</td>
    </tr>
    <tr>
      <td>Button</td>
      <td>btn</td>
    </tr>
    <tr>
      <td>Hyperlink</td>
      <td>lnk</td>
    </tr>
    <tr>
      <td>Select</td>
      <td>ddl</td>
    </tr>
    <tr>
      <td>Checkbox</td>
      <td>chk</td>
    </tr>
    <tr>
      <td>RadioButton</td>
      <td>rdo</td>
    </tr>
    <tr>
      <td>File</td>
      <td>flo</td>
    </tr>
    <tr>
      <td>Image</td>
      <td>img</td>
    </tr>
    <tr>
      <td>Table</td>
      <td>tbl</td>
    </tr>
  </tbody>
</table>



**Example**

```html
<input class="form-control" id="txt-firstName" type="text">
<div class="row">
    <div></div>
    <div class="selected-row"></div>
    <div></div>
</div>
```
# Enforcing Tool and Config

- [W3C Validator](https://validator.w3.org/): Validate your HTML here.
- Use ESLint for linting. https://github.com/BenoitZugmeyer/eslint-plugin-html