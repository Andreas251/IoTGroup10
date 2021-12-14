using System;

namespace IoT_REST_API.Interfaces
{
    public interface Reading
    {
        public Guid SensorId { get; set; }
        public DateTimeOffset Timestamp { get; set; }
    }
}
