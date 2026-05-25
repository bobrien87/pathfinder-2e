---
type: deity
source-type: "Remaster"
domains: "Earth, Family, Luck, Protection"
favored-weapon: "Mambele"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Sleep]], Rank 2: [[Laughing Fit]], Rank 3: [[Enthrall]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Bes is a member of the pantheon often worshiped in Ancient Osirion.

**Title** The Guardian Fool

**Areas of Concern** Households, luck, marriage, protection

**Edicts** Aid childbirths, spread joy and celebration, protect sleeping creatures

**Anathema** Harm or neglect a child, separate families, use magic to corrupt dreams

**Religious Symbol** bearded dwarf face

**Sacred Animal** lion

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
