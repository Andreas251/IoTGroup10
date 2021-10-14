using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace REST_API.Models
{
    [Table("TemperatureReading", Schema = "dbo")]
    public class TemperatureReading
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        [Required]
        public DateTimeOffset Timestamp { get; set; }
        [Required]
        public double Temperature { get; set; }
        
    }
}