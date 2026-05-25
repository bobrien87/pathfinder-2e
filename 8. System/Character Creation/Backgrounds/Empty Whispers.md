---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism, Planar Rift Lore Lore"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You knew someone once, and now you know only a life stitched together and healed over, nary even a scar remaining. You hear voices of souls that have fallen through the cracks of reality, creatures who have been removed from memory, banished planar entities, and similar. Their whispers guide you.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Occultism skill and the Planar Rift Lore skill. You get a Planar Rift Lore check to sense planar rifts, even if you aren't specifically Investigating or Searching for them, as well as locations where magic has been used to remove the memory of an object or creature from existence.

**Source:** `= this.source` (`= this.source-type`)
