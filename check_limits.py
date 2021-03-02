from bms import validate_bms_param_name
from bms import validate_bms_param_value
from bms import validate_overall_bms_health

if __name__ == '__main__':
    
    assert (validate_bms_param_name({'temperature': 40, 'soc': 40, 'charging_rate': 0.8, 'current': 5}) == 'ParamNameUnknown')
    assert (validate_bms_param_name({'temperature': 39, 'soc': 53, 'charging_rate': 0.8}) != 'ParamNameUnknown')
    assert (validate_bms_param_name({'temperature': 44, 'soc': 70, 'charging_rate': 0.75}) == 'OK')

    assert (validate_bms_param_value({'temperature': float('nan'), 'soc': 40, 'charging_rate': 0.8}) == 'NullValue')
    assert (validate_bms_param_value({'temperature': 40, 'soc': float('nan'), 'charging_rate': 0.8}) == 'NullValue')
    assert (validate_bms_param_value({'temperature': 40, 'soc': 40 , 'charging_rate': float('nan')}) == 'NullValue')
    assert (validate_bms_param_value({'temperature': 40, 'soc': 40, 'charging_rate': 0.6}) == 'OK')

    assert (len(validate_overall_bms_health({'temperature': 40, 'soc': 40, 'charging_rate': 0.6})) == 0)
    assert (len(validate_overall_bms_health({'temperature': 100, 'soc': 89, 'charging_rate': 0.8})) > 0)
    assert (len(validate_overall_bms_health({'temperature': -1, 'soc': 40, 'charging_rate': 0.8})) > 0)
    assert (len(validate_overall_bms_health({'temperature': -1, 'soc': 85, 'charging_rate': 1})) > 0)
