---
type: background
source-type: "Remaster"
boosts: "Int/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Warfare Lore Lore"
feats: "[[Improvise Tool]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You've spent years rummaging through the corpses of armies and their equipment as soon as battles were won, seeking items from the dead that you can craft into something of value. While you've left that life behind, you've learned about warfare as well as how to create useful items from scavenged goods.

Choose two attribute boosts. One must be to **Strength** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and the Warfare Lore skill. You gain the [[Improvise Tool]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
