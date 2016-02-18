# -*- coding: utf-8 -*-
import os

import click

from frogsay.client import open_client
from frogsay.speech import make_frog_fresco


def get_cache_file(app_name='frogsay'):
    return os.path.join(click.get_app_dir(app_name), 'croak_cache')


@click.command()
def cli():
    """\
    Frogsay generates an ASCII picture of a FROG spouting a FROG tip.

    FROG tips are fetched from frog.tips's API endpoint when needed,
    otherwise they are cached locally in an application-specific folder.
    """
    with open_client(cache_file=get_cache_file()) as client:
        tip = client.frog_tip()

    terminal_width = click.termui.get_terminal_size()[0]
    wisdom = make_frog_fresco(tip, width=terminal_width)

    click.echo(wisdom)
