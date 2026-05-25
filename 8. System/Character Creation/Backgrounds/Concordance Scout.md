---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy"
feats: "[[Hobnobber]]"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You were hired by the Concordance of Elements to seek out rumors of planar breaches or other evidence of planar imbalances. After reporting back to the Concordance, they'd send agents more well equipped to deal with the situation. Still, this job has led you into more trouble than your employers suspect, and you've learned how to get your information quickly and get out relatively unscathed.

Choose two attribute boosts. One must be to **Constitution** or **Charisma**, and one is a free attribute boost.

You're trained in the Diplomacy skill and one of the following lore skills: Plane of Air Lore, Plane of Earth Lore, Plane of Fire Lore, Plane of Metal Lore, Plane of Water Lore, or Plane of Wood Lore. You gain the [[Hobnobber]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
