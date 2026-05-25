---
type: background
source-type: "Remaster"
boosts: "Con/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Stealth, Underworld Lore Lore"
feats: "[[Experienced Smuggler]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have been imprisoned or punished for crimes (whether you were guilty or not). Now that your sentence has ended or you've escaped, you take full advantage of the newfound freedom of your adventuring life.

Choose two attribute boosts. One must be to **Strength** or **Constitution**, and one is a free attribute boost.

You're trained in the Stealth skill and the Underworld Lore skill. You gain the [[Experienced Smuggler]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
