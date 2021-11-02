using System;
using System.Linq;
using IoT_REST_API.Extensions;
using IoT_REST_API.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;

namespace REST_API.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class DataController : ControllerBase
    {
        private readonly ILogger<DataController> _logger;
        private readonly EFDataContext _context;

        public DataController(ILogger<DataController> logger, EFDataContext context)
        {
            _logger = logger;
            _context = context;
        }

        [HttpGet]
        [Route("Readings")]
        public ReadingObject GetReadingsByTime(Guid sensorId, DateTime start, DateTime end)
        {
            return new ReadingObject()
            {
                AcceleroMeterReadings = _context.AccelerometerReadings.ReadingsWithinRange(sensorId, start, end),
                AirPressureReadings = _context.AirpressureReadings.ReadingsWithinRange(sensorId, start, end),
                TemperatureReadings = _context.TemperatureReadings.ReadingsWithinRange(sensorId, start, end),
                HumidityReadings = _context.HumidityReadings.ReadingsWithinRange(sensorId, start, end)
            };
        }

        [HttpPost]
        [Route("injection")]
        public void accelerometerSqlInjection(string injection)
        {
            using (var context = new EFDataContext())
            {
                var x = context.AccelerometerReadings.FromSqlRaw(injection).ToList();
            }
        }
    }
}
