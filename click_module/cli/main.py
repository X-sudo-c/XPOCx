import click


VERSION = "0.1.0"

@click.command()
@click.version_option(VERSION)
@click.argument("--name", nargs=2)
def profile(names):
    print(names)





if __name__ =='__main__':
    profile
