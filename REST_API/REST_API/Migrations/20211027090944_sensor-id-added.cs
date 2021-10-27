using Microsoft.EntityFrameworkCore.Migrations;

namespace REST_API.Migrations
{
    public partial class sensoridadded : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<double>(
                name: "SensorId",
                schema: "dbo",
                table: "TemperatureReading",
                type: "float",
                nullable: false,
                defaultValue: 0.0);

            migrationBuilder.AddColumn<double>(
                name: "SensorId",
                schema: "dbo",
                table: "HumidityReading",
                type: "float",
                nullable: false,
                defaultValue: 0.0);

            migrationBuilder.AddColumn<double>(
                name: "SensorId",
                schema: "dbo",
                table: "AirpressureReading",
                type: "float",
                nullable: false,
                defaultValue: 0.0);

            migrationBuilder.AddColumn<double>(
                name: "SensorId",
                schema: "dbo",
                table: "AccelerometerReading",
                type: "float",
                nullable: false,
                defaultValue: 0.0);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "SensorId",
                schema: "dbo",
                table: "TemperatureReading");

            migrationBuilder.DropColumn(
                name: "SensorId",
                schema: "dbo",
                table: "HumidityReading");

            migrationBuilder.DropColumn(
                name: "SensorId",
                schema: "dbo",
                table: "AirpressureReading");

            migrationBuilder.DropColumn(
                name: "SensorId",
                schema: "dbo",
                table: "AccelerometerReading");
        }
    }
}
