using System.IO;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using REST_API.Models;

namespace REST_API
{
    public class EFDataContext : DbContext
    {
        public DbSet<TemperatureReading> TemperatureReadings { get; set; }
        public DbSet<HumidityReading> HumidityReadings { get; set; }
        public DbSet<AccelerometerReading> AccelerometerReadings { get; set; }
        public DbSet<AirpressureReading> AirpressureReadings { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                IConfigurationRoot configuration = new ConfigurationBuilder()
                    .SetBasePath(Directory.GetCurrentDirectory())
                    .AddJsonFile("appsettings.json")
                    .Build();
                var connectionString = configuration.GetConnectionString("SubscriptionDatabase");
                optionsBuilder.UseSqlServer(connectionString);
            }
        }
    }
}