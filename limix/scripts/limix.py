from argparse import ArgumentParser


def do_see(args):
    import limix

    ft = limix.io.file_type(args.file)

    if ft == 'hdf5':
        limix.io.hdf5.see(args.file, show_chunks=args.show_chunks)
    elif ft == 'csv':
        limix.io.csv.see(args.file)
    else:
        print("Unknown file type: %s." % args.file)


def see_parser(parser):
    parser.add_argument('file', help='file path')
    parser.add_argument(
        '--show-chunks',
        dest='show_chunks',
        action='store_true',
        help='show chunk information')
    parser.set_defaults(show_chunks=False)
    parser.set_defaults(func=do_see)
    return parser

def entry_point():
    p = ArgumentParser()

    subparsers = p.add_subparsers(title='subcommands')
    see_parser(subparsers.add_parser('see'))

    args = p.parse_args()
    if hasattr(args, 'func'):
        func = args.func
        del args.func
        func(args)
    else:
        p.print_help()
