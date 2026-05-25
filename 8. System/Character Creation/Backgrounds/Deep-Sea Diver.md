---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Plane of Water Lore Lore"
feats: "[[Underwater Marauder]]"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The sapphire depths of the seas and the mysteries they hold beneath their surface have always piqued your interest. Your obsession with the ocean depths cannot be contained to one world alone, and you've read tomes and journals about the source of all water, everywhere, hoping to one day understand the watery secrets of the great unknown.

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Athletics skill and the Plane of Water Lore skill. You gain the [[Underwater Marauder]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
