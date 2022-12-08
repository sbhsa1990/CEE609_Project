
"""
@author: Babak Asadollah
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import glob

csfont = {'fontname':'Times New Roman'}
plt.rcParams["font.family"] = "Times New Roman"
font = {'weight' : 'bold', 'size'   : 14}
matplotlib.rc('font', **font)

fileList=glob.glob("*.xlsx")
dfList=[]


for filename in fileList:
    data = pd.read_excel(filename)
    x = data[["R", "RMSE", "MAE", "NSE", "Mean"]]
    y = data['CMIP6 source']
    Performance_Indices = y.to_list()
    
    # sphinx_gallery_thumbnail_number = 2
    
    X_axis = ["R", "RMSE", "MAE", "NSE", "Average"]
    
    def heatmap(data, row_labels, col_labels, ax=None,
                cbar_kw={}, cbarlabel="", **kwargs):
    
        if not ax:
            ax = plt.gca()
    
        # Plot the heatmap
        im = ax.imshow(data, **kwargs)
    
        # Create colorbar
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        
        # Color bar label properties
        cbar.ax.set_ylabel(cbarlabel, rotation=90,
                           va="bottom", fontsize=16,
                           fontweight="bold", labelpad=25,**csfont)
    
    
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_yticks(np.arange(data.shape[0]))
        ax.set_xticklabels(col_labels, fontsize=14, fontweight="bold",**csfont)
        ax.set_yticklabels(row_labels, fontsize=16, fontweight="bold",**csfont)
    
        # Let the horizontal axes labeling appear on top.
        ax.tick_params(top=False, bottom=True,
                       labeltop=False, labelbottom=True)
    
        # Rotate the Bottom labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
                 rotation_mode="anchor",**csfont)
    
        # Turn spines off and create white grid.
        for edge, spine in ax.spines.items():
            spine.set_visible(False)
    
        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    
        # White Grids
        # ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
        # ax.tick_params(which="minor", bottom=False, left=False)
        
        return im, cbar
    
    
    def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                         textcolors=["black", "white"],
                         threshold=None, **textkw):
    
    
        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()
    
        # Normalize the threshold to the images color range.
        if threshold is not None:
            threshold = im.norm(threshold)
        else:
            threshold = im.norm(data.max())/2.
    
        # Set default alignment to center, but allow it to be
        # overwritten by textkw.
        kw = dict(horizontalalignment="center",
                  verticalalignment="center")
        kw.update(textkw)
    
        # Get the formatter in case a string is supplied
        if isinstance(valfmt, str):
            valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)
    
        # Loop over the data and create a `Text` for each "pixel".
        # Change the text's color depending on the data.
        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
                text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
                texts.append(text)
    
        return texts
    
    
    
    fig, ax = plt.subplots(figsize=(5,10))
    ax.set_aspect(aspect=0.8)
    
    im, cbar = heatmap(x, Performance_Indices, X_axis, ax=ax,
                       cmap="inferno_r", cbarlabel="Normilzed metrics")
    # Standardized error
    
    # White text labels inside squares
    texts = annotate_heatmap(im, valfmt="{x:.2f}", fontweight="bold",**csfont,
                             fontsize=17)
    
    # Set Label for x and y axis
    ax.set_xlabel('Performance metrics', fontsize=18, fontweight="bold",
                  labelpad=1,**csfont)
    ax.set_ylabel('CMIP6 sources', fontsize=18, fontweight="bold",
                  labelpad=10,**csfont)
    
    # Set Label for title
    ax.set_title(filename[19:23], fontweight="bold", pad=20, fontsize=20)
    
    
    
    #fig.savefig('destination_path.jpeg', format='jpeg', dpi=300)
    
    #fig.tight_layout()
    #plt.show()
    plt.savefig(filename[19:23] + '.jpg', format='jpg', bbox_inches='tight', dpi=300)

