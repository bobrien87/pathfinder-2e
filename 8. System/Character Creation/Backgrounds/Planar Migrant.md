---
type: background
source-type: "Remaster"
boosts: "Con/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics"
feats: "[[Hefty Hauler]]"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Your birthplace was on one of the elemental planes, but you traveled to the Universe for some reason. Maybe you left on good terms, or maybe you were driven out and hope to one day return. Maybe you were even exiled, and any mention of it brings pain and resentment. In any case, nowhere has quite felt like home since, and you've roamed the land, carrying your life's possessions on your back wherever you go. You adventure possibly in search of a place to belong or a way to return to your plane of origin and settle unfinished business.

Choose two attribute boosts. One must be **Dexterity** or **Constitution**, and one is a free attribute boost.

You're trained in the Athletics skill and one of the following lore skills: Plane of Air Lore, Plane of Earth Lore, Plane of Fire Lore, Plane of Metal Lore, Plane of Water Lore, or Plane of Wood Lore. You gain the [[Hefty Hauler]] and [[Prescient Planner]] skill feats.

**Source:** `= this.source` (`= this.source-type`)
