---
type: background
source-type: "Remaster"
boosts: "Con/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Underworld Lore Lore"
feats: "[[Streetwise]]"
source: "Pathfinder Hellbreakers Player’s Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You hail from Cheliax but no longer call it home, having rejected its tyranny and hellish oppression. Yet the traces of your old home linger in your place of refuge, tainting it with violence and injustice. Now you must do in Isger what you couldn't in Cheliax—take up arms and cut out all traces of Abrogail Thrune's influence.

Choose two attribute boosts. One must be to **Constitution** or **Intelligence**, and one is a free attribute boost.

You're trained in the Society skill and the Underworld Lore skill. You gain the [[Streetwise]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
