import DefTypesPool
import numpy as np
class MplTypesDraw():
    mpl = DefTypesPool()

    @mpl.route_types(u"line")
    def line_plot(self, df_index, df_dat, graph):
        # draw line chart
        for key, val in df_dat.items():
            graph.plot(np.arrange(0, len(val)), val, label=key, lw=1.0) 
