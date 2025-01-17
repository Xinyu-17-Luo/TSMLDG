import argparse

from TSMLDG import MetaFrameWork

parser = argparse.ArgumentParser(description='TSMLDG train args parser')
parser.add_argument('--name', default='exp', help='name of the experiment')
parser.add_argument('--source', default='GSIM', help='source domain name list, capital of the first character of dataset "GSIMcuv"(dataset should exists first.)')
parser.add_argument('--target', default='C', help='target domain name, only one target supported')
parser.add_argument('--inner-lr', type=float, default=1e-3, help='inner learning rate of meta update')
parser.add_argument('--outer-lr', type=float, default=5e-3, help='outer learning rate of network update')
parser.add_argument('--resume', action='store_true', help='resume the training procedure')
# parser.add_argument('--debug', action='store_true', help='set the workers=0 and batch size=1 to accelerate debug') # MetaFrameWork() doesn't have this parameter
parser.add_argument('--train-size', type=int, default=8, help='the batch size of training')
parser.add_argument('--test-size', type=int, default=16, help='the batch size of evaluation')
parser.add_argument('--train-num', type=int, default=1,
                    help='every ? iteration do one meta train, 1 is meta train, 10000000 is normal supervised learning.')
parser.add_argument('--no-source-test', action='store_false', help='whether test the validation performance in source domain when training')


def train():
    args = vars(parser.parse_args())
    print(args)
    for name in args['source']:
        # my datasets
        assert name in 'WBIACD'
    assert args['target'][0] in  'WBIACD'
    assert len(args['target'])
    framework = MetaFrameWork(**args)
    framework.do_train()


if __name__ == '__main__':
    from utils.task import FunctionJob
    # parameter to be changed gpus, minimum_memory
    job = FunctionJob([train], gpus=[[3, 1, 2, 0]])
    job.run(minimum_memory=20000)
    # train()
