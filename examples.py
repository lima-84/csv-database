"""
    author: @lima84

    Generates .csv datasets initially for testing with pysid.
"""
#%%
from csv_data import gen_data, save_data
from os.path import exists

def gen_csv(filename, Ao, Bo, N):
    """
    author: @lima84
    Generates a set of input and output data following:
        y(t) = Go(q)*u(t) + Ho(q)*e(t),
    where G(q) = Bo(q)/Ao(q) and H(q) = 1/Ao(q). Saves into 'filename'

    Parameters
    ----------

    Ao : array_like
        Ao(q) polynomial coefficients.
    Bo : array_like
        Bo(q) polynomial coefficients.
    N : int
        Number of samples for the dataset.
    Returns
    -------

    """

    data = gen_data(Ao, Bo, N)
    if not exists('./' + filename):
        save_data(data, filename)

#%%
N = 1000

#Ex1: zpk([-0.2],[0.6, 0.6], 0.5, Ts)
gen_csv("ex1.csv",[1, -1.2, 0.36], [0, 0.5, 0.1], N)

#Ex2: zpk([0.4, 0.4, 0.4], [0.3, 0.5, 0.5, 0.7, 0.9], 1 , Ts)
gen_csv("ex2.csv",[1, -2.9, 3.26, -1.774, 0.4665, -0.04725], [1, -1.2, 0.48, -0.064], N)
