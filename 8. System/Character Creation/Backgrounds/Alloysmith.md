---
type: background
source-type: "Remaster"
boosts: "Int/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Plane of Metal Lore Lore"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Blacksmithing might be an ancient profession, but you are its cutting edge. You've studied the properties of different metals, experimented with them by combining them, exposing them to different elements and processes, and have even delved into the metaphysical nature of metal in your quest to master it. You might have taken up adventuring to acquire more funding and materials or to test your designs.

Choose two attribute boosts. One must be to **Strength** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and the Plane of Metal Lore skill. You gain the [[Specialty Crafting]] skill feat with the blacksmithing specialty.

**Source:** `= this.source` (`= this.source-type`)
