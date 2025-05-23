from .namespaces import BRICK, RDFS, SKOS, A, QUDTQK

deprecations = {
    BRICK.Speed_Status: {
        "version": "1.4.0",
        "mitigation_message": "Speed Status is no longer necessary. Use Speed Mode Status for motors with various categorical speed settings, such as low, medium, and high. To further clarify, points representing the current speed of a variable speed fan as an analog value or input, use Speed Sensor.",
        "replace_with": BRICK.Speed_Mode_Status,
        RDFS.subClassOf: BRICK.Status,
    },
    BRICK.Condenser: {
        "version": "1.3.0",
        "mitigation_message": "'Condenser' and 'Condensing Unit' are interchangable terms. Renaming class to 'Condensing_Unit' to further aligns with ASHRAE's terminology.",
        "replace_with": BRICK.Condensing_Unit,
    },
    BRICK.Heat_Sensor: {
        "version": "1.4.0",
        "mitigation_message": "This class has a poor definition is supplanted by Temperature_Sensor",
        "replace_with": BRICK.Temperature_Sensor,
        RDFS.subClassOf: BRICK.Sensor,
    },
    BRICK.Trace_Heat_Sensor: {
        "version": "1.4.0",
        "mitigation_message": "Removed due to unclear definition",
        "replace_with": BRICK.Sensor,
    },
    BRICK.Solar_Radiance_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Solar_Radiance_Sensor' is deprecated in favor of 'Solar_Irradiance_Sensor'. The new name better reflects the standard unit of measurement, watts per square meter (W/m²), and aligns with the terminology commonly used in solar applications.",
        "replace_with": BRICK.Solar_Irradiance_Sensor,
        RDFS.subClassOf: BRICK.Sensor,
    },
    BRICK.Occupied_Air_Temperature_Cooling_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Occupied_Air_Temperature_Cooling_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Occupied_Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Occupied_Air_Temperature_Setpoint,
    },
    BRICK.Occupied_Air_Temperature_Heating_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Occupied_Air_Temperature_Heating_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Occupied_Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Occupied_Air_Temperature_Setpoint,
    },
    BRICK.Unoccupied_Air_Temperature_Cooling_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Unoccupied_Air_Temperature_Cooling_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Unoccupied_Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Unoccupied_Air_Temperature_Setpoint,
    },
    BRICK.Unoccupied_Air_Temperature_Heating_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Unoccupied_Air_Temperature_Heating_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Unoccupied_Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Unoccupied_Air_Temperature_Setpoint,
    },
    BRICK.Effective_Air_Temperature_Cooling_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Effective_Air_Temperature_Cooling_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Effective_Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Effective_Air_Temperature_Setpoint,
    },
    BRICK.Effective_Air_Temperature_Heating_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Effective_Air_Temperature_Heating_Setpoint' is deprecated in favor of further specifying that it is a zone air setpoint.",
        "replace_with": BRICK.Effective_Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Effective_Air_Temperature_Setpoint,
    },
    BRICK.Zone_Air_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Zone_Air_Temperature_Setpoint' is deprecated in favor of more explicit class names to distinguish target and cooling/heating setpoints.",
        "replace_with": BRICK.Target_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Air_Temperature_Setpoint,
    },
    BRICK.Effective_Zone_Air_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "The class 'Effective_Zone_Air_Temperature_Setpoint' is deprecated and replaced to better represent its function as a target setpoint",
        "replace_with": BRICK.Effective_Target_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Occupied_Zone_Air_Temperaure_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Occupied_Zone_Air_Temperature_Setpoint' is deprecated in favor of further specifying that it is a target setpoint",
        "replace_with": BRICK.Occupied_Target_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Unoccupied_Zone_Air_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Unoccupied_Zone_Air_Temperature_Setpoint' is deprecated in favor of further specifying that it is a target setpoint",
        "replace_with": BRICK.Unoccupied_Target_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Zone_Air_Cooling_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Zone_Air_Cooling_Temperature_Setpoint' is deprecated to support new naming convention, which reorders intended behaviour (cooling) before the substance (zone air).",
        "replace_with": BRICK.Cooling_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Zone_Air_Heating_Temperature_Setpoint: {
        "version": "1.3.0",
        "mitigation_message": "'Zone_Air_Heating_Temperature_Setpoint' is deprecated to support new naming convention, whic reorders intended behaviour (heating) before the substance (zone air)",
        "replace_with": BRICK.Heating_Zone_Air_Temperature_Setpoint,
        RDFS.subClassOf: BRICK.Zone_Air_Temperature_Setpoint,
    },
    BRICK.Fresh_Air_Fan: {
        "version": "1.3.0",
        "mitigation_message": "Fresh Air Fan is deprecated in favor of Outside Fan because the latter is a more accurate representation",
        "replace_with": BRICK.Outside_Fan,
        RDFS.subClassOf: BRICK.Fan,
    },
    BRICK.Exhaust_Fan_Disable_Command: {
        "version": "1.3.0",
        "mitigation_message": "Exhaust_Fan_Disable_Command is deprecated as a point name should not include more specific equipment names than top level equipment names",
        "replace_with": BRICK.Disable_Command,
        RDFS.subClassOf: BRICK.Command,
    },
    BRICK.Exhaust_Fan_Enable_Command: {
        "version": "1.3.0",
        "mitigation_message": "Exhaust_Fan_Enable_Command is deprecated as a point name should not include more specific equipment names than top level equipment names",
        "replace_with": BRICK.Enable_Command,
    },
    BRICK.Light_Command: {
        "version": "1.3.1",
        "mitigation_message": "Replaced with Lighting_Command to represent its function more precisely.",
        "replace_with": BRICK.Lighting_Level_Command,
        RDFS.subClassOf: BRICK.Command,
    },
    BRICK.Supply_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Discharge_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Supply_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Flow_Sensor,
        RDFS.subClassOf: BRICK.Water_Flow_Sensor,
    },
    BRICK.Discharge_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Flow_Sensor,
        RDFS.subClassOf: BRICK.Water_Flow_Sensor,
    },
    BRICK.Chilled_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Chilled_Water_Supply_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Supply_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Chilled_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Flow_Sensor,
            BRICK.Chilled_Water_Flow_Sensor,
        ],
    },
    BRICK.Supply_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water,
        SKOS.broader: BRICK.Water,
        A: BRICK.Substance,
    },
    BRICK.Supply_Chilled_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water,
        SKOS.broader: BRICK.Chilled_Water,
        A: BRICK.Substance,
    },
    BRICK.Discharge_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water,
        SKOS.broader: BRICK.Water,
        A: BRICK.Substance,
    },
    BRICK.Discharge_Chilled_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water,
        SKOS.broader: BRICK.Chilled_Water,
        A: BRICK.Substance,
    },
    BRICK.Supply_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water,
        SKOS.broader: BRICK.Hot_Water,
        A: BRICK.Substance,
    },
    BRICK.Discharge_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water,
        SKOS.broader: BRICK.Hot_Water,
        A: BRICK.Substance,
    },
    BRICK.Return_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water,
        SKOS.broader: BRICK.Water,
        A: BRICK.Substance,
    },
    BRICK.Return_Hot_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water,
        SKOS.broader: BRICK.Hot_Water,
        A: BRICK.Substance,
    },
    BRICK.Supply_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water,
        SKOS.broader: BRICK.Condenser_Water,
        A: BRICK.Substance,
    },
    BRICK.Discharge_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water,
        SKOS.broader: BRICK.Condenser_Water,
        A: BRICK.Substance,
    },
    BRICK.Return_Condenser_Water: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water,
        SKOS.broader: BRICK.Condenser_Water,
        A: BRICK.Substance,
    },
    BRICK.Heat_Exchanger_Supply_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Heat_Exchanger_Leaving_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Heat_Exchanger_Discharge_Water_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Heat_Exchanger_Leaving_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Hot_Water_Supply_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Flow_Sensor,
        RDFS.subClassOf: [BRICK.Hot_Water_Flow_Sensor, BRICK.Supply_Water_Flow_Sensor],
    },
    BRICK.Hot_Water_Discharge_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Hot_Water_Flow_Sensor,
            BRICK.Discharge_Water_Flow_Sensor,
        ],
    },
    BRICK.Hot_Water_Supply_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
    BRICK.Domestic_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Domestic_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Domestic_Hot_Water_Temperature_Sensor,
    },
    BRICK.High_Temperature_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_High_Temperature_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Hot_Water_Discharge_Temperature_Sensor,
    },
    BRICK.Medium_Temperature_Hot_Water_Discharge_Temperature_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Medium_Temperature_Hot_Water_Temperature_Sensor,
        RDFS.subClassOf: BRICK.Hot_Water_Discharge_Temperature_Sensor,
    },
    BRICK.Return_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water_Flow_Sensor,
        RDFS.subClassOf: BRICK.Water_Flow_Sensor,
    },
    BRICK.Chilled_Water_Return_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Chilled_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Flow_Sensor,
            BRICK.Return_Water_Flow_Sensor,
        ],
    },
    BRICK.Hot_Water_Return_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water_Flow_Sensor,
        RDFS.subClassOf: [BRICK.Hot_Water_Flow_Sensor, BRICK.Return_Water_Flow_Sensor],
    },
    BRICK.Return_Condenser_Water_Flow_Sensor: {
        "version": "1.3.0",
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water_Flow_Sensor,
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Flow_Sensor,
            BRICK.Return_Water_Flow_Sensor,
        ],
    },
    BRICK.Chilled_Water_Discharge_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Flow_Setpoint,
            BRICK.Discharge_Water_Flow_Setpoint,
        ],
    },
    BRICK.Chilled_Water_Return_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Chilled_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Sensor,
            BRICK.Return_Water_Temperature_Sensor,
        ],
    },
    BRICK.Chilled_Water_Supply_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Flow_Setpoint,
            BRICK.Supply_Water_Flow_Setpoint,
        ],
    },
    BRICK.Chilled_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Sensor,
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Chilled_Water_Discharge_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Sensor,
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
    BRICK.Differential_Supply_Return_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Differential_Entering_Leaving_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Differential_Temperature_Sensor,
    },
    BRICK.Differential_Discharge_Return_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Differential_Entering_Leaving_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Differential_Temperature_Sensor,
    },
    BRICK.Domestic_Hot_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Domestic_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Supply_Temperature_Sensor,
    },
    BRICK.Domestic_Hot_Water_Supply_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Domestic_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Supply_Hot_Water_Temperature_Setpoint,
    },
    BRICK.Domestic_Hot_Water_Discharge_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Domestic_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Discharge_Hot_Water_Temperature_Setpoint,
    },
    BRICK.High_Temperature_Hot_Water_Return_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_High_Temperature_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Return_Temperature_Sensor,
    },
    BRICK.High_Temperature_Hot_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_High_Temperature_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Supply_Temperature_Sensor,
    },
    BRICK.Hot_Water_Discharge_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Flow_Setpoint,
            BRICK.Hot_Water_Flow_Setpoint,
        ],
    },
    BRICK.Discharge_Water_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Water_Flow_Setpoint,
        ],
    },
    BRICK.Supply_Water_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Water_Flow_Setpoint,
        ],
    },
    BRICK.Hot_Water_Return_Flow_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water_Flow_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [BRICK.Return_Water_Flow_Sensor, BRICK.Hot_Water_Flow_Sensor],
    },
    BRICK.Hot_Water_Return_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Return_Water_Temperature_Sensor,
        ],
    },
    BRICK.Hot_Water_Supply_Flow_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Flow_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Hot_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Medium_Temperature_Hot_Water_Return_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Medium_Temperature_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Return_Temperature_Sensor,
    },
    BRICK.Medium_Temperature_Hot_Water_Supply_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Medium_Temperature_Hot_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Hot_Water_Supply_Temperature_Sensor,
    },
    BRICK.Return_Chilled_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Chilled_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Setpoint,
            BRICK.Return_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Return_Condenser_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Condenser_Water_Temperature_Sensor,
    },
    BRICK.Return_Condenser_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Condenser_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Return_Water_Temperature_Setpoint,
    },
    BRICK.Return_Hot_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Return_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Return_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Temperature_Sensor,
    },
    BRICK.Return_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Entering_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: BRICK.Water_Temperature_Setpoint,
    },
    BRICK.Supply_Chilled_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Discharge_Chilled_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Chilled_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Chilled_Water_Temperature_Setpoint,
        ],
    },
    BRICK.Supply_Condenser_Water: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water,
        "version": "1.3.0",
        SKOS.broader: BRICK.Condenser_Water,
        A: BRICK.Substance,
    },
    BRICK.Supply_Condenser_Water_Flow_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Flow_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Flow_Sensor,
            BRICK.Supply_Water_Flow_Sensor,
        ],
    },
    BRICK.Discharge_Condenser_Water_Flow_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Flow_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Flow_Sensor,
            BRICK.Discharge_Water_Flow_Sensor,
        ],
    },
    BRICK.Supply_Condenser_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Temperature_Sensor,
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Discharge_Condenser_Water_Temperature_Sensor: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Sensor,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Condenser_Water_Temperature_Sensor,
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
    BRICK.Supply_Condenser_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Discharge_Condenser_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Condenser_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },
    BRICK.Supply_Hot_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Supply_Water_Temperature_Sensor,
        ],
    },
    BRICK.Discharge_Hot_Water_Temperature_Setpoint: {
        "mitigation_message": "Swapped supply/return for entering/leaving with water-related points",
        "replace_with": BRICK.Leaving_Hot_Water_Temperature_Setpoint,
        "version": "1.3.0",
        RDFS.subClassOf: [
            BRICK.Discharge_Water_Temperature_Sensor,
        ],
    },

    BRICK.Electric_Current: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Electric_Current' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/ElectricCurrent' directly.",
        "replace_with": QUDTQK.ElectricCurrent,
    },
    BRICK.Voltage: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Voltage' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Voltage' directly.",
        "replace_with": QUDTQK.Voltage,
    },
    BRICK.Thermal_Energy: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Thermal_Energy' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/ThermalEnergy' directly.",
        "replace_with": QUDTQK.ThermalEnergy,
    },
    BRICK.Frequency: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Frequency' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Frequency' directly.",
        "replace_with": QUDTQK.Frequency,
    },
    BRICK.Irradiance: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Irradiance' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Irradiance' directly. For specific solar irradiance, use brick:Solar_Irradiance.",
        "replace_with": QUDTQK.Irradiance,
    },
    BRICK.Power_Factor: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Power_Factor' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/PowerFactor' directly.",
        "replace_with": QUDTQK.PowerFactor,
    },
    BRICK.Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined generic quantity 'Pressure' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Pressure' directly, or more specific QUDT/Brick quantities like qudt:QuantityKind/StaticPressure, qudt:QuantityKind/AtmosphericPressure, brick:Differential_Pressure, etc.",
        "replace_with": QUDTQK.Pressure,
    },
    BRICK.Atmospheric_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Atmospheric_Pressure' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/AtmosphericPressure' directly.",
        "replace_with": QUDTQK.AtmosphericPressure,
    },
     BRICK.Gauge_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Gauge_Pressure' is deprecated. Use the QUDT quantity 'qudt:QuantityKind/Pressure' and indicate contextually that it is gauge pressure if necessary.",
        "replace_with": QUDTQK.Pressure,
    },
    BRICK.Static_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Static_Pressure' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/StaticPressure' directly.",
        "replace_with": QUDTQK.StaticPressure,
    },
    BRICK.Dynamic_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Dynamic_Pressure' (also referred to as Velocity_Pressure) is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/DynamicPressure' directly.",
        "replace_with": QUDTQK.DynamicPressure,
    },
    BRICK.Velocity_Pressure: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Velocity_Pressure' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/DynamicPressure' directly.",
        "replace_with": QUDTQK.DynamicPressure,
    },
    BRICK.Radiance: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Radiance' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Radiance' directly. For specific solar radiance, use brick:Solar_Radiance.",
        "replace_with": QUDTQK.Radiance,
    },
    BRICK.Temperature: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined generic quantity 'Temperature' is deprecated for direct use. Use the equivalent QUDT quantity 'qudt:QuantityKind/Temperature' directly, or more specific Brick quantities like brick:Dry_Bulb_Temperature, brick:Wet_Bulb_Temperature, etc., which now subclass the QUDT quantity.",
        "replace_with": QUDTQK.Temperature,
    },
    BRICK.Time: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Time' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Time' directly.",
        "replace_with": QUDTQK.Time,
    },
    BRICK.Energy: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Energy' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Energy' directly.",
        "replace_with": QUDTQK.Energy,
    },
    BRICK.Deceleration_Time: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Deceleration_Time' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Time' directly.",
        "replace_with": QUDTQK.Time,
    },
    BRICK.Acceleration_Time: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Acceleration_Time' is deprecated. Use the equivalent QUDT quantity 'qudt:QuantityKind/Time' directly.",
        "replace_with": QUDTQK.Time,
    },
    BRICK.Radioactivity_Concentration_Sensor: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Radioactivity_Concentration_Sensor' is deprecated. Use Air_Quality_Sensor instead, or the provided sensor class for the specific kind or source of radioactivity (e.g. Radon gas)",
        "replace_with": BRICK.Air_Quality_Sensor,
    },

    BRICK.Phasor: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Phasor' is deprecated.",
    },
    BRICK.Radioactivity_Concentration: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Radioactivity_Concentration' is deprecated.",
    },
    BRICK.Weather_Condition: {
        "version": "1.4.4",
        "mitigation_message": "Brick-defined quantity 'Weather_Condition' is deprecated.",
    },
}
