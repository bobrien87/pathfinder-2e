---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Mercantile Lore Lore"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You delight in making little trinkets for children of all ages, and seeing their faces light up thanks to one of your creations brings joy to your heart. Perhaps you sell your wares from a particular shop or from the back of a wagon as you travel from town to town.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in the Crafting skill and the Mercantile Lore skill. You gain the [[Specialty Crafting]] skill feat, choosing Artistry, Blacksmithing, Glassmaking, Leatherworking, Tailoring, or Woodworking as your specialty.

**Source:** `= this.source` (`= this.source-type`)
