---
type: background
source-type: "Remaster"
boosts: "Con/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation, Warfare Lore Lore"
feats: "[[Intimidating Glare]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

In your younger days, you waded into battle as a mercenary, a warrior defending a nomadic people, or a member of a militia or army. You might have wanted to break away from the regimented structure of these forces, or you could have always been as independent a warrior as you are now.

Choose two attribute boosts. One must be to **Strength** or **Constitution**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Warfare Lore skill. You gain the [[Intimidating Glare]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
