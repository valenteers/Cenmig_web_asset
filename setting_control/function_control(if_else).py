#!/usr/bin/env python3 


#==================================== Load my packages =================================#
import setting as config
import work_module 

#==================================== Load library =====================================#


#==================================== var setting ======================================#

def import_setting_control(setting_control,data_in,data_out=''):
    if setting_control == "1":
        data_out = step_by_step_follow_setting(config.setting_1,data_in)
        return data_out
    elif setting_control == "2":
        data_out = step_by_step_follow_setting(config.setting_2,data_in)
        return data_out
    elif setting_control == "3":
        data_out = step_by_step_follow_setting(config.setting_3,data_in)
        return data_out
    else:
        print("Don't have this setting")

def step_by_step_follow_setting(setting_import,data):
    while 0 < len(setting_import):
        data = choose_function_control(setting_import.pop(0),data)
    else:
        return data  

def choose_function_control(setting,data):
    if setting == "step1":
        x = work_module.step1(data)
        data = (x[1])
        print (x[0])
        return data
    elif setting == "step2":
        x = work_module.step2(data)
        data = (x[1])
        print (x[0])
        return data
    elif setting == "step3":
        x = work_module.step3(data)
        data = (x[1])
        print (x[0])
        return data
    else:
        print("Error no this function in setting")

if __name__ == "__main__":
    print('Plz choose your setting :') #instead of some setting you need
    setting = input()
    print('Plz choose your data_out :') #instead of some data_out need to work 
    data = input()
    print('Begin to work')
    data_after_work = import_setting_control(setting,data)
    print('Success all Step \(^-^)/')
    print('Success data : '+ data_after_work) #get black your data_out after wokr to save or something...

