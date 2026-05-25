---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Deception, Fey Lore Lore"
feats: "[[Charming Liar]]"
source: "Pathfinder Wardens of Wildwood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Many grow up hearing cautionary tales of mischievous fey, and with good reason: from sprites' pranks to gremlins' sabotage to redcaps' outright lethality, fey pose a real danger to the unwary. But not for you—usually! Whether you grew up near an enchanted wilderness, have visited the First World, frequently deal with nature spirits, or even were a fey foundling raised by otherworldly beings, you're well acquainted with fey, their myriad traditions, and their even more numerous tricks. Fey and the Wildwood Lodge aren't the same thing, yet there's enough overlap that you're sure to fit in at the upcoming Greenwood Gala.

Choose two attribute boosts. One must be to **Charisma** or **Dexterity**, and one is a free attribute boost.

You're trained in the Deception skill and the Fey Lore skill. You gain the [[Charming Liar]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
