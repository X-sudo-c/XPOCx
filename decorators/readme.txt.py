# i am learning about how to use decorators this is a crucial step to advancing my python skills 


# import subprocess
# import click
# from typing import List

# def run_command(cmd: List[str], input_data: str = None) -> str:
#     """Run a shell command and return its output."""
#     try:
#         result = subprocess.run(
#             cmd,
#             input=input_data,
#             capture_output=True,
#             text=True,
#             check=True,
#         )
#         return result.stdout.strip()
#     except subprocess.CalledProcessError as e:
#         click.echo(f"Error running {' '.join(cmd)}: {e.stderr}", err=True)
#         return ""

# @click.group()
# def cli():
#     """Subdomain Reconnaissance Tool (AssetFinder + SubFinder)"""
#     pass

# @cli.command()
# @click.argument("domain")
# @click.option("--subs-only", is_flag=True, help="Only include subdomains (exclude related domains)")
# @click.option("--alive", is_flag=True, help="Check which domains are live (using httprobe)")
# @click.option("--output", "-o", type=click.Path(), help="Save results to a file")
# def scan(domain, subs_only, alive, output):
#     """Run AssetFinder and SubFinder on a domain."""
#     # Run AssetFinder
#     assetfinder_cmd = ["assetfinder"]



# so in the code above function was called before the @click decorators which was weird for me 
# because normally the decorator eg "@click.command()" would beb called before a function would be defined

#SO id be learning about decorators in detail to see how things go 
