from difflib import SequenceMatcher
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def diff(ab_list, autoescape=True):
    a, b = ab_list

    if autoescape:
        a = conditional_escape(a)
        b = conditional_escape(b)

    sm = SequenceMatcher(a=a, b=b)
    result = ''
    for op, a_start, a_end, b_start, b_end in sm.get_opcodes():
        a_chunk = a[a_start:a_end]
        b_chunk = b[b_start:b_end]
        if op == 'insert':
            result += "<span class='diff_added'>{}</span>".format(b_chunk)
        elif op == 'delete':
            result += "<span class='diff_removed'>{}</span>".format(a_chunk)
        elif op == 'replace':
            result += "<span class='diff_removed'>{}</span><span class='diff_added'>{}</span>".format(a_chunk, b_chunk)
        else: # equal
            result += a_chunk
    return mark_safe(result)