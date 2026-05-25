---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine, Herbalism Lore Lore"
feats: "[[Inoculation]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Plagues often spring from mass deaths and the vermin that multiply after such tragedies. Cities under siege can grow ill without proper nutrition and clean water. Your expertise with medicine allows you to help those afflicted by disease, and your view of the world is likely colored by seeing so much misfortune.

Choose two attribute boosts. One must be in **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Medicine skill and the Herbalism Lore skill. You gain the [[Inoculation]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
