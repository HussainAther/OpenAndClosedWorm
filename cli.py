import argparse
import sys
from logger import setup_logger  # Make sure to integrate the logger we discussed earlier

def parse_args(args):
    parser = argparse.ArgumentParser(description="OpenWorm Enhanced CLI")
    parser.add_argument('-c', '--config', type=str, default='config.ini', help='Path to configuration file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
    subparsers = parser.add_subparsers(title='commands', description='Valid commands', help='Additional commands', dest='command')

    # Run simulation command
    run_parser = subparsers.add_parser('run', help='Run the simulation')
    run_parser.add_argument('-t', '--type', choices=['full', 'partial'], default='full', help='Type of simulation to run')

    # Export data command
    export_parser = subparsers.add_parser('export', help='Export data')
    export_parser.add_argument('-f', '--format', choices=['csv', 'json'], default='csv', help='Format of the export file')

    # System status command
    status_parser = subparsers.add_parser('status', help='View system status')

    return parser.parse_args(args)

def main():
    args = parse_args(sys.argv[1:])  # Excluding the first argument which is the script name
    
    logger = setup_logger()
    if args.verbose:
        logger.setLevel('DEBUG')  # Set logger to debug if verbose is true
    
    logger.info("Starting the application")

    if args.config:
        logger.info(f"Using configuration file: {args.config}")

    if args.command == 'run':
        logger.info(f"Running the {args.type} simulation")
        # Integration of simulation functionality goes here

    elif args.command == 'export':
        logger.info(f"Exporting data in {args.format} format")
        # Integration of data export functionality goes here

    elif args.command == 'status':
        logger.info("Checking system status")
        # Integration of status check functionality goes here

    logger.info("Application finished")

if __name__ == "__main__":
    main()

