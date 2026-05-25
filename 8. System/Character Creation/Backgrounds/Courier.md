---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society"
feats: "[[Glean Contents]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

In your youth, you earned coin running messages for persons of wealth and influence, darting through crowded city streets. Your dogged commitment to deliver your message was good training for the life of an adventurer.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Society skill and the Lore skill for the city in which you were raised. You gain the [[Glean Contents]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
