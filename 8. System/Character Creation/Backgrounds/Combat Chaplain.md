---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Religion"
feats: "[[Recognize Spell]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

As a member of the clergy, you have been responsible for tending to the spiritual and moral well-being of soldiers and their families. While you may have been a follower of a specific deity, you acted as an ambassador of the church overall, providing religious support in a religiously pluralistic and diverse setting. You provided counsel and took on the role of critical friend, mediator, and reconciler for those under your charge. You may have been called to lead worship, perform weddings, and conduct funerals in both nearby villages as well as remote locales.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You're trained in the Religion skill and the Lore skill associated with the deity you worship. You gain the [[Recognize Spell]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
