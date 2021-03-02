from math import isnan
from bmsConstants import bms_param_thresholds 

def get_param_min_limit(param_name):
    return bms_param_thresholds[param_name]['min']

def get_param_max_limit(param_name):
    return bms_param_thresholds[param_name]['max']


def validate_bms_param_name(bms_parameter):
    for param_name in bms_parameter.keys():
        if param_name not in bms_param_thresholds:
            return 'ParamNameUnknown'
    return 'OK'

def validate_bms_param_value(bms_parameter):
    for param_value in bms_parameter.values():
        if isnan(param_value):
            return 'NullValue'    
    return 'OK'

def validate_bms_limits(anomaly, bms_param_name, bms_param_value):
    if bms_param_value < get_param_min_limit(bms_param_name):
        anomaly.append([bms_param_name, 'UnderLimit'])
    elif bms_param_value > get_param_max_limit(bms_param_name):
        anomaly.append([bms_param_name, 'ExceedLimit'])


def validate_overall_bms_health(status_report):
    bms_error_report = []
    for bms_param_name in status_report:
        validate_bms_limits(bms_error_report, bms_param_name, status_report[bms_param_name])
        
    bms_log_report(bms_error_report)
    return bms_error_report

def bms_log_report(bms_error_report):
    if len(bms_error_report) == 0:
        print('All Parameters are OK')
    else:
        print('ALERT: BMS ran into issue ')
        print('------------------------------------')
        for parameter in bms_error_report:
            print('{} -> {}'.format(parameter[0],parameter[1]))
