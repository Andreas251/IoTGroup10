using System;

namespace REST_API.Models
{
    public class Measurement
    {
        public Guid sensorId { get; set; }
        public string timestamp { get; set; }
        public dynamic value { get; set; }
    }
}
