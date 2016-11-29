## US Election by County Distance

It is a known fact that Republicans are get more votes in the country regions whether Democrats have bigger influence at the big cities. I got curious to see if this assumption also appeared on the last presidential election between Clinton and Trump. 
To confirm that, I decided to compare the distance of a county from big counties to its percentage of vote on Trump (big county == densely populated county). If the previous assumption is correct, I expect to have lower Trump vote rate on counties with short distances from a big county and red counties far from the centers. 
Here is what I’ve got, ([You can find an interactive version here](https://public.tableau.com/profile/joao.carabetta#!/vizhome/USElectionDistance/Dashboard1))

![](https://github.com/JoaoCarabetta/US_Election_Analysis/blob/master/images/Screen%20Shot%202016-11-29%20at%2012.56.43.png)


in which you can see that counties with more than one million inhabitants tend to vote for Hillary, whereas scarcely populated counties from the country side massively vote Trump. 
Counties with up to 25% of Trump votes can be assumed as heavily democrats. These counties include the two biggest counties in total of votes, Los Angeles County CA and Cook County IL. Also, there are few counties far from the a big county that  appear to have a big population, which indicates that they are central counties on its states. On the other hand, heavily republican counties (more than 75% vote percentage on Trump) are tiny and far from a big county. 


The central parts, also tell a story. The range between 25–50% on Trump preference contains most of the biggest cities on US, which can be noted by the amount of bigger circles. The 50–75% is quite similar to the top Trumpers, tiny counties on the country side.
Overall, this viz confirms the assumption that the country side is red and the democrats are heavily concentrated on big centers. 


---

If you want to make the graph yourself, or explore it even further, get the data/final/county_all.csv file with all this info.

The election results come from www.politico.com
