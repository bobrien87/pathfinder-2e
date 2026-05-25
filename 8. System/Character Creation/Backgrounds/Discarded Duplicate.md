---
type: background
source-type: "Remaster"
boosts: "Cha/Con/Dex/Int/Str/Wis, Cha/Con/Dex/Int/Str/Wis, Cha/Con/Dex/Int/Str/Wis"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Someone created you for a specific purpose. Some important person, be they a storied royal, a contentious politician, or a stark military leader, needed a body double for their most dangerous appearances. Using a mixture of fringe science and magic, you were commissioned and trained to emulate this person in every way, and have stood in for them in countless deadly circumstances. You may or may not know the reason behind your decommissioning, but whoever discarded you didn't finish you off. Now, the world is yours to explore—but "you" may have a bold or brutish reputation, or the individual you were duplicating may be long dead. Regardless of the fate of this individual, your way of life has changed drastically.

You and the GM can work out how to incorporate your previous life into your story. The GM can keep this knowledge [[Hidden]] even from you, or you or another character know what happened. You and the GM can also leave the information unspecified and fill it in later.

You gain three free attribute boosts. You choose two, and the GM chooses one based on the attributes of the character you were built to duplicate.

**Source:** `= this.source` (`= this.source-type`)
