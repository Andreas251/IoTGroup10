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
    public class HumidityController : ControllerBase
    {
        private readonly ILogger<HumidityController> _logger;
        private readonly EFDataContext _context;

        public HumidityController(ILogger<HumidityController> logger, EFDataContext context)
        {
            _logger = logger;
            _context = context;
        }

        [HttpGet]
        [Route("Latest")]
        public HumidityReading GetLatestReading()
        {
            return _context.HumidityReadings.OrderByDescending(p => p.Timestamp).FirstOrDefault();
        }

        [HttpGet]
        [Route("LatestBySensor")]
        public HumidityReading GetLatestReadingBySensor(Guid sensorId)
        {
            var reading = _context.HumidityReadings.Where(p => p.SensorId == sensorId).OrderByDescending(p => p.Timestamp).FirstOrDefault();
            return reading;
        }

        [HttpGet]
        [Route("ReadingsByTime")]
        public IEnumerable<HumidityReading> GetReadingsByTime(Guid? sensorId, DateTime start, DateTime end)
        {
            return _context.HumidityReadings.ReadingsWithinRange(sensorId, start, end);
        }
    }
}
