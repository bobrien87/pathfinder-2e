---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Island Lore Lore"
feats: "[[Survey Wildlife]]"
source: "Pathfinder Shades of Blood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Talmandor's Bounty's first year was fraught with hardship and peril, and many of the original settlers—including your parents—returned to the mainland at the earliest opportunity. However, you have nothing but fond memories of your time on Ancorato! Your carefree days in the colony were spent climbing trees, picking berries, and wondering at the island's natural splendor. You might even fondly remember some of the original settlers from that time who are still in town. Now that you're grown, you've returned to the colony to recapture that childhood magic (and hopefully avoid the dangers that forced your family to leave the island in the first place).

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Island Lore skill. You gain the [[Survey Wildlife]] skill feat.

In addition, work with your GM to select one business in town. You have a connection to the owner or someone who works there and get a 10% discount on goods and services from that establishment.

**Source:** `= this.source` (`= this.source-type`)
