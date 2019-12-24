from config.tags_config import get_opening_tag, get_closing_tag


def get_content_array(tiptap_json):
    """
            Get Content of Tiptap's json

            Args
            ----
            tiptap_json : dict
                titap_json to be converted
    """
    if tiptap_json['type'] == 'doc':
        return tiptap_json['content']
    else:
        raise Exception('Not Doc Type')


def get_string_with_marks(line_dict):
    """
            Get HTML string for marked text

            Args
            ----
            line_dict : dict
                :key marks : marks array of mark-dict { 'type': ''}
                     text : text
    """
    html_string = ""
    text = line_dict['text']
    marks_arr = []
    if 'marks' in line_dict:
        marks_arr = line_dict['marks']
    for mark in marks_arr:
        html_string += get_opening_tag(mark['type'])
    html_string += text

    marks_arr.reverse()
    for mark in marks_arr:
        html_string += get_closing_tag(mark['type'])
    return html_string


def get_html_string_for_dict(line_dict):
    """
            Get HTML string for given dict

            Args
            ----
            line_dict : dict
                :key type : element_type
                     attrs : element_attrs
                     content: element_content_array
    """
    html_string = ""
    type = line_dict['type']
    if type in ['blockquote', 'code_block', 'ordered_list', 'bullet_list', 'paragraph', 'list_item']:
        html_string += get_opening_tag(type) + get_html_string_for_arr(line_dict['content']) + get_closing_tag(type)
    elif type == 'horizontal_rule':
        html_string += get_opening_tag(type)
    elif type =='heading':
        html_string += get_opening_tag(type, attrs=line_dict['attrs']) + get_html_string_for_arr(line_dict['content'])\
                      + get_closing_tag(type, attrs=line_dict['attrs'])
    elif type == 'text':
        html_string += get_string_with_marks(line_dict)
    # print(html_string)
    return html_string


def get_html_string_for_arr(arr):
    """
            Get HTML string for given list of dicts

            Args
            ----
            arr : list
    """
    html_string = ""
    for line_dict in arr:
        html_string += get_html_string_for_dict(line_dict)
    return html_string


def convert_to_html_string(json_file):
    """
            Get HTML string for given list of dicts

            Args
            ----
            json_file : dict
                titap_json to be converted
    """
    return get_html_string_for_arr(get_content_array(json_file))


if __name__ == "__main__":
    # print(convert_to_html_string(file))
    pass