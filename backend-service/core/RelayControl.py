import RPi.GPIO as GPIO
from time import sleep


class Relay:

    """
    @param relay_id: The GPIO pin number
    @param is_on: The state of the relay

    initializes the relay object, and sets the
    output of the actual relay to low
    """

    def __init__(self, relay_id: int, is_on: bool):
        self.relay_id = relay_id
        self.is_on = is_on
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.relay_id, GPIO.OUT)
        GPIO.output(self.relay_id, GPIO.LOW)

   

    def getRelayState(self) -> bool:
        """
        :return: The state of the relay (True or False)
        """
        return self.is_on

    def setRelayState(self, is_on: bool):
        """
        :param is_on: The state of the relay (True or False)
        """
        self.is_on = is_on
        GPIO.output(self.relay_id, (GPIO.LOW if self.is_on else GPIO.HIGH))


class RelayStateControl:
    def __init__(self, relayContainer: list = None, relay: Relay = None):
        self.relayContainer = []
        if relayContainer is not None:
            self.relayContainer = relayContainer
        if relay is not None:
            self.relayContainer.append(relay)

    def addRelay(self, id: int, is_on: bool):
        """
        Adds a new relay to the container, and due to the nested class in the file,
        the relay is automatically set to low

        :param relay: The relay object to be added to the container
        """
        self.relayContainer.append(Relay(id, is_on))

    def initializeLow(self):
        for relay in self.relayContainer:
            relay.setRelayState(False)


if __name__ == "__main__":
    rsc = RelayStateControl()
    rsc.addRelay(4, False)
    rsc.initializeLow(4, False)

