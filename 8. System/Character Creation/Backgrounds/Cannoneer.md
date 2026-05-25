---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Warfare Lore Lore"
feats: "[[Hefty Hauler]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You served as a crewmate aboard a military vessel or pirate ship and were responsible for the use and maintenance of the ship's cannons. A strong back and quick reflexes were equally important to you in your duties, and you know your way around explosives and the dangers that lie therein. These skills serve you well in your new life as an adventurer, as compared to the weight of a cannon, a gear load that makes your allies blanche just makes you laugh instead.

Choose two attribute boosts. One boost must be to **Dexterity** or **Strength**, and one is a free attribute boost.

You're trained in the Athletics skill and the Warfare Lore skill. You gain the [[Hefty Hauler]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
