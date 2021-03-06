using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using IoT_REST_API.Interfaces;

namespace REST_API.Models
{
    public class HumidityReading : Reading
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        [Required]
        public DateTimeOffset Timestamp { get; set; }
        [Required]
        public double Humidity { get; set; }
        [Required]
        public Guid SensorId { get; set; }
    }
}