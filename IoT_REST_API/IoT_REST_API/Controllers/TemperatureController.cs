using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using REST_API;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace IoT_REST_API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TemperatureController : ControllerBase
    {
        private readonly ILogger<TemperatureController> _logger;
        private readonly EFDataContext _context;

        public TemperatureController(ILogger<TemperatureController> logger, EFDataContext context)
        {
            _logger = logger;
            _context = context;
        }

        [HttpGet]
        [Route("Latest")]
        public double GetLatestTemperature(Guid sensorId)
        {
            var reading = _context.TemperatureReadings.Where(p => p.SensorId == sensorId).OrderByDescending(p => p.Timestamp).FirstOrDefault();
            _logger.LogInformation($"Latest temperature for sensorId {sensorId} requested, value is: {reading.Temperature}");
            return reading.Temperature;
        }
    }
}
