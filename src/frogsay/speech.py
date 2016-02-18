# -*- coding: utf-8 -*-
import textwrap


def make_frog_fresco(text, width, padding=8):
    """\
    Formats your lovely text into a speech bubble spouted by this adorable
    little frog.
    """
    stem = r'        /'
    frog = r"""
{text}
{stem}
  @..@
 (----)
( >__< )
^^ ~~ ^^"""
    offset = len(stem) - 1

    formatted_indent = ' ' * offset
    formatted_text = textwrap.fill(text, width=width-padding,
        initial_indent=formatted_indent, subsequent_indent=formatted_indent)

    return frog.format(stem=stem, text=formatted_text)
