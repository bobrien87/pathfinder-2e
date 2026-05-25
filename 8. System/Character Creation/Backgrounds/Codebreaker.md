---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Cryptography Lore Lore"
feats: "[[Glean Contents]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Whether you're employed by a military organization to decipher coded messages sent by enemy factions or work independently to crack an enigma created by a past civilization, you have a head for patterns and linguistics. You might even use new clockwork devices to aid you in your efforts.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Society skill and the Cryptography Lore skill. You gain the [[Glean Contents]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
