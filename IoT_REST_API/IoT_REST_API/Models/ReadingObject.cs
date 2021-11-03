using REST_API.Models;
using System.Collections.Generic;

namespace IoT_REST_API.Models
{
    public class ReadingObject
    {
        public IEnumerable<TemperatureReading> TemperatureReadings { get; set; }
        public IEnumerable<AirpressureReading> AirPressureReadings { get; set; }
        public IEnumerable<HumidityReading> HumidityReadings { get; set; }
        public IEnumerable<AccelerometerReading> AcceleroMeterReadings { get; set; }
    }
}
