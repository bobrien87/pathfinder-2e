---
type: background
source-type: "Remaster"
boosts: "Con/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Plane of Fire Lore Lore"
feats: "[[Breath Control]]"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Whether you fought against fires in the wilderness or in crowded city streets, you've had your fair share of dealing with uncontrolled flames. Battling thick smoke and toxic fumes, you've broken down obstacles to save trapped people from a fiery grave, and you've studied the nature and source of fire itself to try and better learn how to fight it.

Choose two attribute boosts. One must be to **Strength** or **Constitution**, and one is a free attribute boost.

You're trained in the Athletics skill and the Plane of Fire Lore skill. You gain the [[Breath Control]] feat.

**Source:** `= this.source` (`= this.source-type`)
