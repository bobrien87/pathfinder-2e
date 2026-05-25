---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Performance"
feats: "[[Virtuosic Performer]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

All you want to do is entertain the people, but sure enough, bad news seems to follow you. Gunfights, brawls, robberies, and more befall establishments you play at, and word is quick to spread. Keep one town ahead of the gossip, and you just might be able to play a gig, command a stage, or run a table again.

Choose two attribute boosts. One must be to **Charisma** or **Dexterity**, and one is a free attribute boost.

You're trained in the Performance skill and a lore skill of your choice. You gain the [[Virtuosic Performer]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
