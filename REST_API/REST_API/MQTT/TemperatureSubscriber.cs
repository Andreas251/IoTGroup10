using System;
using System.Text;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;

namespace REST_API.MQTT
{
    public class TemperatureSubscriber
    {
        private const string MqttUri = "broker.mqttdashboard.com";
        public static void Subscribe()
        {
            var client = new MqttClient(MqttUri);
            client.MqttMsgPublishReceived += HandlePublishedMessage;
            var clientId = Guid.NewGuid().ToString();

            client.Connect(clientId);

            client.Subscribe(new[] { "iot_grp10/temp" }, new[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
        }

        static void HandlePublishedMessage(object sender, MqttMsgPublishEventArgs e)
        {
            var message = Encoding.UTF8.GetString(e.Message);
            // handle message received 
        }
    }
}
