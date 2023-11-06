CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    channel_now = 1

    def __init__(self, channels):
        self.channels = channels
    def first_channel(self):
        self.channel_now = 1
        print(self.channels[0])

    def last_channel(self):
        self.channel_now = 3
        print(self.channels[-1])

    def turn_channel(self, which_channel):
        self.channel_now = which_channel
        print(self.channels[which_channel - 1])

    def next_channel(self):
        self.channel_now += 1
        print(self.channels[self.channel_now - 1])

    def previous_channel(self):
        self.channel_now -= 1
        print(self.channels[self.channel_now - 1])

    def current_channel(self):
        print(self.channels[self.channel_now - 1])

    def is_exist(self, channel):
        if isinstance(channel, str):
            if channel in self.channels:
                print("Yes")
            else:
                print("No")
        elif isinstance(channel, int):
            print("Yes") if 1 <= channel <= len(self.channels) else print("No")



controller = TVController(CHANNELS)

controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(4)
controller.is_exist("BBC")

