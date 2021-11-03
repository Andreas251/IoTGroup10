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
    public class AirPressureController : ControllerBase
    {
        private readonly ILogger<AirPressureController> _logger;
        private readonly EFDataContext _context;

        public AirPressureController(ILogger<AirPressureController> logger, EFDataContext context)
        {
            _logger = logger;
            _context = context;
        }

        [HttpGet]
        [Route("Readings")]
        public IEnumerable<AirpressureReading> GetReadingsByTime(Guid? sensorId, DateTime start, DateTime end)
        {
            return _context.AirpressureReadings.ReadingsWithinRange(sensorId, start, end);
        }
    }
}
