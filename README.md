# 2021 CARGO Hackathon Technical Solution

Our submission for the hackathon is a GUI and a command line tool that calculates the CO2 emissions associated with the transport of a specific product, specified by the user. CO2 is the most prevalent greenhouse gas and accounts for >95% of the transportation industry's impact on climate change. By allowing a user to input the origin and destination of a product along with its mass, our program is able to determine the CO2 emissions produced by the transportation of that good in a variety of modes-- namely, air, ground, and rail transport.

We use a publicly-available API to find the straight-line distance between two points. For ground transport, this straight-line distance is multiplied by a scalar that accounts for the ratio of straight-line distance and travel distance. This distance value is then used to find the total emissions created by the transport of a product of a given mass that distance based on the efficiency of various modes of transport (see Green Freight Handbook source).

Our program is written in Python and deals with making the API call to find the distance between the origin and destination as well as crunching the numbers to determine the total CO2 emissions produced. A user specifies an origin and a destination (within the same country) as well as the mass of the cargo. Our program uses a number of experimentally-derived values for transport efficiency to calculate the CO2 emissions associated with the transportation of that cargo. 

The aim of our program is to provide a more individualistic view of the relationship between consumerism and greenhouse gas emissions. While data exists on the GHG emissions of entire sectors, these numbers are often staggering (with emissions being measured in the millions of tons). By tailoring our application to individual users rather than companies, we hope to provide a more personal insight into the GHG emissions associated with one's consumerism.

How to use:
To use the program, download the files, navigate to the CARGO-Hackathon folder in a terminal and run the program as such: 'python3 main.py '<origin>' '<destination>' '<mode {air, rail, ground}>' '<mass in kg (optional, dafults to 1)>'' (for example: python3 main.py 'Boston' 'Providence' 'rail' '10'). Output is given as grams of CO2 produced by transporting the cargo between the given locations.


Sources:
- https://storage.googleapis.com/scsc/Green%20Freight/EDF-Green-Freight-Handbook.pdf
- https://thepep.unece.org/sites/default/files/2017-06/Info_CO2_Methodological_Guide.pdf
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3835347/ 
  
  


https://user-images.githubusercontent.com/92478707/140549268-aa9f6ce3-ed58-4f24-bf78-44081a96e033.mp4

