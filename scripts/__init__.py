import click

from passwords.manager import PasswordFilesystemBackend


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj["MANAGER"] = PasswordFilesystemBackend()
    pass


@cli.command()
@click.pass_context
@click.argument("key", type=str)
def get(ctx, key):
    manager = ctx.obj["MANAGER"]
    click.echo(manager.get(key))


@cli.command()
@click.pass_context
@click.argument("key", type=str)
@click.argument("value", type=str)
def save(ctx, key, value):
    manager = ctx.obj["MANAGER"]
    manager.save(key, value)

