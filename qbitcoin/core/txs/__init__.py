from importlib import import_module

TYPENAME_MAP = {
    'transfer': 'TransferTransaction',
    'coinbase': 'CoinBase',
    'latticePK': 'LatticeTransaction',
    'message': 'MessageTransaction',
    'token': 'TokenTransaction',
    'transfer_token': 'TransferTokenTransaction',
    'slave': 'SlaveTransaction',

    'multi_sig_create': 'MultiSigCreate',
    'multi_sig_spend': 'MultiSigSpend',
    'multi_sig_vote': 'MultiSigVote',
}

TYPENAME_PACKAGE = {
    'transfer': 'qbitcoin.core.txs',
    'coinbase': 'qbitcoin.core.txs',
    'latticePK': 'qbitcoin.core.txs',
    'message': 'qbitcoin.core.txs',
    'token': 'qbitcoin.core.txs',
    'transfer_token': 'qbitcoin.core.txs',
    'slave': 'qbitcoin.core.txs',

    'multi_sig_create': 'qbitcoin.core.txs.multisig',
    'multi_sig_spend': 'qbitcoin.core.txs.multisig',
    'multi_sig_vote': 'qbitcoin.core.txs.multisig',

    'proposal_vote': 'qbitcoin.core.txs.proposal',
}


def build_tx(pb_tx_type, *args, **kwargs):
    try:
        tx_class_name = TYPENAME_MAP[pb_tx_type]
        package = TYPENAME_PACKAGE[pb_tx_type]
        tx_module = import_module('.' + tx_class_name, package=package)
        tx_class = getattr(tx_module, tx_class_name)
        return tx_class(*args, **kwargs)

    except(AttributeError, ModuleNotFoundError) as e:  # noqa
        raise ImportError("{} is not defined as a transaction type".format(pb_tx_type))
