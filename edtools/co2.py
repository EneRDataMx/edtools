import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import numpy as np
from dateutil.parser import parse
# colores
# azulier     = "#1A3D6F"
# doradoier  = '#C65C25'
#  @file     enerdata.mplstyle
#  @author   Guillermo Barrios <gbv@ier.unam.mx>
#
#  This mpl style is intended to be used in for the dataviz project at IER-UNAM

# figure.figsize 		: 12.00, 6.00
#
# axes.spines.bottom  : True
# axes.spines.left    : False
# axes.spines.right   : False
# axes.spines.top     : False
# axes.prop_cycle		: cycler('color', [ 'grey', 'grey', 'grey', 'grey', 'grey'])
# axes.labelcolor		: grey
# axes.labelsize		: 26   # fontsize of the axes title
# axes.grid           : True   # display grid or not
# axes.grid.which     : major
# axes.grid.axis      : y
#
# grid.linestyle   :   :       # dotted
#
#
# xtick.labelsize		: 22 # fontsize of the tick labels
# ytick.labelsize		: 22 # fontsize of the tick labels
# legend.fontsize		: 22
#
#
# lines.linewidth		: 8
# lines.markersize	: 14            # markersize, in points
#
# font.size		: 20
# #font.family		: sans-serif
# #font.serif		: Tahoma
#
# xtick.color		: grey
# ytick.color		: grey
# text.color		: grey

# savefig.transparent : True    # setting that controls whether figures are saved with a
def load_co2():
    f = 'https://raw.githubusercontent.com/EneRDataMx/edtools/main/data/co2_mlo_surface-insitu_1_ccgg_DailyData.txt'
    df = pd.read_csv(f,skiprows=150,delimiter=' ',parse_dates={'date':[1,2,3,4,5,6]})
    df.date = pd.to_datetime(df.date,format="%Y %m %d %H %M %S")
    df.set_index('date',inplace=True)
    df.columns
    df = df[df.value>0]
    df = df.resample('D').interpolate(method='time')
    return df['value']


def co2_when_born(nombre,anio,mes,dia):
    df = load_co2()

    fecha  =  date(anio,mes,dia)

    inicio = df.index[0].date()
    final  = df.index[-1].date()
    with plt.style.context('../enerdata_rectangle.mplstyle'):


        dates = [inicio,final]
        labels = ['','']

        labels.insert(1,nombre)
        dates.insert(1,fecha)
#         try:
        values = [df.value.loc[ date.strftime("%Y-%m-%d")] for date in dates ]
        labels = ['{0:%d %b %Y}:\n{1} {2} ppm CO2'.format(d, l,v) for l, d, v in zip (labels, dates,values)]


        min_date = date(np.min(dates).year - 2, np.min(dates).month, np.min(dates).day)
        max_date = date(np.max(dates).year + 2, np.max(dates).month, np.max(dates).day)


        timeline = 300
        fig, ax = plt.subplots()


        ax.plot(df.value,lw=1,c=doradoier)
        ax.set_ylabel("ppm CO2")

        ax.set_xlim(min_date, max_date)
    #     ax.axhline(timeline, xmin=0.05, xmax=0.95, c='deeppink', zorder=2)
        ax.axhline(timeline, xmin=0.05, xmax=0.95, c=doradoier, zorder=2,lw=3)
        ax.scatter(dates, np.full(len(dates),300), s=120, c='palevioletred', zorder=2)
        ax.scatter(dates, np.full(len(dates),300), s=30, c='darkmagenta', zorder=3 )



        label_offsets = np.zeros(len(dates))
        label_offsets[::2] = timeline - 15
        label_offsets[1::2] = timeline + 5
        ax.grid()

        for i, (l, d) in enumerate(zip(labels, dates)):

            ax.text(d, label_offsets[i], l, ha='left', color=doradoier,fontsize=12)


        for spine in ["left", "top", "right", "bottom"]:
            ax.spines[spine].set_visible(False)

        ax.set_xticks([])
