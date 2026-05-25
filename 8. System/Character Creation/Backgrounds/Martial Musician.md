---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Performance, Warfare Lore Lore"
feats: "[[Impressive Performance]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Before you were old enough to join the actual fighting forces, you found your way onto the battlefield playing bagpipes, bugles, or drums. With these instruments of war, you helped direct troops in speed and direction, providing a pulsing cadence to push troops forward and keep them motivated.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You're trained in the Performance skill and the Warfare Lore skill. You gain the [[Impressive Performance]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
