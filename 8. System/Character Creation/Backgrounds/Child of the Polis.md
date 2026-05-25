---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Myth-Speaker Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're a longtime Kardaji Bay resident. Rather than explore distant lands, you've strengthened your connection to Iblydos, learning its little-known secrets and making friends in every port. You know the cadence and body language needed to set strangers at ease and communicate belonging, making it easy to track down deals and leads. Who needs wealth and glory when they can revel in Iblydos's eclectic culture? That said, if anything threatens the isles, you'll be ready to rally your neighbors and fight back.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in either the Diplomacy or Society skill, as well as the Lore skill associated with one Iblydan city-state (Pol-Bailax or Pol-Dhuraxilis is recommended). If you choose Diplomacy, you gain the [[Bargain Hunter]] skill feat. If you choose Society, you gain the [[Streetwise]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
