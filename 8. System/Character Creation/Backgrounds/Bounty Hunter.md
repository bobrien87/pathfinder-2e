---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Legal Lore Lore"
feats: "[[Experienced Tracker]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Bringing in lawbreakers lined your pockets. Maybe you had an altruistic motive and sought to bring in criminals to make the streets safer, or maybe the coin was motivation enough. Your techniques for hunting down criminals transfer easily to the life of an adventurer.

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Legal Lore skill. You gain the [[Experienced Tracker]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
