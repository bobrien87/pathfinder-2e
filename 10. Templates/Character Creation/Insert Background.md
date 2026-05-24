---
type: background
source-type: "{source-type}"
traits: "{traits}"
boosts: "{boosts}"
skills: "{skills}"
feats: "{feats}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

`= choice(this.boosts != null, "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null, choice(this.boosts != null, "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null, choice(this.boosts != null or this.skills != null, "<br>", "") + "**Gained Feat** " + this.feats, "")`

***

{description}

**Source:** `= this.source` (`= this.source-type`)
