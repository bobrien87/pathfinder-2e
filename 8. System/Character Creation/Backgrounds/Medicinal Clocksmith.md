---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine, Engineering Lore Lore"
feats: "[[Risky Surgery]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

While others might have looked to clockwork as a mechanical innovation, you see the potential in the technology to improve the health of patients. You might be an experienced field medic who reached for a scrapped construct to help a wounded soldier, or a vanguard surgeon who's found replacing organs with clockwork more effective than repairing them. Perhaps you've also worked to "optimize" organic bodies with fine machinery, with or without the permission of your patients.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Medicine skill and the Engineering Lore skill. You gain the [[Risky Surgery]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
