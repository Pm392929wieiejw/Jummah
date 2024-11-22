import requests

# Your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1309427185559535686/yIszQfDJbwXbjEy9i12KU45d5srlv7G-uvtWWIoofD9u00V-XGFcAkZ3S7gq21HHQvji"

# Jummah Reminder Content
message = {
    "content": "@everyone",
    "embeds": [
        {
            "title": "📢 Friday Jummah Announcement",
            "description": (
                "**🕌 Assalamu Alaikum Wa Rahmatullahi Wa Barakatuh, dear brothers and sisters!**\n\n"
                "✨ Alhamdulillah, another blessed **Friday** has arrived, the best day of the week in Islam. "
                "Let us take this opportunity to strengthen our faith and increase in worship.\n\n"
                "📖 **Allah (SWT) says in the Qur'an:**\n"
                "*“O you who have believed, when [the adhan] is called for the prayer on the day of Jumu'ah [Friday], "
                "then proceed to the remembrance of Allah and leave business. That is better for you, if you only knew.”*\n"
                "*(Surah Al-Jumu'ah, 62:9)*\n\n"
                "🤲 **Hadith of the Prophet ﷺ:**\n"
                "- *\"The best day on which the sun rises is Friday; on it, Adam was created, on it, he was made to enter "
                "Paradise, on it, he was expelled from it, and the Last Hour will take place on no day other than Friday.\"*\n"
                "*(Sahih Muslim: 854)*\n\n"
                "💡 **Reminders for this blessed day:**\n"
                "1. **Recite Surah Al-Kahf** – It is a sunnah of the Prophet ﷺ and brings immense blessings.\n"
                "2. **Increase in sending salawat upon the Prophet ﷺ.**\n"
                "3. **Attend the Jummah prayer** with full focus and sincerity.\n"
                "4. **Make dua**, as there is a special hour on Friday in which duas are accepted.\n"
                "5. **Reflect on your deeds and seek forgiveness from Allah (SWT).**\n\n"
                "Let us make the most of this sacred day by drawing closer to Allah and strengthening our bonds with "
                "one another. May Allah (SWT) grant us His mercy and forgiveness on this blessed day.\n\n"
                "📌 **Don’t forget to remind your family and friends!**"
            ),
            "color": 5814783  # Blue color
        }
    ]
}

# Send the reminder
response = requests.post(WEBHOOK_URL, json=message)
if response.status_code == 204:
    print("Reminder sent successfully!")
else:
    print(f"Failed to send reminder. Status code: {response.status_code}")
  
