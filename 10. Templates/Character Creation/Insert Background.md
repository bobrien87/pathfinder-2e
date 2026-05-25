---
type: background
source-type: "{source-type}"
traits:
boosts: "{boosts}"
skills: "{skills}"
feats: "{feats}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, ", "), "")`
`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

{description}

**Source:** `= this.source` (`= this.source-type`)
