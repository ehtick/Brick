from .namespaces import TAG, BRICK, OWL, QUDTQK

status_definitions = {
    "Status": {
        "tags": [TAG.Point, TAG.Status],
        "subclasses": {
            "Pump_Status": {
                "tags": [TAG.Point, TAG.Status, TAG.Pump],
            },
            "Thermostat_Status": {
                "tags": [TAG.Point, TAG.Status, TAG.Thermostat],
            },
            "Switch_Status": {
                "tags": [TAG.Point, TAG.Status, TAG.Switch],
            },
            "Tint_Status": {"tags": [TAG.Tint, TAG.Status, TAG.Point]},
            "Damper_Position_Status": {
                "tags": [TAG.Point, TAG.Damper, TAG.Position, TAG.Status],
                BRICK.hasQuantity: BRICK.Position,
            },
            "Direction_Status": {
                BRICK.hasQuantity: BRICK.Direction,
                "subclasses": {
                    "Motor_Direction_Status": {
                        "tags": [TAG.Point, TAG.Motor, TAG.Direction, TAG.Status],
                    },
                },
                "tags": [TAG.Point, TAG.Direction, TAG.Status],
            },
            "Disable_Status": {"tags": [TAG.Point, TAG.Disable, TAG.Status]},
            "Drive_Ready_Status": {
                "tags": [TAG.Point, TAG.Drive, TAG.Ready, TAG.Status],
            },
            "Emergency_Generator_Status": {
                "tags": [TAG.Point, TAG.Emergency, TAG.Generator, TAG.Status],
            },
            "Emergency_Push_Button_Status": {
                "tags": [TAG.Point, TAG.Emergency, TAG.Push, TAG.Button, TAG.Status],
            },
            "Enable_Status": {
                "subclasses": {
                    "Heat_Exchanger_System_Enable_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Heat,
                            TAG.Exchanger,
                            TAG.System,
                            TAG.Enable,
                            TAG.Status,
                        ],
                        "parents": [BRICK.System_Status],
                    },
                },
                "tags": [TAG.Point, TAG.Enable, TAG.Status],
            },
            "Even_Month_Status": {
                "tags": [TAG.Point, TAG.Even, TAG.Month, TAG.Status],
            },
            "Fan_Status": {"tags": [TAG.Point, TAG.Fan, TAG.Status]},
            "Valve_Status": {"tags": [TAG.Point, TAG.Valve, TAG.Status]},
            "Fault_Status": {
                "subclasses": {
                    "Humidifier_Fault_Status": {
                        "tags": [TAG.Point, TAG.Humidifier, TAG.Fault, TAG.Status],
                    },
                    "Last_Fault_Code_Status": {
                        "tags": [TAG.Point, TAG.Last, TAG.Fault, TAG.Code, TAG.Status],
                    },
                },
                "tags": [TAG.Point, TAG.Fault, TAG.Status],
            },
            "Filter_Status": {
                "subclasses": {
                    "Pre_Filter_Status": {
                        "tags": [TAG.Point, TAG.Pre, TAG.Filter, TAG.Status],
                    }
                },
                "tags": [TAG.Point, TAG.Filter, TAG.Status],
            },
            "Freeze_Status": {"tags": [TAG.Point, TAG.Freeze, TAG.Status]},
            "Hold_Status": {"tags": [TAG.Point, TAG.Hold, TAG.Status]},
            "Load_Shed_Status": {
                "subclasses": {
                    "Entering_Hot_Water_Temperature_Load_Shed_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Hot,
                            TAG.Water,
                            TAG.Entering,
                            TAG.Temperature,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Status,
                        ],
                        "subclasses": {
                            "Entering_Medium_Temperature_Hot_Water_Temperature_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Entering,
                                    TAG.Temperature,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                            },
                        },
                    },
                    "Leaving_Hot_Water_Temperature_Load_Shed_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Hot,
                            TAG.Water,
                            TAG.Leaving,
                            TAG.Temperature,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Status,
                        ],
                        "subclasses": {
                            "Leaving_Medium_Temperature_Hot_Water_Temperature_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Leaving,
                                    TAG.Temperature,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                            },
                        },
                    },
                    "Differential_Pressure_Load_Shed_Status": {
                        "subclasses": {
                            "Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Medium,
                                    TAG.Temperature,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                                "subclasses": {
                                    "Medium_Temperature_Hot_Water_Differential_Pressure_Load_Shed_Reset_Status": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Medium,
                                            TAG.Temperature,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Load,
                                            TAG.Shed,
                                            TAG.Reset,
                                            TAG.Status,
                                        ],
                                    },
                                },
                            },
                            "Chilled_Water_Differential_Pressure_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Chilled,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                                "subclasses": {
                                    "Chilled_Water_Differential_Pressure_Load_Shed_Reset_Status": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Chilled,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Load,
                                            TAG.Shed,
                                            TAG.Reset,
                                            TAG.Status,
                                        ],
                                    },
                                },
                            },
                            "Hot_Water_Differential_Pressure_Load_Shed_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Hot,
                                    TAG.Water,
                                    TAG.Differential,
                                    TAG.Pressure,
                                    TAG.Load,
                                    TAG.Shed,
                                    TAG.Status,
                                ],
                                "subclasses": {
                                    "Hot_Water_Differential_Pressure_Load_Shed_Reset_Status": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Hot,
                                            TAG.Water,
                                            TAG.Differential,
                                            TAG.Pressure,
                                            TAG.Load,
                                            TAG.Shed,
                                            TAG.Reset,
                                            TAG.Status,
                                        ],
                                    },
                                },
                            },
                        },
                        "tags": [
                            TAG.Point,
                            TAG.Differential,
                            TAG.Pressure,
                            TAG.Load,
                            TAG.Shed,
                            TAG.Status,
                        ],
                        "parents": [BRICK.Pressure_Status],
                    },
                },
                "tags": [TAG.Point, TAG.Load, TAG.Shed, TAG.Status],
            },
            "Lockout_Status": {
                "tags": [TAG.Point, TAG.Lockout, TAG.Status],
            },
            "Availability_Status": {
                "tags": [TAG.Point, TAG.Availability, TAG.Status],
            },
            "Manual_Auto_Status": {
                "tags": [TAG.Point, TAG.Manual, TAG.Auto, TAG.Status],
            },
            "Mode_Status": {
                "subclasses": {
                    "Speed_Mode_Status": {
                        "tags": [TAG.Point, TAG.Speed, TAG.Status, TAG.Mode],
                    },
                    "Zone_Air_Conditioning_Mode_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Air,
                            TAG.Zone,
                            TAG.Conditioning,
                            TAG.Mode,
                            TAG.Status,
                        ],
                    },
                    "Heating_Mode_Status": {
                        "tags": [TAG.Point, TAG.Heat, TAG.Mode, TAG.Status],
                        "subclasses": {
                            "Occupied_Heating_Mode_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Heat,
                                    TAG.Mode,
                                    TAG.Status,
                                    TAG.Occupied,
                                ],
                                "parents": [BRICK.Occupied_Mode_Status],
                            },
                            "Unoccupied_Heating_Mode_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Heat,
                                    TAG.Mode,
                                    TAG.Status,
                                    TAG.Unoccupied,
                                ],
                                "parents": [BRICK.Unoccupied_Mode_Status],
                            },
                        },
                    },
                    "Cooling_Mode_Status": {
                        "tags": [TAG.Point, TAG.Cool, TAG.Mode, TAG.Status],
                        "subclasses": {
                            "Occupied_Cooling_Mode_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Cool,
                                    TAG.Mode,
                                    TAG.Status,
                                    TAG.Occupied,
                                ],
                                "parents": [BRICK.Occupied_Mode_Status],
                            },
                            "Unoccupied_Cooling_Mode_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Cool,
                                    TAG.Mode,
                                    TAG.Status,
                                    TAG.Unoccupied,
                                ],
                                "parents": [BRICK.Unoccupied_Mode_Status],
                            },
                        },
                    },
                    "Occupied_Mode_Status": {
                        "tags": [TAG.Point, TAG.Occupied, TAG.Mode, TAG.Status],
                    },
                    "Unoccupied_Mode_Status": {
                        "tags": [TAG.Point, TAG.Unoccupied, TAG.Mode, TAG.Status],
                    },
                    "Operating_Mode_Status": {
                        "subclasses": {
                            "Vent_Operating_Mode_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Vent,
                                    TAG.Operating,
                                    TAG.Mode,
                                    TAG.Status,
                                ],
                            }
                        },
                        "tags": [TAG.Point, TAG.Operating, TAG.Mode, TAG.Status],
                    },
                },
                "tags": [TAG.Point, TAG.Mode, TAG.Status],
            },
            "Open_Close_Status": {
                "tags": [TAG.Point, TAG.Open, TAG.Close, TAG.Status],
            },
            "Occupancy_Status": {
                "subclasses": {
                    "Temporary_Occupancy_Status": {
                        "tags": [TAG.Point, TAG.Temporary, TAG.Occupancy, TAG.Status],
                    }
                },
                "tags": [TAG.Point, TAG.Occupancy, TAG.Status],
            },
            "On_Off_Status": {
                "subclasses": {
                    "Fan_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Fan, TAG.On, TAG.Off, TAG.Status],
                        "parents": [BRICK.Fan_Status],
                    },
                    "Motor_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Motor, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Pump_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Pump, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Locally_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Locally, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Remotely_On_Off_Status": {
                        "tags": [TAG.Point, TAG.Remotely, TAG.On, TAG.Off, TAG.Status],
                    },
                    "Standby_Unit_On_Off_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Standby,
                            TAG.Unit,
                            TAG.On,
                            TAG.Off,
                            TAG.Status,
                        ],
                        "subclasses": {
                            "Standby_Glycool_Unit_On_Off_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Standby,
                                    TAG.Glycool,
                                    TAG.Unit,
                                    TAG.On,
                                    TAG.Off,
                                    TAG.Status,
                                ],
                            },
                        },
                    },
                    "Start_Stop_Status": {
                        "subclasses": {
                            "Cooling_Start_Stop_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Cool,
                                    TAG.Start,
                                    TAG.Stop,
                                    TAG.Status,
                                ],
                            },
                            "Dehumidification_Start_Stop_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Dehumidification,
                                    TAG.Start,
                                    TAG.Stop,
                                    TAG.Status,
                                ],
                            },
                            "EconCycle_Start_Stop_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Econcycle,
                                    TAG.Start,
                                    TAG.Stop,
                                    TAG.Status,
                                ],
                            },
                            "Heating_Start_Stop_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Heat,
                                    TAG.Start,
                                    TAG.Stop,
                                    TAG.Status,
                                ],
                            },
                            "Humidification_Start_Stop_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Humidification,
                                    TAG.Start,
                                    TAG.Stop,
                                    TAG.Status,
                                ],
                            },
                            "Run_Status": {
                                "tags": [TAG.Point, TAG.Run, TAG.Status],
                                "subclasses": {
                                    "Run_Request_Status": {
                                        "tags": [
                                            TAG.Point,
                                            TAG.Request,
                                            TAG.Run,
                                            TAG.Status,
                                        ],
                                    },
                                },
                            },
                        },
                        "tags": [TAG.Point, TAG.Start, TAG.Stop, TAG.Status],
                    },
                },
                "tags": [TAG.Point, TAG.On, TAG.Off, TAG.Status],
                "parents": [BRICK.On_Status, BRICK.Off_Status],
            },
            "Off_Status": {"tags": [TAG.Point, TAG.Off, TAG.Status]},
            "On_Status": {"tags": [TAG.Point, TAG.On, TAG.Status]},
            "Overridden_Status": {
                "subclasses": {
                    "Overridden_Off_Status": {
                        "tags": [TAG.Point, TAG.Overridden, TAG.Off, TAG.Status],
                        "parents": [BRICK.Off_Status],
                    },
                    "Overridden_On_Status": {
                        "tags": [TAG.Point, TAG.Overridden, TAG.On, TAG.Status],
                        "parents": [BRICK.On_Status],
                    },
                },
                "tags": [TAG.Point, TAG.Overridden, TAG.Status],
            },
            "Pressure_Status": {
                BRICK.hasQuantity: QUDTQK.Pressure,
                "subclasses": {
                    "Supply_Air_Duct_Pressure_Status": {
                        "aliases": [BRICK["Discharge_Air_Duct_Pressure_Status"]],
                        "tags": [
                            TAG.Point,
                            TAG.Supply,
                            TAG.Discharge,
                            TAG.Air,
                            TAG.Duct,
                            TAG.Pressure,
                            TAG.Status,
                        ],
                    },
                },
                "tags": [TAG.Point, TAG.Pressure, TAG.Status],
            },
            "Lead_Lag_Status": {"tags": [TAG.Point, TAG.Lead, TAG.Lag, TAG.Status]},
            "Level_Status": {
                "tags": [TAG.Level, TAG.Status, TAG.Point],
            },
            "Stages_Status": {"tags": [TAG.Point, TAG.Stages, TAG.Status]},
            "System_Shutdown_Status": {
                "tags": [TAG.Point, TAG.System, TAG.Shutdown, TAG.Status],
                "parents": [BRICK.System_Status],
            },
            "System_Status": {
                "tags": [TAG.Point, TAG.System, TAG.Status],
                "subclasses": {
                    "Emergency_Air_Flow_System_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Emergency,
                            TAG.Air,
                            TAG.Flow,
                            TAG.System,
                            TAG.Status,
                        ],
                    },
                    "Emergency_Power_Off_System_Status": {
                        "tags": [
                            TAG.Point,
                            TAG.Emergency,
                            TAG.Power,
                            TAG.Off,
                            TAG.System,
                            TAG.Status,
                        ],
                        "parents": [BRICK.Off_Status],
                        "subclasses": {
                            "Emergency_Power_Off_System_Activated_By_High_Temperature_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Emergency,
                                    TAG.Power,
                                    TAG.Off,
                                    TAG.System,
                                    TAG.High,
                                    TAG.Temperature,
                                    TAG.Status,
                                ],
                            },
                            "Emergency_Power_Off_System_Activated_By_Leak_Detection_System_Status": {
                                "tags": [
                                    TAG.Point,
                                    TAG.Emergency,
                                    TAG.Power,
                                    TAG.Off,
                                    TAG.System,
                                    TAG.Leak,
                                    TAG.Detection,
                                    TAG.Status,
                                ],
                            },
                        },
                    },
                },
            },
        },
    }
}
