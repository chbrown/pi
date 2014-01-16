# pi.commands

One goal with `pi` is to make installation tools that are more programmer friendly, rather than command-line-centric.

Thus, `pi.commands` priorities follow this order:

1. Expose functionality that makes package manipulation easier.
2. Connect this functionality directly to the `pi` command.

    Each module (command) in `commands.*` should have a CLI entry-point with the following signature:

            def cli(parser):
                # parser is an instance of argparse.ArgumentParser
                opts = parser.parse_args()
