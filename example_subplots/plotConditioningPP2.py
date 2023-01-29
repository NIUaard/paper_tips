# %load plot_phasescan1105compare2.py
import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.gridspec import GridSpec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib import lines

plt.style.use(r'./prlsinglecolumnlonger.mplstyle')


length_per_pixel_mm = 5.85480093676815e-05 * 1E3

colcen = 229
center_col = colcen
colmin = 1001
rowmin = 260

conditionning = np.loadtxt('conditioning_history.txt')


fig  = plt.figure()

gs1 = GridSpec(3, 3, wspace=0.55, hspace=0.1, left=0.15, right=0.85, top=0.85 )
ax1 = fig.add_subplot(gs1[1:, :])
ax2 = fig.add_subplot(gs1[0, 0])
ax3 = fig.add_subplot(gs1[0, 1])
ax4 = fig.add_subplot(gs1[0, 2])

ln1=ax1.plot(conditionning[:,0], conditionning[:,1]*1e-6,'o', alpha=0.25, markerfacecolor='none', label=r'$E_0$')
ax1.text(0.05, 0.92,r'{(a)}', ha='center', va='center', transform=ax1.transAxes)
ax1t = ax1.twinx()
ln1t=ax1t.plot(conditionning[:,0], conditionning[:,2], 's', color='C1', alpha=0.15, markerfacecolor='none', label=r'$R$')
ax1.plot([10000,10000],[-100, 1e5],'--', color='C8')
ax1.plot([37000,37000],[-100, 1e5],'--', color='C8')
ax1.plot([65000,65000],[-100, 1e5],'--', color='C8')
ax1.set_xlabel(r'number of pulses');
ax1.set_ylabel(r' $E_0$ (MV/m)', color='C0')
ax1.tick_params(axis='y', colors='C0')    
ax1t.set_ylabel(r'ratio $R$', color='C1')
ax1t.tick_params(axis='y', colors='C1')    
ax1t.set_ylim([0,1.5])
ax1.set_ylim([0,400])
# fig.tight_layout()
lns = ln1+ln1t
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=4)


# low power 
Pwr = np.loadtxt('LowPower.txt')
ax2.plot(Pwr[:,0], Pwr[:,1]*1e-3,'C2')
ax2.plot(Pwr[:,2], Pwr[:,3]*1e-3,'--', color='C3')
ax2.set_ylabel ('reflected signal (kV)')
ax2.yaxis.set_label_coords(-0.6,0.7)

ax2.set_xlim([-5, 25])
ax2.tick_params(top=True, bottom=False)
ax2.tick_params(labeltop=True, labelbottom=False)
ax2.set_title ('t (ns)')
ax2.text(0.2, 0.85,r'{(b)}', ha='center', va='center', transform=ax2.transAxes)

Pwr = np.loadtxt('MiddlePower.txt')
ax3.plot(Pwr[:,0], Pwr[:,1]*1e-3,'C2')
ax3.plot(Pwr[:,2], Pwr[:,3]*1e-3,'--', color='C3')
ax3.set_xlim([-5, 25])
#ax3.set_ylim([0, 25])
#ax3.axes.yaxis.set_ticklabels([])
ax3.tick_params(top=True, bottom=False)
ax3.tick_params(labeltop=True, labelbottom=False)
ax3.set_title ('t (ns)')
ax3.text(0.2, 0.85,r'{(c)}', ha='center', va='center', transform=ax3.transAxes)

Pwr = np.loadtxt('HighPower.txt')
ax4.plot(Pwr[:,0], Pwr[:,1]*1e-3,'C2')
ax4.plot(Pwr[:,2], Pwr[:,3]*1e-3,'--', color='C3')
ax4.set_xlim([-5, 25])
#ax4.axes.yaxis.set_ticklabels([])
ax4.set_title ('t (ns)')
ax4.tick_params(top=True, bottom=False)
ax4.tick_params(labeltop=True, labelbottom=False)
ax4.text(0.2, 0.85,r'{(d)}', ha='center', va='center', transform=ax4.transAxes)

transFigure = fig.transFigure.inverted()
xyA=[10000,400]
xyB=[0,0]
coord1 = transFigure.transform(ax1.transData.transform(xyA))
coord2 = transFigure.transform(ax2.transData.transform(xyB))
line = lines.Line2D(
    (coord1[0], coord2[0]),  # xdata
    (coord1[1], coord2[1]),  # ydata
    transform=fig.transFigure,
    color="C8",
)
fig.lines.append(line)


xyA=[37000,400]
xyB=[0,0]
coord1 = transFigure.transform(ax1.transData.transform(xyA))
coord2 = transFigure.transform(ax3.transData.transform(xyB))
line = lines.Line2D(
    (coord1[0], coord2[0]),  # xdata
    (coord1[1], coord2[1]),  # ydata
    transform=fig.transFigure,
    color="C8",
)
fig.lines.append(line)

xyA=[65000,400]
xyB=[0,0]
coord1 = transFigure.transform(ax1.transData.transform(xyA))
coord2 = transFigure.transform(ax4.transData.transform(xyB))
line = lines.Line2D(
    (coord1[0], coord2[0]),  # xdata
    (coord1[1], coord2[1]),  # ydata
    transform=fig.transFigure,
    color="C8",
)
fig.lines.append(line)


#axins1 = inset_axes(ax, width=0.5, height=0.5, loc=3, bbox_to_anchor=(170,520))
#axins1.plot(Pwr[:,0], Pwr[:,1]*1e-3,'C2')
#axins1.plot(Pwr[:,2], Pwr[:,3]*1e-3,'--', color='C3')
#axins1.set_xlim([-5, 25])
##axins1.set_yticks([])
#axins1.text(0.85, 0.85,r'{(b)}', ha='center', va='center', color='w', transform=axins1.transAxes)
plt.show()

fig.savefig('conditionning.png', transparent=True, dpi=300)
fig.savefig('conditionning.pdf', transparent=True, dpi=300)

# print((np.abs(charge_avg) + charge_std).max())
