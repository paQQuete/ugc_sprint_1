import argparse


def args_parser():
    _ = argparse.ArgumentParser()
    _.add_argument('-t', dest='topic', required=True, type=str)
    _.add_argument('-o', dest='offset_group', nargs='?', default='etl_default', type=str)
    return _
