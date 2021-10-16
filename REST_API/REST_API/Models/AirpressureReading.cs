using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace REST_API.Models
{
    [Table("AirpressureReading", Schema = "dbo")]
    public class AirpressureReading
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        [Required]
        public DateTimeOffset Timestamp { get; set; }
        [Required]
        public double Airpressure { get; set; }
        
    }
}