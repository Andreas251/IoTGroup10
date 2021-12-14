
# Course: Internet Of Things Technology - Fall 2021

**Group**: 10

**Group members/developers/authors**: 
*Andreas Larsen Engholm, Andreas Vorgaard, Jesper Strøm, Simon Zacher Høholt Jensen and Tobias Sandø Lund*

# Step-by-step guide to setting up the system
1. Transfer the code from the Raspberry folder to the Raspberry Pi
2. Prepare one or more local computers for running the database, API and Vizualiser (The Database and API **has to** run on the same computer)
3. Use EF Core to migrate the database contained within the */IoT_REST_API/IoT_REST_API* folder
    1. This can be done via the following command in the command prompt, if .NET EF Core CLI is installed 

            dotnet ef database update

    2. The command prompt will output "***Done***" when finished creating the database. The prompt can sometimes freeze here, if that happens then just close the prompt since we no longer need it.
4. Run the REST API solution (File: *\IoT_REST_API\IoT_REST_API.sln*), e.g. via Visual Studio 2019.
5. Run the Raspberry Pi with code transferred in *step 1*, with command "python3 WeatherStation.py"
7. Run the Visualizer with Python version >=3.7.4 (File: *\Visualizer\Visualizer.py*)
8. If all of these previous steps have been done, then the Visualizer.py that was just opened should be outputting the measured data with 1 minute intervals. For faster intervals, you need to go in and change the settings in the code transfered to the Raspberry Pi from the Raspberry folder. For a faster live data update the intervals in the Matplotlib Animator should also be changed to match the half of what the interval of the RPI is set to. 
