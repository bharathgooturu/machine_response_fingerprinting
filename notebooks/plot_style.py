import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
import numpy as np

PALETTE = {
    'bg':         '#FAFAF8',
    'panel':      '#FFFFFF',
    'grid':       '#EBEBEB',
    'tick':       '#999896',
    'label':      '#52514E',
    'title':      '#0B0B0B',
    'border':     '#D8D7D2',
    'blue':       '#2A78D6',
    'orange':     '#EB6834',
    'event_load': '#EB6834',
    'event_drag': '#EDA100',
    'event_volt': '#6250D6',
}

FAULT_COLORS = {
    'Healthy':                   '#2C2C2A',
    'Bearing fault (B x2.0)':   '#E34948',
    'Winding fault (R x1.5)':   '#2A78D6',
    'Mechanical fault (J x1.3)':'#EB6834',
    'Supply fault (V x0.90)':   '#1BAF7A',
}
FAULT_DASHES = {
    'Healthy':                   (None, None),
    'Bearing fault (B x2.0)':   (6, 3),
    'Winding fault (R x1.5)':   (3, 3),
    'Mechanical fault (J x1.3)':(8, 3),
    'Supply fault (V x0.90)':   (4, 2),
}

EVENT_META = {
    'load_torque':  {'time': 2.0, 'color': PALETTE['event_load'], 'label': 'Load torque +5%'},
    'viscous_drag': {'time': 3.0, 'color': PALETTE['event_drag'], 'label': 'Viscous drag +10%'},
    'voltage_dip':  {'time': 4.0, 'color': PALETTE['event_volt'], 'label': 'Voltage dip −3%'},
}

def apply_base_style():
    plt.rcParams.update({
        'figure.facecolor':     PALETTE['bg'],
        'axes.facecolor':       PALETTE['panel'],
        'axes.edgecolor':       PALETTE['border'],
        'axes.linewidth':       0.6,
        'axes.grid':            True,
        'axes.axisbelow':       True,
        'grid.color':           PALETTE['grid'],
        'grid.linewidth':       0.6,
        'grid.linestyle':       '-',
        'xtick.color':          PALETTE['tick'],
        'ytick.color':          PALETTE['tick'],
        'xtick.labelsize':      9,
        'ytick.labelsize':      9,
        'xtick.major.size':     0,
        'ytick.major.size':     0,
        'xtick.major.pad':      6,
        'ytick.major.pad':      6,
        'axes.labelcolor':      PALETTE['label'],
        'axes.labelsize':       10,
        'axes.labelpad':        10,
        'axes.spines.top':      False,
        'axes.spines.right':    False,
        'text.color':           PALETTE['title'],
        'font.family':          'sans-serif',
        'font.sans-serif':      ['Inter', 'SF Pro Text', 'Helvetica Neue', 'Arial', 'DejaVu Sans'],
        'font.size':            10,
        'figure.dpi':           150,
        'savefig.dpi':          200,
        'savefig.facecolor':    PALETTE['bg'],
        'savefig.bbox':         'tight',
        'savefig.pad_inches':   0.25,
        'lines.linewidth':      1.8,
        'lines.solid_capstyle': 'round',
    })

def draw_event_lines(ax):
    for name, meta in EVENT_META.items():
        ax.axvline(meta['time'], color=meta['color'],
                   linewidth=1.0, linestyle='--', alpha=0.7, zorder=2)

def add_event_legend(ax):
    handles = [
        Line2D([0], [0], color=m['color'], linewidth=1.2,
               linestyle='--', alpha=0.85, label=m['label'])
        for m in EVENT_META.values()
    ]
    leg = ax.legend(
        handles=handles, loc='upper right', fontsize=8,
        frameon=True, framealpha=0.92, edgecolor=PALETTE['border'],
        facecolor=PALETTE['panel'], handlelength=2.2,
        borderpad=0.7, labelspacing=0.45,
        title='Stimulus events', title_fontsize=8,
    )
    leg.get_title().set_color(PALETTE['label'])