import hassapi as hass


class Pults(hass.Hass):
    def initialize(self):
        self.listen_state(self.pult_pressed, "sensor.four_pult_3_action")

    def pult_pressed(self, entity, attribute, old, new, cb_args):
        if attribute != "state" or not new:
            return

        self.log([entity, attribute, old, new, cb_args])

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

    def open_all_windows(self):
        self.turn_off("switch.roboarm_living")
        self.turn_off("switch.roboarm_kitchen")

    def close_all_windows(self):
        self.turn_on("switch.roboarm_living")
        self.turn_on("switch.roboarm_kitchen")
                        
