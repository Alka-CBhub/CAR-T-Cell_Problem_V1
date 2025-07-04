# plot_utils.py

# Import necessary library
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D 
# Plot style
def set_plot_style(dpi = 500):
    """
    Call once at the top of any script to apply global rcParams.
    """
    mpl.rcParams.update({
        # Use serif fonts throughout
        "text.usetex": False,
        "font.family": "serif",
        # Axes labels and titles
        "axes.labelsize": 16,
        "axes.titlesize": 16,
        # Tick‐label sizes
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        # Legend font size
        "legend.fontsize": 13,
        # Default line thickness and marker size
        "lines.linewidth": 2.2,
        "lines.markersize": 7,
        # Grid appearance
        "grid.linestyle": "--",
        "grid.alpha": 0.6,
        # Higher resolution figures
        "figure.dpi": 500
    })


# Spline format
## 2D
def set_spines_black(ax):
    """
    Given a Matplotlib Axes instance, make every spine black and linewidth=2.
    """
    for spine in ax.spines.values():
        spine.set_linewidth(2)
        spine.set_edgecolor('k')


## 3D
def set_spines_black_3d(ax):
    # color axis lines
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.line.set_color('black')
        axis.line.set_linewidth(2)
    # white panes with black edges
    for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
        pane.set_facecolor('white')
        pane.set_edgecolor('black')
