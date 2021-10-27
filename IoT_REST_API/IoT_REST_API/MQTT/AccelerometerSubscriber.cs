﻿using System;
using System.Text;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;

namespace REST_API.MQTT
{
    public class AccelerometerSubscriber
    {
        public static void Subscribe(MqttSettings settings)
        {
            if (settings == null) throw new ArgumentNullException(nameof(settings));

            var client = new MqttClient(settings.URI, settings.Port, settings.isSecure, null, null, MqttSslProtocols.TLSv1_2);
            client.MqttMsgPublishReceived += HandlePublishedMessage;
            var clientId = Guid.NewGuid().ToString();

            client.Connect(clientId, settings.Username, settings.Password);

            client.Subscribe(new[] { "iot_grp10/accelerometer" }, new[] { MqttMsgBase.QOS_LEVEL_EXACTLY_ONCE });
        }

        static void HandlePublishedMessage(object sender, MqttMsgPublishEventArgs e)
        {
            var message = Encoding.UTF8.GetString(e.Message);
            // handle message received 
        }
    }
}
