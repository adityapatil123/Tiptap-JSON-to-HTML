import json

json_file1 = {
  "type": "doc",
  "content": [
    {
      "type": "heading",
      "attrs": {
        "level": 1
      },
      "content": [
        {
          "type": "text",
          "text": "Example Heading"
        }
      ]
    },
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "This is simple "
        },
        {
          "type": "text",
          "marks": [
            {
              "type": "bold"
            }
          ],
          "text": "example"
        },
        {
          "type": "text",
          "text": " text."
        }
      ]
    }
  ]
}


json_file2 = {
  "type": "doc",
  "content": [
    {
      "type": "blockquote",
      "content": [
        {
          "type": "heading",
          "attrs": {
            "level": 2
          },
          "content": [
            {
              "type": "text",
              "text": "Export HTML or JSON"
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "marks": [
                {
                  "type": "underline"
                }
              ],
              "text": "baha"
            }
          ]
        }
      ]
    },
    {
      "type": "horizontal_rule"
    },
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "You are able to export your data as "
        },
        {
          "type": "text",
          "marks": [
            {
              "type": "code"
            }
          ],
          "text": "HTML"
        },
        {
          "type": "text",
          "text": " or "
        },
        {
          "type": "text",
          "marks": [
            {
              "type": "code"
            }
          ],
          "text": "JSON"
        },
        {
          "type": "text",
          "text": "."
        }
      ]
    }
  ]
}

json_file3 = {
  "type": "doc",
  "content": [
    {
      "type": "blockquote",
      "content": [
        {
          "type": "bullet_list",
          "content": [
            {
              "type": "list_item",
              "content": [
                {
                  "type": "paragraph",
                  "content": [
                    {
                      "type": "text",
                      "text": "This is "
                    },
                    {
                      "type": "text",
                      "marks": [
                        {
                          "type": "strike"
                        }
                      ],
                      "text": "some"
                    },
                    {
                      "type": "text",
                      "text": " "
                    },
                    {
                      "type": "text",
                      "marks": [
                        {
                          "type": "code"
                        }
                      ],
                      "text": "inserted"
                    },
                    {
                      "type": "text",
                      "text": " "
                    },
                    {
                      "type": "text",
                      "marks": [
                        {
                          "type": "code"
                        }
                      ],
                      "text": "text"
                    },
                    {
                      "type": "text",
                      "text": "."
                    }
                  ]
                },
                {
                  "type": "code_block",
                  "content": [
                    {
                      "type": "text",
                      "text": "ksmknsks"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}

EXAMPLES = {
    json.dumps(json_file1): "<h1>Example Heading</h1><p>This is simple <strong>example</strong> text.</p>",
    json.dumps(json_file2): "<blockquote><h2>Export HTML or JSON</h2><p><u>baha</u></p></blockquote><hr><p>You are able to export your data as <code>HTML</code> or <code>JSON</code>.</p>",
    json.dumps(json_file3): "<blockquote><ul><li><p>This is <s>some</s> <code>inserted</code> <code>text</code>.</p><pre><code>ksmknsks</code></pre></li></ul></blockquote>"
}