import matplotlib.pyplot as plt

import rosbag_pandas as rpd

def plot_pid_performance(file):
    df = rpd.bag_to_dataframe(file)
    ax1 = plt.subplot(2, 1, 1)
    ax1.plot(df.index, df.current_velocity__twist_linear_x, '-o', df.index, df.twist_cmd__twist_linear_x, '-o')
    plt.ylabel('Vehicle Speed (m/s)')
    plt.legend(['Actual','Demand'])
    ax2 = plt.subplot(2, 1, 2, sharex=ax1)
    ax2.plot(df.index, df.vehicle_throttle_cmd__pedal_cmd, '-o')
    plt.ylabel('Throttle (%)')
    plt.show()

if __name__ == "__main__":
    import sys
    import os
    file = os.path.join(os.getcwd(), sys.argv[1])
    plot_pid_performance(file)