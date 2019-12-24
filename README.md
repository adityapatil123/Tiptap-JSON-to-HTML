# Tiptap JSON to HTML
Convert tiptap JSON to HTML(similar to titap HTML)

## Aim:
input: JSON (Tiptap)
output: HTML (Tiptap)

## Hierarchy of Elements:
- doc
- blackquote
- horizontal_rule
- heading / code_block / ordered_list(child-list_item-paragraph) / bullet_list(child-list_item-paragraph) / paragraph
- text

## Elements Description:
### doc -(type, content)
- json:
```json
{
    "type": "doc",
    "content": []
}
```

### blackquote -(type, content)
- content-child : child can be anything except text
- json:
```json
{
    "type": "blackquote",
    "content": []
}
```
- html-tag: 
```html
<blockquote> .. </blockquote>
```

### horizontal_rule -(type)
- content-child : no child
- json:
```json
{
    "type": "horizontal_rule"
}
```
- html-tag: 
```html
<hr>
```

### heading -(type, attrs, content)
- content-child : (text)
- json:
```json
{
    "type": "heading",
    "attrs": {
            "level": 1
            },
    "content": []
}
```
- html-tag:
```html 
<h1> .. </h1>
```

### code_block -(type, content)
- content-child : (text)
- json:
```json
{
    "type": "code_block",
    "content": []
}
```
- html-tag:
```html 
<pre><code> .. </code></pre>
```

### bullet_list -(type, content)
- content-child : (list_item)
- json:
```json
{
    "type": "bullet_list",
    "content": [
    {
      "type": "list_item",
      "content": []
    }
    ]
}
```
- html-tag:
```html 
<ul>
    <li> .. </li> 
    <li> .. </li> 
</ul>
```

### ordered_list -(type, attrs,  content)
- content-child : (list_item)
- json:
```json
{
    "type": "ordered_list",
    "attrs": {
            "order": 1
          },
    "content": [
    {
      "type": "list_item",
      "content": []
    }
    ]
}
```
html-tag:
```html 
<ol>
    <li> .. </li> 
    <li> .. </li> 
</ol>
```

### list_item -(type,  content)
- content-child : (paragraph)
- json:
```json
{
    "type": "list_item",
    "content": []
}
```
html-tag:
```html 
<li> .. </li>
```

### paragraph -(type, content)
- content-child : (text)
- json:
```json
{
    "type": "paragraph",
    "content": []
}
```
- html-tag:
```html 
<p> .. </p>
```

### text -(type, marks, text)
- content-child : no child
- json:
```json
{
    "type": "text",
    "marks": [
    {
      "type": "bold"
    },
    {
      "type": "italic"
    }
    ],
    "text": ""
}
```
- html-tag:
```html 
<strong><em> .. </em></strong>
```

### Text marks:
- content-child : no child
```json
{
  "type": "bold"
}
```
- html-tag:
```html
<strong>bold</strong>
<em>italic</em>
<s>strike</s>
<u>underline</u>
<code>code </code>
```

## Logic:
1. Got the content of ***doc*** from **get_content_array** function.
2. Made the opening and closing tags for all elements.
3. There are two things to be handled, one dict or list of dict. Hence made the two functions for them.
    - **get_html_string_for_dict**
    - **get_html_string_for_arr**
4. These functions will be called recursively and string will be given at lowest level.
5. Marks are handled for text with **get_string_with_marks**.
6. Finally, main function **convert_to_html_string** converts json to html.
7. Wrote the 3 cases and checked with nosetests.