using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace REST_API.Migrations
{
    public partial class addedmodels : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropPrimaryKey(
                name: "PK_Temperature",
                schema: "dbo",
                table: "Temperature");

            migrationBuilder.RenameTable(
                name: "Temperature",
                schema: "dbo",
                newName: "TemperatureReading",
                newSchema: "dbo");

            migrationBuilder.AddPrimaryKey(
                name: "PK_TemperatureReading",
                schema: "dbo",
                table: "TemperatureReading",
                column: "Id");

            migrationBuilder.CreateTable(
                name: "AccelerometerReading",
                schema: "dbo",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Timestamp = table.Column<DateTimeOffset>(type: "datetimeoffset", nullable: false),
                    Accelerometer = table.Column<double>(type: "float", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AccelerometerReading", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "AirpressureReading",
                schema: "dbo",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Timestamp = table.Column<DateTimeOffset>(type: "datetimeoffset", nullable: false),
                    Airpressure = table.Column<double>(type: "float", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AirpressureReading", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "HumidityReading",
                schema: "dbo",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Timestamp = table.Column<DateTimeOffset>(type: "datetimeoffset", nullable: false),
                    Humidity = table.Column<double>(type: "float", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_HumidityReading", x => x.Id);
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "AccelerometerReading",
                schema: "dbo");

            migrationBuilder.DropTable(
                name: "AirpressureReading",
                schema: "dbo");

            migrationBuilder.DropTable(
                name: "HumidityReading",
                schema: "dbo");

            migrationBuilder.DropPrimaryKey(
                name: "PK_TemperatureReading",
                schema: "dbo",
                table: "TemperatureReading");

            migrationBuilder.RenameTable(
                name: "TemperatureReading",
                schema: "dbo",
                newName: "Temperature",
                newSchema: "dbo");

            migrationBuilder.AddPrimaryKey(
                name: "PK_Temperature",
                schema: "dbo",
                table: "Temperature",
                column: "Id");
        }
    }
}
