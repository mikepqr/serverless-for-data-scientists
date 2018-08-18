# From https://github.com/ucbrise/risecamp/tree/risecamp2017/pywren

def plot_pywren_execution(futures):
    import warnings
    warnings.filterwarnings("ignore")
    from IPython import get_ipython
    get_ipython().run_line_magic('pylab', 'inline')
    import pylab
    import seaborn as sns
    import pandas as pd
    sns.set_style('whitegrid')
    sns.set_context("poster")
    import os
    import matplotlib.patches as mpatches
    import numpy as np

    def collect_execution_info(futures):
        results = [f.result() for f in futures]
        run_statuses = [f.run_status for f in futures]
        invoke_statuses = [f.invoke_status for f in futures]
        return {'results' : results,'run_statuses' : run_statuses, 'invoke_statuses' : invoke_statuses}

    info = collect_execution_info(futures)

        # visualization
    def visualize_execution(info):
        # preparing data
        run_df = pd.DataFrame(info['run_statuses'])
        invoke_df = pd.DataFrame(info['invoke_statuses'])
        info_df = pd.concat([run_df, invoke_df], axis=1)
        
        def remove_duplicate_columns(df):
            Cols = list(df.columns)
            for i,item in enumerate(df.columns):
                if item in df.columns[:i]: Cols[i] = "toDROP"
            df.columns = Cols
            return df.drop("toDROP",1)

        info_df = remove_duplicate_columns(info_df)
        
        total_tasks = len(info_df)
        y = np.arange(total_tasks)
            
        time_offset = np.min(info_df.host_submit_time)
        fields = [('host submit', info_df.host_submit_time - time_offset), 
                  ('task start', info_df.start_time - time_offset ), 
                  ('setup done', info_df.start_time + info_df.setup_time - time_offset), 
                  ('task done', info_df.end_time - time_offset), 
                  ('results returned', info_df.download_output_timestamp - time_offset)
                 ]

        # create plotting env
        fig = pylab.figure(figsize=(16, 8))
        ax = fig.add_subplot(1, 1, 1)

        # plotting
        patches = []
        palette = sns.color_palette("deep", 6)
        point_size = 100
        for f_i, (field_name, val) in enumerate(fields):
            ax.scatter(val, y, c=palette[f_i], edgecolor='none', s=point_size, alpha=1)
            patches.append(mpatches.Patch(color=palette[f_i], label=field_name))
        ax.set_xlabel('wallclock time (sec)')
        ax.set_ylabel('task')
        
        # legend
        legend = pylab.legend(handles=patches, 
                              loc='upper left', frameon=True)
        legend.get_frame().set_facecolor('#FFFFFF')

        # y ticks
        plot_step = 5
        y_ticks = np.arange(total_tasks//plot_step + 2) * plot_step
        ax.set_yticks(y_ticks)
        for y in y_ticks:
            ax.axhline(y, c='k', alpha=0.1, linewidth=1)
        
        # formatting
        ax.grid(False)
        fig.tight_layout()

    visualize_execution(info)
