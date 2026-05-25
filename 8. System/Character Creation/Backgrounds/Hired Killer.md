---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Stealth, Underworld Lore Lore"
feats: "[[Terrain Stalker]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Your life truly began after your first kill. Maybe you killed in self-defense, maybe it was a crime of passion, or maybe it was just an accident and you were a kid in the wrong place at the wrong time. In the end, the why doesn't matter. You got away with it. And then you found that maybe it didn't bother you as much as it should have. And maybe, just maybe, you had a talent you could use to forge a life for yourself. A blood-soaked talent and a blood-soaked life, sure. But it's yours.

Choose two attribute boosts. One boost must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in the Stealth skill and the Underworld Lore skill. You gain the [[Terrain Stalker]] skill feat, choosing a terrain appropriate for where you make your kills.

**Source:** `= this.source` (`= this.source-type`)
