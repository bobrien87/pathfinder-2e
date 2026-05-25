---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Religion, Devil Lore Lore"
feats: "[[Student of the Canon]]"
source: "Pathfinder Hellbreakers Player’s Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You once worshipped a powerful archdevil, but have turned away from fiendish practices. Whether you walked away due to moral compunctions or cold pragmatism, you know your soul was once bound for Hell, and you can only pray that your new path erases the sins you've committed.

Choose two attribute boosts. One must be to **Charisma** or **Intelligence**, and one is a free attribute boost.

You're trained in the Religion skill and the Devil Lore skill. You gain the [[Student of the Canon]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
