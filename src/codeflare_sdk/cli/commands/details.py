import click

from codeflare_sdk.cluster.cluster import get_cluster


@click.group()
def cli():
    """Get the details of a specified resource"""
    pass


@cli.command()
@click.argument("name", type=str)
@click.option("--namespace", type=str)
@click.pass_context
def raycluster(ctx, name, namespace):
    """Get the details of a specified RayCluster"""
    namespace = namespace or ctx.obj.current_namespace
    try:
        cluster = get_cluster(name, namespace)
    except FileNotFoundError:
        click.echo(f"Cluster {name} not found in {namespace} namespace")
        return
    cluster.details()