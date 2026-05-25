---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Farming Lore Lore"
feats: "[[Forager]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You built your house using wood from the trees surrounding it. Raised it up from the dirt and called it home. You thought that it would be where you would grow old and die. But despite your best efforts, you were wrong. The land that once gave you food fell fallow, and dust took to the air and choked the livestock. Now you wander the world as an adventurer. Are you in search of a new place to settle down and try again, or have you become disillusioned by your old dreams, leading you to seek out a new purpose?

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Farming Lore skill. You gain the [[Forager]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
