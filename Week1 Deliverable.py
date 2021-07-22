import numpy as np
import matplotlib.pyplot as plt


def waveform(phone_num, duration=100, gap=50, sampling_rate=8000, amplitude=1, graphic=False):
    '''Returns numpy array for the values of the corresponding waveform.
    There's also a 'graphic' option to include a graph.'''
    dtmf_table = {
        "1": [1209, 697],
        "2": [1336, 697],
        "3": [1477, 697],
        "A": [1633, 697],
        "4": [1209, 770],
        "5": [1336, 770],
        "6": [1477, 770],
        "B": [1633, 770],
        "7": [1209, 852],
        "8": [1336, 852],
        "9": [1477, 852],
        "C": [1633, 852],
        "*": [1209, 941],
        "0": [1336, 941],
        "#": [1477, 941],
        "D": [1633, 941],
    }
    phone_num = phone_num.upper()
    for digit in phone_num:
        if digit not in dtmf_table:
            raise ValueError('The only allowed digits are 0-9, A-D, #, and *')

    gap_amount_of_samples = gap * sampling_rate // 1000
    gap_values = np.zeros(gap_amount_of_samples)

    first = True
    ans = np.array([])
    amount_of_samples = (duration/1000)*sampling_rate
    samples = np.arange(0, duration/1000, (duration/1000)/amount_of_samples)
    for digit in phone_num:
        if not first:
            ans = np.append(ans, gap_values)
        else:
            first = False
        values = (amplitude/2) * (
                np.sin(samples * 2 * np.pi * dtmf_table[digit][0]) +
                np.sin(samples * 2 * np.pi * dtmf_table[digit][1])
        )
        ans = np.append(ans, values)
    # plotting
    if graphic:
        plt.title("Line graph")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.plot(np.arange(0, (len(phone_num)-1)*gap_amount_of_samples+len(phone_num)*amount_of_samples), ans, color="green")
        plt.show()
    return ans


if __name__ == '__main__':
    waveform('A', graphic=True)