---
type: background
source-type: "Remaster"
boosts: "Int/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Engineering Lore Lore"
feats: "[[Quick Repair]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The intricate inner workings of machines are no stranger to you. Whether they are mundane devices or complex clockworks, you know what makes them tick and how to maintain them. An adventuring group might keep you around to repair their equipment, or you might travel around to offer your rare services to those in need—for a price, of course!

Choose two attribute boosts. One must be to **Strength** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and the Engineering Lore skill. You gain the [[Quick Repair]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
