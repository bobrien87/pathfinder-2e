---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting"
feats: "[[Crafter's Appraisal]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You live by the adage that one person's trash is another's treasure. Whether by sifting through scrap heaps or digging up old battlefields, you remain on the lookout for lost or discarded objects that you might be able to turn into something useful. More often than not, what you find is just junk, but you're convinced that one of these days, you're going to hit the jackpot. You've even taken up adventuring as a means to supercharge your access to all sorts of junk, gear, and loot.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and your choice of either the Engineering Lore or Mining Lore skill. You gain the [[Crafter's Appraisal]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
