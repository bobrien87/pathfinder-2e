---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Tasked by the Concordance of Elements to research a variety of enigmatic planar phenomena, you've acquired very specific knowledge about the planes and the interactions between them. While being a researcher is usually a peaceful profession, the Concordance might require you to go out into the field and research unstable planar situations.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in four of the following: Plane of Air Lore, Plane of Earth Lore, Plane of Fire Lore, Plane of Metal Lore, Plane of Water Lore, or Plane of Wood Lore.

**Source:** `= this.source` (`= this.source-type`)
