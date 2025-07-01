import logging
import os
import schedule
import time
import requests
import feedparser
from telegram import Bot, ParseMode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
channel = os.getenv("CHANNEL_USERNAME")

def post_sports_news():
    feed = feedparser.parse("http://www.espn.com/espn/rss/news")
    if feed.entries:
        top = feed.entries[0]
        message = f"📰 *{top.title}*
{top.link}"
        bot.send_message(chat_id=channel, text=message, parse_mode=ParseMode.MARKDOWN)

def post_football_scores():
    bot.send_message(chat_id=channel, text="⚽ Sample Football Score: Man City 2 - 1 Real Madrid")

def post_betting_odds():
    message = (
        "💰 Betting Odds (Sample):

"
        "Match: PSG vs Bayern
Odds: PSG 2.10 | Draw 3.50 | Bayern 3.00

"
        "Bet here:
"
        "[Stake](https://stake.com/?c=xjXOVUk8)
"
        "[1xBet](https://1xbet.ng?bf=63eac89802907_2136044107)
"
        "[Paripesa](https://paripesa.ng?bf=6864326fd88bf_11377051151)"
    )
    bot.send_message(chat_id=channel, text=message, parse_mode=ParseMode.MARKDOWN)

def run_bot():
    schedule.every(2).minutes.do(post_football_scores)
    schedule.every(30).minutes.do(post_sports_news)
    schedule.every(2).hours.do(post_betting_odds)

    logger.info("BallRadar bot is live.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_bot()
