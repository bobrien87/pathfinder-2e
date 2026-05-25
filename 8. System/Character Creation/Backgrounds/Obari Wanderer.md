---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Sailing Lore Lore"
source: "Pathfinder Myth-Speaker Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

For millennia, the Obari Crossing has been the lifeblood of Iblydos's economy. You're no stranger to these waters, having traveled the route before and learned to feel the currents' pulse. Did you begin your career far to the west in the Impossible Lands before sailing in search of fortune? Perhaps your first voyage involved a hold full of Vudran spices, textiles, and artwork bound for Absalom's markets or beyond. You might have even grown up in Iblydos, learning to ply the Obari Ocean and guide incoming merchants past treacherous reefs. Whatever the case, you're at home at sea—a priceless boon in this scattered archipelago.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in either the Acrobatics or Survival skill, as well as the Sailing Lore skill. If you choose Acrobatics, you gain the [[Cat Fall]] skill feat. If you choose Survival, you gain the [[Terrain Expertise]] skill feat (aquatic or forest terrain is recommended).

**Source:** `= this.source` (`= this.source-type`)
