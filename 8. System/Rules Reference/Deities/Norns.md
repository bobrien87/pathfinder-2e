---
type: deity
source-type: "Remaster"
domains: "Family, Fate, Knowledge, Truth"
favored-weapon: "Shears"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Mindlink]], Rank 2: [[Web]], Rank 4: [[Clairvoyance]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Followers of Fate

**Areas of Concern** Aging, destiny, fate

**Edicts** Make predictions of the future, offer advice and guidance to those in positions of power, provide comfort to the elderly

**Anathema** Apologize for making an incorrect prediction, disrespect mothers, accept payment for fortune-telling

**Religious Symbol** shears cutting a golden thread

**Sacred Animal** spider

**Sacred Colors** gold

**Source:** `= this.source` (`= this.source-type`)
