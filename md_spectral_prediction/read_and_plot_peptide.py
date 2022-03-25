# libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
#from sympy import re
import os

def main(pred_file_path: str, spec_id_select: str, output_directory: str):
    spectra = pd.read_csv(pred_file_path)
    peptide = select_peptide(spectra, spec_id_select)
    plot_spectrum(output_directory, peptide)
    return

def select_peptide(spectra: DataFrame, spec_id_select: str):
    
    #spectra = spectra.set_index('spec_id')

    peptide = spectra.loc[spectra.spec_id == spec_id_select,
    ['spec_id','ion','mz','prediction', 'peptide']].reset_index(drop=True)
    peptide = peptide.sort_values('mz', ascending=True)

    return peptide

def plot_spectrum(output_directory: str, peptide: DataFrame):
    x=peptide.loc[:,'mz'].reset_index(drop=True)
    y=peptide.loc[:,'prediction'].reset_index(drop=True)

    sequence = peptide.peptide[0]

    ion_type = peptide.loc[:, 'ion'].reset_index(drop=True)
    my_color = np.where(ion_type=='B', 'orange', 'skyblue')
    
    
    plt.vlines(x=x, ymin=0, ymax=y, color=my_color, alpha=0.4)
    plt.scatter(x, y, color=my_color, s=1, alpha=1)

    # Add title and axis names
    plt.title(f"Peptide Sequence:{sequence}", loc='left')
    plt.xlabel('m/z')
    plt.ylabel('intensity')

    plt.show()

    file_name = "spectrum" + peptide.iloc[0,0]+ ".png"
    img = img.save(os.path.join(output_directory, file_name))


