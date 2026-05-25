---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Scribing Lore Lore"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You make a living out of reading and writing letters for people who are eager to keep in touch with their loved ones over long distances. Many of these people are semiliterate and can't afford magical communication, such as sending or dream message spells. You aren't always fluent in the many disparate languages you're asked to record, but with your many books and dictionaries, you get by. Your services are important to the community, despite your craft being a rarity

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in Scribing Lore. You gain one skill feat of your choice between the Specialty Crafting or Multilingual skill feat. During your daily preparations, you can choose one additional language that you know. You can change this language the next time you make your daily preparations.

**Source:** `= this.source` (`= this.source-type`)
