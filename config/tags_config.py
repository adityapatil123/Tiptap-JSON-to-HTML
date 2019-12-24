OPENING_TAGS = {
    'blockquote': '<blockquote>',
    'horizontal_rule': '<hr>',
    # Heading Remaining
    'code_block': '<pre><code>',
    'bullet_list': '<ul>',
    'ordered_list': '<ol>',
    'list_item': '<li>',
    'paragraph': '<p>',
    'bold': '<strong>',
    'italic': '<em>',
    'strike': '<s>',
    'underline': '<u>',
    'code': '<code>'
}


CLOSING_TAGS = {
    'blockquote': '</blockquote>',
    # Heading Remaining
    'code_block': '</code></pre>',
    'bullet_list': '</ul>',
    'ordered_list': '</ol>',
    'list_item': '</li>',
    'paragraph': '</p>',
    'bold': '</strong>',
    'italic': '</em>',
    'strike': '</s>',
    'underline': '</u>',
    'code': '</code>'
}


def get_opening_tag(type, **kwargs):
    if type == 'heading':
        return f"<h{str(kwargs['attrs']['level'])}>"
    else:
        return OPENING_TAGS[type]


def get_closing_tag(type, **kwargs):
    if type == 'heading':
        return f"</h{str(kwargs['attrs']['level'])}>"
    else:
        return CLOSING_TAGS[type]