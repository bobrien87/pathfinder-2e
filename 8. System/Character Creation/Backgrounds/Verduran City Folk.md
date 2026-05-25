---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Games Lore Lore"
source: "Pathfinder Wardens of Wildwood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You hail from one of the few large settlements in or around the Verduran Forest, such as Bellis or Wispil. It might be that you're part of these towns' timber operations or supporting industries, such as transporting supplies, overseeing operations, or serving as a remote bureaucrat who reports to a distant capital and enforces the Treaty of the Wildwood. Whatever the case, you're part of a scattered constellation of settlements that share cultural touchstones, including fey-inspired games like Prismati.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Society skill and the Games Lore skill. You gain either [[Multilingual]] or [[Streetwise]] as a skill feat.

**Source:** `= this.source` (`= this.source-type`)
