using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Extensions.Logging;
using REST_API;

namespace IoT_REST_API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SensorController : ControllerBase
    {
        private readonly ILogger<SensorController> _logger;
        private readonly EFDataContext _context;

        public SensorController(ILogger<SensorController> logger, EFDataContext context)
        {
            _logger = logger;
            _context = context;
        }

        [HttpGet]
        [Route("Sensors")]
        public IEnumerable<Guid> GetAvailableSensors()
        {
            return _context.TemperatureReadings.Select(p => p.SensorId).Distinct();
        }
    }
}
