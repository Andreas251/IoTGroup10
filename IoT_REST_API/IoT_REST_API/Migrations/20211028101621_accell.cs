using Microsoft.EntityFrameworkCore.Migrations;

namespace IoT_REST_API.Migrations
{
    public partial class accell : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "Accelerometer",
                table: "AccelerometerReadings",
                newName: "Z");

            migrationBuilder.AddColumn<double>(
                name: "X",
                table: "AccelerometerReadings",
                type: "float",
                nullable: false,
                defaultValue: 0.0);

            migrationBuilder.AddColumn<double>(
                name: "Y",
                table: "AccelerometerReadings",
                type: "float",
                nullable: false,
                defaultValue: 0.0);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "X",
                table: "AccelerometerReadings");

            migrationBuilder.DropColumn(
                name: "Y",
                table: "AccelerometerReadings");

            migrationBuilder.RenameColumn(
                name: "Z",
                table: "AccelerometerReadings",
                newName: "Accelerometer");
        }
    }
}
