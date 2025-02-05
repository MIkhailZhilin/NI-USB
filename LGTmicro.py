from typing import Tuple
import numpy as np
import numpy.typing
import nidaqmx
from scipy import signal
from nidaqmx.constants import AcquisitionType


def generate_sine_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: float,
    number_of_samples: int,
    phase_in: float = 0.0,
) -> Tuple[numpy.typing.NDArray[np.double], float]:

    duration_time = number_of_samples / sampling_rate
    duration_radians = duration_time * 2 * np.pi
    phase_out = (phase_in + duration_radians) % (2 * np.pi)
    t = np.linspace(0, duration_time, number_of_samples, endpoint=False)
    return amplitude * abs(np.sin(2 * np.pi * frequency * t + phase_in)), phase_out


def generate_triangle_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: float,
    number_of_samples: int,
) -> np.ndarray:

    t = np.linspace(0, 1 / frequency, int(sampling_rate / frequency), endpoint=False)
    triangle_wave = 2 * amplitude * np.abs(2 * (t * frequency - np.floor(t * frequency + 0.5)))
    return np.tile(triangle_wave, number_of_samples // len(triangle_wave))
def generic_pulse(   frequency: float,
    amplitude: float,
    sampling_rate: float,
    number_of_samples: int,):
    t = np.linspace(0, 1 / frequency, int(sampling_rate / frequency), endpoint=False)
    pulse= 2.2 + 1.65 * signal.square((2 * np.pi * frequency*t), duty=0.01)
    return pulse, 0
#
# def main():
#
#     with nidaqmx.Task() as task:
#         # Настраиваем каналы аналогового вывода
#         task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
#         task.ao_channels.add_ao_voltage_chan("Dev1/ao1")
#
#         # Настраиваем временные параметры
#         sampling_rate = 1000.0
#         number_of_samples = 1000
#         task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)
#
#         # Генерируем данные для двух сигналов
#         sine_wave, _ = generate_sine_wave(
#             frequency=10.0,
#             amplitude=1.0,
#             sampling_rate=sampling_rate,
#             number_of_samples=number_of_samples,
#         )
#         triangle_wave = generate_triangle_wave(
#             frequency=10.0,
#             amplitude=1.0,
#             sampling_rate=sampling_rate,
#             number_of_samples=number_of_samples,
#         )
#
#
#         data = np.vstack((sine_wave, triangle_wave))
#
#         # Записываем данные в задачу
#         task.write(data, auto_start=False)
#         task.start()
#
#         input("Generating voltage continuously. Press Enter to stop.\n")
#
#         task.stop()




with nidaqmx.Task() as task:


    task.ao_channels.add_ao_voltage_chan("Dev1/ao1")
    sampling_rate = 1000.0
    number_of_samples = 1000
    task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)

    # Генерируем данные для двух сигналов
    # sine_wave, _ = generate_sine_wave(
    #     frequency=10.0,
    #     amplitude=1.0,
    #     sampling_rate=sampling_rate,
    #     number_of_samples=number_of_samples,
    # )
    pulse , _ =generic_pulse(
        frequency=100.0,
        amplitude=1.0,
        sampling_rate=sampling_rate,
        number_of_samples=number_of_samples,
    )
    task.write(pulse, auto_start=False)
    task.start()
    input("Generating voltage continuously. Press Enter to stop.\n")
    task.stop()

