---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation, Legal Lore Lore"
feats: "[[Intimidating Glare]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

An army marches on its stomach, and you have been on the forefront of ensuring your troops were properly fed and supplied. Through your logistical expertise, you understand that it can be vital to keep a tight fist around necessary supplies. And when soldiers ask for items without the proper clearance, you know how to turn them away with a withering look.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Legal Lore skill. You gain the [[Intimidating Glare]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
