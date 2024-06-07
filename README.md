# Sportsbook-Arbitrage-Detector

This Python script serves as a web scraper utilizing the LiveAPI to search for arbitrage opportunities between various sportsbooks, particularly focusing on the most popular ones in the U.S.

## How to Run
Executing this script is straightforward. You can run the file from the terminal using the following command:
```bash
python3 findArbitrage.py
```
Upon running the script, you'll interact with the output to choose which sports you want to search for arbitrage opportunities. The output prompts you as follows:

Hit 'y' to view americanfootball_cfl results or any other key to continue:

You can respond by typing 'y' followed by Enter to explore that sport or simply hit Enter to skip and move on to the next sport.

## Output Format
When searching for arbitrage opportunities in a specific sport, the output appears as follows:

Hit 'y' to view basketball_wnba results or any other key to continue: y

===basketball_wnba===

==New Game==

Caesars: 1.91(-109.8901098901099) + (Dallas Wings)

DraftKings: 2.14(+114.00000000000001) + (Los Angeles Sparks)

0.9908499290502519

==New Game==

Caesars: 1.91(-109.8901098901099) + (Las Vegas Aces)

DraftKings: 4.0(+300.0) + (Seattle Storm)

0.7735602094240838

==New Game==

## Interpretation
Each arbitrage opportunity is presented under a "New Game" header, followed by the respective lines for each sportsbook and the calculated score. A score below 1 indicates an arbitrage opportunity. For example:


Caesars: 1.91(-109.8901098901099) + (Dallas Wings)

DraftKings: 2.14(+114.00000000000001) + (Los Angeles Sparks)

0.9908499290502519

This suggests an arbitrage opportunity for the Dallas Wings vs. Los Angeles Sparks game. By betting on Dallas Wings to win at Caesars and Los Angeles Sparks at DraftKings, one can exploit the discrepancy in odds.


## Known Limitations
One known limitation is the occasional scenario where one sportsbook releases moneylines for a game before another, resulting in inaccurate calculations. This is detected when seeing unusually low scores, such as:


Caesars: 1.91(-109.8901098901099) + (Las Vegas Aces)

DraftKings: 4.0(+300.0) + (Seattle Storm)

0.7735602094240838

A score as low as 0.77 indicates that one sportsbook has not yet entered its moneyline for the game, leading to inaccuracies in the detected arbitrage opportunities.
