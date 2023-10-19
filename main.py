import json
import pandas as pd
import matplotlib.pyplot as plt
import os


class Plotter:
    def __init__(self):
        self.plots_dir = 'plots'
        os.makedirs(self.plots_dir, exist_ok=True)

    def draw_plots(self, json_file):

        with open(json_file) as f:
            data = json.load(f)
        df = pd.DataFrame(data)


        plots = []
        for column in df.columns:
            if column not in ['gt_corners', 'rb_corners']:
                plt.figure(figsize=(10, 6))
                plt.plot(df['gt_corners'], label='Ground Truth')
                plt.plot(df['rb_corners'], label='Model Prediction')
                plt.plot(df[column], label=column)
                plt.legend()
                plt.xlabel('Room Index')
                plt.ylabel('Corner Count')
                plt.title(f'Comparison {column}')
                plot_path = os.path.join(self.plots_dir, f'{column}.png')
                plt.savefig(plot_path)
                plt.close()
                plots.append(plot_path)

        return plots


if __name__ == '__main__':
    plotter = Plotter()
    json_file = 'deviation.json'
    plots = plotter.draw_plots(json_file)
    print(f'Plots saved: {plots}')



# У меня не профессиональный пайчарм поэтому не доступно .ipynb ,но чтобы заработало в Notebook.ipynb
# там надо прописать этот код, но это не точно

# from main import Plotter
#
# plotter = Plotter()
# json_file = 'deviation.json'
# plots = plotter.draw_plots(json_file)
#
# for plot in plots:
#     display(Image(filename=plot))

# а в main.py должен быть такой код
# import json
# import pandas as pd
# import matplotlib.pyplot as plt
# import os
#
# class Plotter:
#     def __init__(self):
#         self.plots_dir = 'plots'
#         os.makedirs(self.plots_dir, exist_ok=True)
#
#     def draw_plots(self, json_file):
#         # Load JSON data into a pandas DataFrame
#         with open(json_file) as f:
#             data = json.load(f)
#         df = pd.DataFrame(data)
#
#         plots = []
#         for column in df.columns:
#             if column not in ['gt_corners', 'rb_corners']:
#                 plt.figure(figsize=(10, 6))
#                 plt.plot(df['gt_corners'], label='Ground Truth')
#                 plt.plot(df['rb_corners'], label='Model Prediction')
#                 plt.plot(df[column], label=column)
#                 plt.legend()
#                 plt.xlabel('Room Index')
#                 plt.ylabel('Corner Count')
#                 plt.title(f'Comparison {column}')
#                 plot_path = os.path.join(self.plots_dir, f'{column}.png')
#                 plt.savefig(plot_path)
#                 plt.close()
#                 plots.append(plot_path)
#
#         return plots
#
# plotter = Plotter()
# json_file = 'deviation.json'
# plots = plotter.draw_plots(json_file)
# print(f'Plots saved: {plots}')