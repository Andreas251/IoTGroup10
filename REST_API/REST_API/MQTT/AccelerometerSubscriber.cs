using System;
using System.Text;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;

namespace REST_API.MQTT
{
    public class AccelerometerSubscriber
    {
        private const string MqttUri = "626582a1d37a4c9da269c096cf520060.s1.eu.hivemq.cloud";
        private const int port = 8883;

        public static void Subscribe()
        {
            var client = new MqttClient(MqttUri, port, true, null, null, MqttSslProtocols.TLSv1_2);
            client.MqttMsgPublishReceived += HandlePublishedMessage;
            var clientId = Guid.NewGuid().ToString();

            client.Connect(clientId, "iotgrp10", "Faelles123kode098");

            client.Subscribe(new[] { "iot_grp10/accelerometer" }, new[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
        }

        static void HandlePublishedMessage(object sender, MqttMsgPublishEventArgs e)
        {
            var message = Encoding.UTF8.GetString(e.Message);
            // handle message received 
        }
    }
}
