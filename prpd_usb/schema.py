from collections import namedtuple

Command = namedtuple("Command", ["name", "command", "fields"])
Field = namedtuple("Field", ["type", "name", "unit", "factor"])

FieldResult = namedtuple("FieldResult", ["command", "field", "time", "value"])

SCHEMA = [
    # Command("solar", "5a0071050000dc07a5", [
    #     Field('I', "total_phase_1", "Wh", 1),
    #     Field('I', "total_phase_2", "Wh", 1),
    #     Field('I', "total_phase_3", "Wh", 1),
    # ]),
    Command("solar", "5a00710200001db6a5", [
        Field('I', "W_total_phase_1?", "Wh", 1),
        Field('I', "W_total_phase_2?", "Wh", 1),
        Field('I', "W_total_phase_3?", "Wh", 1),
    ]),
    Command("solar", "5a0071000000dd17a5", [
        Field('I', "W_toal_backup?", "Wh", 1),
        Field('I', "W_total?", "Wh", 1),
        Field('I', "W_?", "Wh", 1),
    ]),   
    Command("dunno", "5a00700000002116a5", [
        Field('h', 'U?', "V", 0.1),
        Field('h', 'U_1?', "W", 0.1),
        Field('h', '?', "W", 1),
        Field('H', '?', "W", 1),
        Field('H', '?', "W", 0.1),
        Field('h', '?', "W", 0.01),
        Field('H', 'temp?', "°C", 0.1),
        Field('h', '?', "W", 0.01),
    ]), 
    Command("grid", "5a00710400001c56a5", [
        Field('I', "W_total_phase_1", "Wh", 1),
        Field('I', "W_total_phase_2", "Wh", 1),
        Field('I', "W_total_phase_3", "Wh", 1),
    ]),
    Command("platform", "5a0071030000dde7a5", [
        Field('I', 'W_consumed', "Wh", 1),
        Field('I', 'W_produced', "Wh", 1),
    ]),
    # Command("solar", "5a00700500002006a5", [
    #     Field('H', 'status', "", 1),
    #     Field('h', 'w_phase_1', "W", 1),
    #     Field('h', 'w_phase_2', "W", 1),
    #     Field('h', 'w_phase_3', "W", 1),
    #     Field('H', 'va_phase_1', "VA", 1),
    #     Field('H', 'va_phase_2', "VA", 1),
    #     Field('H', 'va_phase_3', "VA", 1),
    # ]),
    Command("solar", "5a0070020000e1b7a5", [
        Field('H', 'U_string_1', "V", 0.01),
        Field('I', 'I_string_1', "A", 0.01),
        Field('H', 'u_string_2', "V", 0.01),
        Field('I', 'I_string_2', "A", 0.01),
        Field('h', 'status?', "X", 1),
        Field('H', 'P_total', "W", 1),
        Field('h', 'temp_string_1', "°C", 0.1),
        Field('h', 'temp_string_2', "°C", 0.1),
        Field('H', 'P_string_2?', "W", 0.1),
    ]),
    Command("battery", "5a0070010000e147a5", [
        Field('H', 'U', "V", 0.01),
        Field('i', 'I', "A", 0.01),
        Field('I', '?', '?', 0.01),
        Field('H', '?', '?', 0.01),
        Field('h', 'P', "W", 1),
        Field('B', 'SoC', "%", 1),
        Field('h', 'temp1', "°C", 0.1),
        Field('h', 'temp2', "°C", 0.1),
        Field('H', '?', '?', 1),
    ]),
    Command("battery", "5a00710100001d46a5", [
        Field('I', 'W_consumed', "Wh", 1),
        Field('I', 'W_produced', "Wh", 1),
    ]),
    Command("grid", "5a0070040000e057a5", [
        Field('H', None, None, None),
        Field('h', 'I_phase_1', "A", 0.1),
        Field('h', 'I_phase_2', "A", 0.1),
        Field('h', 'I_phase_3', "A", 0.1),

        Field('H', 'U_phase_1', "V", 0.1),
        Field('H', 'U_phase_2', "V", 0.1),
        Field('H', 'U_phase_3', "V", 0.1),

        Field('h', 'P_DC_phase_1', "W", 1),
        Field('h', 'P_DC_phase_2', "W", 1),
        Field('h', 'P_DC_phase_3', "W", 1),

        Field('H', 'P_AC_phase_1', "VA", 1),
        Field('H', 'P_AC_phase_2', "VA", 1),
        Field('H', 'P_AC_phase_3', "VA", 1),
    ]),
    Command("platform", "5a007003000021e6a5", [
        Field('H', 'f', "Hz", 0.01),
        Field('H', 'U', "V", 0.1),
        Field('h', 'temp', "°C", 0.1),
        Field('H', 'status', "", 1),
        Field('h', 'P', "W", 1),
    ]),
]

NETWORK = [
    Command("mac_address", "5a0031040000dc43a5", [
        Field('bbbbbb', 'mac_address', None, None),
    ]),
    Command("network", "5a00230000006507a5", [
        Field('B', None, None, None),
        Field('I', None, None, None),
        Field('h', None, None, None),
        Field('I', 'ip_address', "", 1),
        Field('I', 'dns1', "", 1),
        Field('I', 'dns2', "", 1),
        Field('I', 'gateway', "", 1),
    ]),
]
