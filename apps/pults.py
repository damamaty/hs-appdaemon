import hassapi as hass


class Pults(hass.Hass):
    # For reference
    LIGHTS = {
        "bedroom": {
            "light.bedroom_child_switcher",
            "light.bedroom_parent_switcher",
            "light.underbed_switcher",
            "light.child_desktop_lamp",
        },
        "living": {
            "light.switcher_living": {
                "light.living_lamp_work_1",
                "light.living_lamp_work_2",
                "light.living_lamp_work_3",
                "light.living_lamp_work_4",
            }
        },
        "kitchen": {
            "light.kitchen_light": {
                "light.kitchen_lamp_1",
                "light.kitchen_lamp_2",
                "light.kitchen_lamp_3",
                "light.kitchen_lamp_4",
            }
        },
        "toilet": {
            "light.toilet_switcher"
        },
        "shower": {
            "light.shower_light_switcher"
        },
        "coridor": {
            "light.coridor_light": {
                "light.coridor_lamp_1",
                "light.coridor_lamp_2",
                "light.coridor_lamp_3",
            }
        }
    }

    def initialize(self):
        self.listen_state(self.pult_pressed, "sensor.four_pult_3_action")
        self.listen_state(self.pult_pressed, "sensor.four_pult_2_action")
        self.listen_state(self.pult_pressed, "sensor.six_pult_1_action")

        self.listen_state(self.button_pressed, "sensor.white_button_2_action")
        self.listen_state(self.button_pressed, "sensor.white_button_6_action")

    def button_pressed(self, entity, attribute, old, new, cb_args):
        if attribute != "state" or not new:
            return

        self.log(["Button Pressed", entity, attribute, old, new, cb_args])

        if entity == "sensor.white_button_2_action":
            match new:
                case "single": self.toggle("light.switcher_living")
                case "double": self.toggle("switch.roboarm_living")
                case "triple": self.toggle("light.kitchen_light")
                case "quadruple": self.toggle("switch.roboarm_kitchen")
                case "hold": self.close_all_windows()

        if entity == "sensor.white_button_6_action":
            match new:
                case "single": self.toggle("light.switcher_living")
                case "double": self.toggle("switch.roboarm_living")
                case "triple": self.toggle("light.kitchen_light")
                case "quadruple": self.toggle("switch.roboarm_kitchen")
                case "hold": self.close_all_windows()

    def pult_pressed(self, entity, attribute, old, new, cb_args):
        if attribute != "state" or not new:
            return

        self.log(["Pult Pressed", entity, attribute, old, new, cb_args])

        # Living - Working place
        if entity == "sensor.four_pult_3_action":
            match new:
                case "1_single": self.toggle("light.switcher_living")
                case "1_double": self.toggle("switch.roboarm_living")
                case "2_single": pass
                case "2_double": pass
                case "3_single": self.toggle("light.kitchen_light")
                case "3_double": self.toggle("switch.roboarm_kitchen")
                case "4_single": self.open_all_windows()
                case "4_double": self.close_all_windows()

        # Living - Sofa
        if entity == "sensor.four_pult_2_action":
            match new:
                case "1_single": self.toggle("light.switcher_living")
                case "1_double": self.toggle("switch.roboarm_living")
                case "2_single": pass
                case "2_double": pass
                case "3_single": self.toggle("light.kitchen_light")
                case "3_double": self.toggle("switch.roboarm_kitchen")
                case "4_single": self.open_all_windows()
                case "4_double": self.close_all_windows()

        # Living - Entry
        if entity == "sensor.six_pult_1_action":
            match new:
                case "1_single": self.toggle("light.switcher_living")
                case "1_double": self.toggle("switch.roboarm_living")
                case "2_single": pass
                case "2_double": pass
                case "3_single": self.toggle("light.kitchen_light")
                case "3_double": self.toggle("switch.roboarm_kitchen")
                case "4_single": self.open_all_windows()
                case "4_double": self.close_all_windows()
                case "5_single": pass
                case "5_double": pass
                case "6_single": self.turn_off_all_lights()
                case "6_double": pass

    def open_all_windows(self):
        self.turn_off("switch.roboarm_living")
        self.turn_off("switch.roboarm_kitchen")

    def close_all_windows(self):
        self.turn_on("switch.roboarm_living")
        self.turn_on("switch.roboarm_kitchen")

    def turn_off_all_lights(self):
        self.turn_off("light.bedroom_child_switcher")
        self.turn_off("light.bedroom_parent_switcher")
        self.turn_off("light.underbed_switcher")
        self.turn_off("light.child_desktop_lamp")

        self.turn_off("light.kitchen_light")
        self.turn_off("light.shower_light_switcher")
        self.turn_off("light.toilet_switcher")
        self.turn_off("light.switcher_living")
        self.turn_off("light.coridor_light")

