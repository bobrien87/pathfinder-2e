---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Vehicle Lore Lore"
feats: "[[Quick Repair]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

All vehicles eventually break down, from both wear and tear and through contact with the enemy, and someone needs to fix them. You have experience repairing air, land, and sea vehicles of all types, and you are knowledgeable about how they function and what specialized tools they require.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Crafting skill and the Vehicle Lore skill. You gain the [[Quick Repair]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
