import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import jinja2


class Sheet:
    def __init__(self, sheet):
        self.chamber_temperature = sheet[:, 0]
        self.adc1 = sheet[:, 7]
        self.die1 = sheet[:, 8]
        self.meter1 = sheet[:, 9]

        # self.meter = np.sort(np.append(self.meter0, self.meter1))
        # self.die = np.sort(np.append(self.die0, self.die1))
        # self.adc = np.sort(np.append(self.adc0, self.adc1))

        self.meter = self.meter1
        self.adc = self.adc1
        self.die = self.die1

        self.param_meter = np.polyfit(self.meter, self.adc, 1)
        self.param_meter = np.array([round(self.param_meter[0], 2), round(self.param_meter[1], 2)])
        self.func = np.poly1d(self.param_meter)
        self.poly_fitting_meter = self.func(self.meter)
        param_lower_bound = np.array([self.param_meter[0], self.param_meter[1] - 3 * self.param_meter[0]])
        func = np.poly1d(param_lower_bound)
        self.poly_lower_bound_meter = func(self.meter)
        param_upper_bound = np.array([self.param_meter[0], self.param_meter[1] + 3 * self.param_meter[0]])
        func = np.poly1d(param_upper_bound)
        self.poly_upper_bound_meter = func(self.meter)


def get_error(params, dies, adcs) -> int:
    error = 0
    for die, adc in zip(dies, adcs):
        fitting_die = (-params[1] + math.sqrt(math.pow(params[1], 2) - 4 * params[0] * (params[2] - adc)))/(2 * params[0])
        error = max(abs(fitting_die - die), error)
    error = round(error, 2)

    return error


def get_linear_max_error(params, dies, adcs) -> int:
    error = 0
    for die, adc in zip(dies, adcs):
        fitting_die = (adc - params[1])/params[0]
        error = max(abs(fitting_die - die), error)
    error = round(error, 2)

    return error


def generate_look_up_table(lower_bound:  int, upper_bound: int, fitting_func):
    look_up_table = list()
    for t in np.arange(lower_bound, upper_bound, 0.5):      # step set as 0.5 degree
        look_up_table.append(int(fitting_func(t)))
    j2_loader = jinja2.FileSystemLoader('./')
    env = jinja2.Environment(loader=j2_loader)
    j2_template = env.get_template('./adc_lookup_table.jinja')
    result = j2_template.render(upper_bound=upper_bound-0.5, lower_bound=lower_bound, adc_lookup_table_size=len(look_up_table))

    with open('adc_lookup_table.h', 'w') as fp:
        fp.write(result)
        fp.write(f'uint16_t adc_lookup_table[{len(look_up_table)}]=' + '{')
        for i, val in enumerate(look_up_table):
            if i % 10 == 0:
                fp.write('\n\t')
            fp.write(f'{val}, ')
        fp.write('\n};\n')


template = 'Temperature_Test.xlsx'
df_raw = pd.read_excel(template, engine='openpyxl', sheet_name=None)

sheet_name = 'amp2_new'
sheet = df_raw.get(sheet_name).values
sheet = np.delete(sheet, 0, axis=0)  # remove nan row
amp_2 = Sheet(sheet)



# plt.figure(1)
# plt.scatter(volex_1_5.meter0, volex_1_5.adc0, color='b', linestyle='dotted', label='adc0 (volex 1.5m)')
# plt.scatter(volex_1_5.meter1, volex_1_5.adc1, color='r', linestyle='dotted', label='adc1 (volex 1.5m)')
# plt.plot(volex_1_5.meter, volex_1_5.poly_fitting_meter, color='g', linestyle='solid', alpha=0.3, label=f'y={volex_1_5.param_meter[0]}$x^2$+{volex_1_5.param_meter[1]}x+{volex_1_5.param_meter[2]}')
# plt.fill_between(volex_1_5.meter, volex_1_5.poly_lower_bound_meter, volex_1_5.poly_upper_bound_meter, color='g', linestyle='solid', label='$+-3^oC$ error range(poly 2d fit)', alpha=0.1)
# plt.title('volex_1_5m_adc_meter')
# plt.legend()
# plt.ylabel('adc')
# plt.xlabel('meter temperature/$^oC$')
# plt.savefig('volex_1_5m_adc_meter')
#
# plt.figure(2)
# plt.scatter(volex_1_5.die0, volex_1_5.adc0, color='b', linestyle='dotted', label='adc0 (volex 1.5m)')
# plt.scatter(volex_1_5.die1, volex_1_5.adc1, color='r', linestyle='dotted', label='adc1 (volex 1.5m)')
# plt.plot(volex_1_5.die, volex_1_5.poly_fitting_die, color='g', linestyle='solid', alpha=0.3, label=f'y={volex_1_5.param_die[0]}$x^2$+{volex_1_5.param_die[1]}x+{volex_1_5.param_die[2]}')
# plt.fill_between(volex_1_5.die, volex_1_5.poly_lower_bound_die, volex_1_5.poly_upper_bound_die, color='g', linestyle='solid', label='$+-3^oC$ error range(poly 2d fit)', alpha=0.1)
# plt.title('volex_1_5m_adc_die')
# plt.legend()
# plt.ylabel('adc')
# plt.xlabel('die temperature/$^oC$')
# plt.savefig('volex_1_5m_adc_die')
#
# plt.figure(3)
# plt.scatter(volex_1_5.meter0, volex_1_5.adc0, color='b', linestyle='dotted', label='meter0 (volex 1.5m)')
# plt.scatter(volex_1_5.meter1, volex_1_5.adc1, color='r', linestyle='dotted', label='meter1 (volex 1.5m)')
# plt.scatter(volex_1_5.die0, volex_1_5.adc0, color='g', linestyle='dotted', label='die0 (volex 1.5m)')
# plt.scatter(volex_1_5.die1, volex_1_5.adc1, color='y', linestyle='dotted', label='die1 (volex 1.5m)')
# plt.title('volex_1_5m_adc_meter_die')
# plt.legend()
# plt.ylabel('adc')
# plt.xlabel('temperature/$^oC$')
# plt.savefig('volex_1_5m_adc_meter_die')
#
plt.figure(4)
error = get_linear_max_error(amp_2.param_meter, amp_2.meter, amp_2.adc)
#plt.scatter(amp_2.meter0, amp_2.adc0, color='b', linestyle='dotted', label='adc0 (amphenol 2m)')
plt.scatter(amp_2.meter1, amp_2.adc1, color='r', linestyle='dotted', label='adc1 (amphenol 2m)')
plt.plot(amp_2.meter, amp_2.poly_fitting_meter, color='g', linestyle='solid', alpha=0.3, label=f'y={amp_2.param_meter[0]}$x$+{amp_2.param_meter[1]}, max error={error}$^oC$')
plt.fill_between(amp_2.meter, amp_2.poly_lower_bound_meter, amp_2.poly_upper_bound_meter, color='g', linestyle='solid', label='$+-3^oC$ error range(poly 2d fit)', alpha=0.1)
plt.title('amphenol_2m_adc_meter')
plt.legend()
plt.ylabel('adc')
plt.xlabel('meter temperature/$^oC$')
plt.savefig('amphenol_2m_adc_meter')
#
# plt.figure(5)
# plt.scatter(amp_2.die0, amp_2.adc0, color='b', linestyle='dotted', label='adc0 (amphenol 2m)')
# plt.scatter(amp_2.die1, amp_2.adc1, color='r', linestyle='dotted', label='adc1 (amphenol 2m)')
# plt.plot(amp_2.die, amp_2.poly_fitting_die, color='g', linestyle='solid', alpha=0.3, label=f'y={amp_2.param_die[0]}$x^2$+{amp_2.param_die[1]}x+{amp_2.param_die[2]}')
# plt.fill_between(amp_2.die, amp_2.poly_lower_bound_die, amp_2.poly_upper_bound_die, color='g', linestyle='solid', label='$+-3^oC$ error range(poly 2d fit)', alpha=0.1)
# plt.title('amphenol_2m_adc_die')
# plt.legend()
# plt.ylabel('adc')
# plt.xlabel('die temperature/$^oC$')
# plt.savefig('amphenol_2m_adc_die')
#
# plt.figure(6)
# plt.scatter(amp_2.meter, amp_2.adc, color='b', linestyle='dotted', label='meter0 (amphenol 2m)')
# plt.scatter(amp_2.die, amp_2.adc, color='g', linestyle='dotted', label='die0 (amphenol 2m)')
# plt.title('amphenol_2m_adc_meter_die')
# plt.legend()
# plt.ylabel('adc')
# plt.xlabel('temperature/$^oC$')
# plt.savefig('amphenol_2m_adc_meter_die')


# plt.figure(7)
# plt.scatter(volex_1_5.die0, volex_1_5.adc0, color='b', linestyle='dotted', label='adc0 (volex 1.5m)')
# plt.scatter(volex_1_5.die1, volex_1_5.adc1, color='r', linestyle='dotted', label='adc1 (volex 1.5m)')
# plt.scatter(amp_2.die0, amp_2.adc0, color='m', linestyle='dotted', label='adc0 (amphenol 2m)')
# plt.scatter(amp_2.die1, amp_2.adc1, color='c', linestyle='dotted', label='adc1 (amphenol 2m)')
# plt.scatter(volex_2_5.die0, volex_2_5.adc0, color='y', linestyle='dotted', label='adc0 (volex 2.5m)')
# plt.scatter(volex_2_5.die1, volex_2_5.adc1, color='g', linestyle='dotted', label='adc1 (volex 2.5m)')
# plt.title('mix_adc_die')
# plt.legend()
# plt.ylabel('adc')
# plt.xlabel('die temperature/$^oC$')
# plt.savefig('mix_adc_die')

# plt.figure(8)
# plt.scatter(volex_2_5.die0, volex_2_5.adc0, color='b', linestyle='dotted', label='adc0 (volex 2.5m)')
# plt.scatter(volex_2_5.die1, volex_2_5.adc1, color='r', linestyle='dotted', label='adc1 (volex 2.5m)')
# plt.plot(volex_2_5.die, volex_2_5.poly_fitting_die, color='g', linestyle='solid', alpha=0.3, label=f'y={volex_2_5.param_die[0]}$x^2$+{volex_2_5.param_die[1]}x+{volex_2_5.param_die[2]}')
# plt.fill_between(volex_2_5.die, volex_2_5.poly_lower_bound_die, volex_2_5.poly_upper_bound_die, color='g', linestyle='solid', label='$+-3^oC$ error range(poly 2d fit)', alpha=0.1)
# plt.title('volex_2_5m_adc_die')
# plt.legend()
# plt.ylabel('adc')
# plt.xlabel('die temperature/$^oC$')
# plt.savefig('volex_2_5m_adc_die')

# # plt.figure(9)
# # plt.scatter(volex_1_5.die0, volex_1_5.adc0, color='b', linestyle='dotted', label='adc0 (volex 1.5m)')
# # plt.scatter(volex_1_5.die1, volex_1_5.adc1, color='r', linestyle='dotted', label='adc1 (volex 1.5m)')
# # plt.scatter(volex_2_5.die0, volex_2_5.adc0, color='y', linestyle='dotted', label='adc0 (volex 2.5m)')
# # plt.scatter(volex_2_5.die1, volex_2_5.adc1, color='g', linestyle='dotted', label='adc1 (volex 2.5m)')
# die = np.sort(np.append(volex_1_5.die, volex_2_5.die))
# adc = np.sort(np.append(volex_1_5.adc, volex_2_5.adc))
# param_die = np.polyfit(die, adc, 2)
# param_die = np.array([round(param_die[0], 2), round(param_die[1], 2), round(param_die[2], 2)])
# fitting_func = np.poly1d(param_die)
# poly_fitting_die = fitting_func(die)
# param_lower_bound = np.array([param_die[0], 6 * param_die[0] + param_die[1], 9 * param_die[0] + 3 * param_die[1] + param_die[2]])
# func = np.poly1d(param_lower_bound)
# poly_lower_bound_die = func(die)
# param_upper_bound = np.array([param_die[0], param_die[1] - 6 * param_die[0], 9 * param_die[0] - 3 * param_die[1] + param_die[2]])
# func = np.poly1d(param_upper_bound)
# poly_upper_bound_die = func(die)
# error = get_error(param_die, die, adc)
# # plt.plot(die, poly_fitting_die, color='g', linestyle='solid', alpha=0.3, label=f'y={param_die[0]}$x^2$+{param_die[1]}x+{param_die[2]}, max error={error}$^oC$')
# # plt.fill_between(die, poly_lower_bound_die, poly_upper_bound_die, color='g', linestyle='solid', label='$+-3^oC$ error range(poly 2d fit)', alpha=0.1)
# # plt.title('volex_adc_die')
# # plt.legend()
# # plt.ylabel('adc')
# # plt.xlabel('die temperature/$^oC$')
# # plt.savefig('volex_adc_die')
#

fitting_func = np.poly1d(amp_2.param_meter)
generate_look_up_table(6, 140, fitting_func)





