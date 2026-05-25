---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Warfare Lore Lore"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You dedicated yourself to intense training and rigorous study to become a great warrior. The school you attended might have been a traditionalist monastery, an elite military academy, or the local branch of a prestigious mercenary organization.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in your choice of the Acrobatics or Athletics skill. You gain a skill feat: [[Cat Fall]] if you chose Acrobatics or [[Quick Jump]] if you chose Athletics. You're also trained in the Warfare Lore skill.

**Source:** `= this.source` (`= this.source-type`)
