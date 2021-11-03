using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.Extensions.Logging;
using REST_API;
using REST_API.Models;
using System;
using IoT_REST_API.Extensions;

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
        [Route("Readings")]
        public IEnumerable<AccelerometerReading> GetReadingsByTime(Guid? sensorId, DateTime start, DateTime end)
        {
            return _context.AccelerometerReadings.ReadingsWithinRange(sensorId, start, end);
        }
    }
}
