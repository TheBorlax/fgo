# fgo
Fate GO roll calc
Calculator to see your odds on getting a specific rate up.

Use core.distributeBuiltIn(core, numberOfRolls, precentChance, NPx, showDistributionCurve) method in rolls.py

For example:

core.distributeBuiltIn(core, 128, 0.015, 5, False)

checks for 128 rolls at 1.5% chance per roll, NP5 or higher,
do not show distribution curve
