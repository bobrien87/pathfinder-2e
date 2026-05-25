---
type: deity
source-type: "Remaster"
divine-skill: "Arcana"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

These cultists believe undeath is the truest form of existence, and life is meant to be spent in preparation for transition to a more glorious unlife after death.

**Areas of Concern** undeath, lichdom, secrets

**Edicts** seek the perfection of undeath, cleanse the world of the living, master the magical secrets of life and death

**Anathema** speak the secrets of the Whispering Way above a whisper, write down the philosophies of the Whispering Way, act irrationally due to concerns for the living

**Source:** `= this.source` (`= this.source-type`)
