class IoTFunctions:
    def __init__(self, client):
        self.client = client
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_subscribe = self.on_subscribe
        self.client.on_log = self.on_log
        self.client.on_disconnect = self.on_disconnect
        self.client.on_unsubscribe = self.on_unsubscribe

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("iot-2/type/+/id/+/evt/+/fmt/+")

    @staticmethod
    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    @staticmethod
    def on_publish(client, userdata, mid):
        print("mid: "+str(mid))

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    @staticmethod
    def on_log(client, userdata, level, buf):
        print("log: "+buf)

    @staticmethod
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")

    @staticmethod
    def on_unsubscribe(client, userdata, mid):
        print("Unsubscribed: "+str(mid))
    
    def publish(self, topic, payload, qos=0, retain=False):
        self.client.publish(topic, payload, qos, retain)   
        pass
