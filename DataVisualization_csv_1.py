import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter
from bokeh.layouts import column

df = pd.read_csv("./RTT_4G_Does_CA.csv")
# print(df.columns)

########## RD
# is_rd = df['RRC Category*'] == 'RD'
# rd = df[['Procedure End Time*','RRC Category*']][is_rd]
rd = df[['Procedure End Time*','RRC Category*']].dropna(how='any')
rd['Procedure End Time*'] = pd.to_datetime(rd['Procedure End Time*'], format = '%H:%M:%S')
RRC_CATEGORY = ["RRC Excl", "Good", "RSF", "RD"]

########## RSRP
cmrRsrp = df[['Procedure End Time*','First  CMR RSRP Serving (dBm)']].dropna(how='any')
cmrRsrp['Procedure End Time*'] = pd.to_datetime(cmrRsrp['Procedure End Time*'], format = '%H:%M:%S')

########### Band
band = df[['Procedure End Time*','Rollup Band #*']].dropna(how='any')
band['Procedure End Time*'] = pd.to_datetime(rd['Procedure End Time*'], format = '%H:%M:%S')

########### UL Avg SINR (dB)
ulSinr = df[['Procedure End Time*','UL Avg SINR (dB)']].dropna(how='any')
ulSinr['Procedure End Time*'] = pd.to_datetime(rd['Procedure End Time*'], format = '%H:%M:%S')

output_file("fig3.html")
fig1 = figure(title = 'RRC Category', plot_width=1000, plot_height=200,y_range=RRC_CATEGORY,x_axis_type="datetime")
fig2 = figure(title = 'CMR RSRP Serving (dBm)', plot_width=1000, plot_height=200,x_axis_type="datetime")
fig3 = figure(title = 'Rollup Band', plot_width=1000, plot_height=200,x_axis_type="datetime")
fig4 = figure(title = 'UL Avg SINR (dB)', plot_width=1000, plot_height=200,x_axis_type="datetime")

#Change x axis type to timestamps
fig1.xaxis.formatter=DatetimeTickFormatter(
    days=["%H:%M:%S"],
    months=["%H:%M:%S"],
    hours=["%H:%M:%S"],
    minutes=["%H:%M:%S"]
)
fig2.xaxis.formatter=DatetimeTickFormatter(
    days=["%H:%M:%S"],
    months=["%H:%M:%S"],
    hours=["%H:%M:%S"],
    minutes=["%H:%M:%S"]
)
fig3.xaxis.formatter=DatetimeTickFormatter(
    days=["%H:%M:%S"],
    months=["%H:%M:%S"],
    hours=["%H:%M:%S"],
    minutes=["%H:%M:%S"]
)
fig4.xaxis.formatter=DatetimeTickFormatter(
    days=["%H:%M:%S"],
    months=["%H:%M:%S"],
    hours=["%H:%M:%S"],
    minutes=["%H:%M:%S"]
)
fig1.circle(rd['Procedure End Time*'],rd['RRC Category*'],color='red', line_width=2)
# fig1.step(rd['Procedure End Time*'],rd['RRC Category*'],color='red', line_width=2)
fig2.line(cmrRsrp['Procedure End Time*'],cmrRsrp['First  CMR RSRP Serving (dBm)'], line_width=2)
fig3.step(band['Procedure End Time*'],band['Rollup Band #*'],color='blue', line_width=2)
fig4.line(ulSinr['Procedure End Time*'],ulSinr['UL Avg SINR (dB)'],color='purple', line_width=2)
show(column(fig1, fig2, fig3, fig4))


