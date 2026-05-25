---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Acrobatics, Plane of Air Lore Lore"
feats: "[[Cat Fall]]"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The freedom of a bird in flight is something to envy, and envy it you did, but not for long. You've borrowed mechanical gliders or sought out the benefits of magically aided gliding and flight, doing anything for an opportunity to look down on the world with only the wind to keep you aloft. The expense of these experiences may have been a notable factor in why you undertook the adventuring lifestyle or perhaps you are seeking new methods of flight to master.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in the Acrobatics skill and the Plane of Air Lore skill. You gain the [[Cat Fall]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
