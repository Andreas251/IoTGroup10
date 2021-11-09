using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.Extensions.Logging;
using REST_API;
using REST_API.Models;
using System;
using IoT_REST_API.Extensions;
using System.Linq;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace IoT_REST_API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class AccelerometerController : ControllerBase
    {
        private readonly ILogger<AccelerometerController> _logger;
        private readonly EFDataContext _context;

        public AccelerometerController(ILogger<AccelerometerController> logger, EFDataContext context)
        {
            _logger = logger;
            _context = context;
        }


        [HttpGet]
        [Route("Latest")]
        public AccelerometerReading GetLatestReading()
        {
            return _context.AccelerometerReadings.OrderByDescending(p => p.Timestamp).FirstOrDefault();
        }

        [HttpGet]
        [Route("LatestBySensor")]
        public AccelerometerReading GetLatestReadingBySensor(Guid sensorId)
        {
            var reading = _context.AccelerometerReadings.Where(p => p.SensorId == sensorId).OrderByDescending(p => p.Timestamp).FirstOrDefault();
            return reading;
        }

        [HttpGet]
        [Route("ReadingsByTime")]
        public IEnumerable<AccelerometerReading> GetReadingsByTime(Guid? sensorId, DateTime start, DateTime end)
        {
            return _context.AccelerometerReadings.ReadingsWithinRange(sensorId, start, end);
        }
    }
}
