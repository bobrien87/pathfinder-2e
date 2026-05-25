---
type: deity
source-type: "Remaster"
domains: "Indulgence, Might, Nature, Trickery"
favored-weapon: "Bo-staff"
divine-font: "Harm, Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Jump]], Rank 3: [[Mad Monkeys]], Rank 4: [[Creation]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Monkey King

**Areas of Concern** Drunkenness, nature, trickery

**Edicts** Live life freely, drink, play pranks

**Anathema** Refuse a reasonable bet or duel, let social pressure change your behavior

**Religious Symbol** stone monkey

**Sacred Animal** monkey

**Sacred Colors** gray, gold

**Source:** `= this.source` (`= this.source-type`)
