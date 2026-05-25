---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Mana Wastes Lore Lore"
feats: "[[Forager]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Whether you grew up in the Mana Wastes, the deserts of northern Garund, or another similarly desolate place, you quickly learned that only the strong survive. You and your family were forced to evade monsters, mutants, wild magic, and worse, as each new day heralded the possibility of a danger or threat you'd never seen before. You learned to adapt to the worst possible conditions and how to forage and survive in a place few others would dare to live.

Choose two attribute boosts. One boost must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill, and Mana Wastes Lore (or another similar Lore skill associated with the wastes where you grew up). You gain the [[Forager]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
