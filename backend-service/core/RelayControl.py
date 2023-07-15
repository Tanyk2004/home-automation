import RPi.GPIO as GPIO
from time import sleep
from core.db.model import dbManager

class Relay:

    """
    A class used to represent a relay. These functions are used to control the 
    state of each relay. The relay is initialized to low, and the state can be 
    changed by calling the setRelayState function. The state can be retrieved
    by calling the getRelayState function.
    """


    def __init__(self, relay_id: int, is_on: bool):
        """
        @param relay_id: The GPIO pin number
        @param is_on: The state of the relay

        initializes the relay object, and sets the
        output of the actual relay to low
        """
        self.relay_id = relay_id
        self.is_on = is_on
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.relay_id, GPIO.OUT)
        GPIO.output(self.relay_id, GPIO.HIGH if is_on else GPIO.LOW)

    def getId(self) -> int:
        """
        Returns the id of the relay
        """
        return self.relay_id
   
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
        GPIO.output(self.relay_id, (GPIO.HIGH if self.is_on else GPIO.LOW))



class RelayStateControl:

    """
    A container class for different various objects that can be used to abstract 
    handling multiple relays and the GPIO operations that need to be done with them.
    """

    def __init__(self):
        self.relayContainer = []
        self.db = dbManager()
        
        for relay in self.db.getAllRelays():
            self.relayContainer.append(Relay(relay[0], relay[1]))
    
    def __str__(self) -> str:
        """
        Prints the list of relays in the container
        """
        output = ""
        for relay in self.relayContainer:
            # print(f"Relay {relay.getId()} is {relay.getRelayState()}")
            output += "\n" + f"Relay {relay.getId()} is {'On' if relay.getRelayState() == 1 else 'Off'}"
        return output

    def addRelay(self, id: int, is_on: bool) -> bool:
        """
        Adds a new relay to the container, and due to the nested class in the file,
        the relay is automatically set to low
        Args:
            :param id: The relay id
            :param is_on: The state of the relay
        Return:
            :returns true if the relay was successfully added
        """
        newRelay = Relay(id, is_on)
        self.relayContainer.append(newRelay)
        if not self.db.checkIfRelayExists(id):
            self.db.addRelay(id, is_on)
            return True
        return False

    def initializeLow(self):
        """
        Sets all the relays in the container to LOW
        """
        for relay in self.relayContainer:
            self.db.updateRelayState(relay.getId(), False)
            relay.setRelayState(False)
    
    
    def getRelayIndex ( self, index : int) -> Relay:
        """
        Args:
            :param index : int -> The index of the relay we want to get
        """
        return self.relayContainer[index]

    def getRelay(self, id: int) -> Relay:
        """
        Args:
            :param id : int -> The id of the relay we want to get
        Return:
            :return -> the relay with the passed in id
        """
        for relay in self.relayContainer:
            if relay.getId() == id:
                return relay
        else:
            raise ValueError("Relay Not Found")

    def removeRelay(self, id: int) -> Relay:
        """

        Removes a relay with the passed in id from the container as well as the database

        Args:
            :param id : int -> Id of the relay that needs to be popped
        Return:
            :returns -> the popped relay object
        """
        if not self.db.checkIfRelayExists(id):
            raise ValueError("Relay does not exist")
        else:
            for relay, index in zip(self.relayContainer, range(len(self.relayContainer))):
                if relay.getId() == id:
                    poppedRelay: Relay = relay
                    self.db.dropRelay(id)
                    self.relayContainer.pop(index)
                    poppedRelay.setRelayState(False)
                    return poppedRelay

    def popRelay(self, index: int) -> Relay:
        """
        Args:
            :param index : int -> index of the relay that we want to remove
        Return:
            :returns -> the popped relay object
        """

        poppedRelay: Relay = self.relayContainer.pop(index)
        self.db.removeRelay(poppedRelay.getId())
        return poppedRelay
    
    def getAllRelays(self) -> list:
        """
        Return:
            :returns a list of all the relays that are connected
        """
        return self.db.getAllRelays()

    def updateRelay(self, id : int, state : bool) -> bool:
        """
        Updates the state of the relay and its value in the database

        Args:
            :param id of the relay that needs to be updated
            :param state that the relay takes after the function is executed

        Return:
            :returns true if the relay was modified successfully

        """
        relay = self.getRelay(id)
        if relay is not None:
            # relay exists
            relay.setRelayState(state)
            self.db.updateRelayState(id, state)
            return True
        return False

if __name__ == "__main__":
    rsc = RelayStateControl()
    print(rsc)
