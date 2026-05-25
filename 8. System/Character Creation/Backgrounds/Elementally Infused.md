---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You were exposed to a strong burst of elemental essence originating directly from an elemental plane, most likely caused by a planar breach. Your body absorbed the elemental essence with no ill effects, and now it coalesces within you. With time, you've learned to project elemental power in a manner safe to you but still deadly to others.

Choose two attribute boosts. One must be to **Constitution** or **Charisma**, and one is a free attribute boost.

Choose one elemental plane: Air, Earth, Fire, Metal, Water, or Wood. You are trained in the corresponding Lore skill: Plane of Air Lore, Plane of Earth Lore, Plane of Fire Lore, Plane of Metal Lore, Plane of Water Lore, or Plane of Wood Lore. You also gain a cantrip according to your chosen plane:

**Air:** [[Gale Blast]]

**Earth:** [[Scatter Scree]]

**Fire:** [[Ignition]]

**Metal:** [[Needle Darts]]

**Water:** [[Spout]]

**Wood:** [[Root Reading]]

You can cast this spell as a primal innate spell at will.

**Source:** `= this.source` (`= this.source-type`)
