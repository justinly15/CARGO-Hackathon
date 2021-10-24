# 2021 Cargo Hackathon Technical Solution

Our submission for the hackathon is an applet that calculates the C02 emissions for a user's specific consumption. C02 is the most prevalent greenhouse gas and accounts for >95% of the transportation industry's impact on climate change.
By allowing a user to input the origin and destination of a product along with its mass, our program is able to give the C02 emissions produced by the transportation of that good in a variety of modes-- namely, air, ground, and rail transport.
We use a publicly-available API to find the straight-line distance between two points. For ground transport, this straight-line distance is multiplied by a scalar that accounts for the ratio of straight-line distance and travel distance (experimentally found to be ~1.4, see NIH source).
This distance value is then used in an equation to find the total emissions created by the transport of a product of a given mass that distance based on the efficiency of various modes of transport (see Green Freight Handbook source).
For example, the program could inform the user of the amount of C02 emissions produced by transporting a 10kg item from Boston to New York on a plane (or a train or a truck). 
We envision the audience of this tool to be environmentally-conscious consumers who will use it to understand how the modes of transport we use (via online shopping and general consumerism) can affect the emissions we are creating as a product.

The backend of our program is written in Python and deals with making the API call to find the distance between the origin and destination as well as crunching the numbers to determine the final output. The program is simple to use and has a front-facing GUI for better ease-of-use. 
TODO: Outline program and how it is used


Sources:
- https://storage.googleapis.com/scsc/Green%20Freight/EDF-Green-Freight-Handbook.pdf
- https://thepep.unece.org/sites/default/files/2017-06/Info_CO2_Methodological_Guide.pdf
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3835347/