using System.Linq;
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

        public DataController(ILogger<DataController> logger)
        {
            _logger = logger;
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
