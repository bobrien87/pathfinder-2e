---
type: deity
source-type: "Remaster"
domains: "Destruction, Knowledge, Secrecy, Trickery"
favored-weapon: "Temple-sword"
divine-font: "Harm, Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Charm]], Rank 4: [[Honeyed Words]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Unsuspected Rot

**Areas of Concern** Discord, eclipses, secrets

**Edicts** Infiltrate righteous organizations and governments, destroy trust, perform human sacrifices

**Anathema** Betray a fellow servant of Dhalavei, harm those under Dhalavei's protection

**Religious Symbol** six arms forming a hexagon

**Sacred Animal** owl

**Sacred Colors** black, orange

**Source:** `= this.source` (`= this.source-type`)
