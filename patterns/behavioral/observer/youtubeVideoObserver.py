# Observer Design Pattern for a YouTube video notification system

class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.latest_video = None

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.name, self.latest_video)

    def upload_video(self, video_title):
        self.latest_video = video_title
        print(f"[{self.name}] Uploaded a new video: '{video_title}'")
        self.notify_subscribers()


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, channel_name, video_title):
        print(f"{self.name} received notification: '{video_title}' uploaded on {channel_name}")


# Example usage
if __name__ == "__main__":
    channel = YouTubeChannel("AI Tutorials")
    alice = Subscriber("Alice")
    bob = Subscriber("Bob")

    channel.subscribe(alice)
    channel.subscribe(bob)

    channel.upload_video("Observer Pattern Explained")
    print("--------------------------------")

    channel.unsubscribe(bob)
    channel.upload_video("Strategy Pattern in Python")
    print("--------------------------------")
