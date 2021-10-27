using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace REST_API.Models
{
    [Table("AccelerometerReading", Schema = "dbo")]
    public class AccelerometerReading
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        [Required]
        public DateTimeOffset Timestamp { get; set; }
        [Required]
        public double Accelerometer { get; set; }
        [Required]
        public double SensorId { get; set; }
        
    }
}