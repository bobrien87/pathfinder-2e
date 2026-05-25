---
type: deity
source-type: "Remaster"
domains: "Protection, Travel, Water, Zeal"
favored-weapon: "Light-mace"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 2: [[Animal Form]], Rank 4: [[Reflective Scales]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Green Empress

**Areas of Concern** Good serpents, the River Sphinx, wisdom

**Edicts** Defend your homelands and your people, aid childbirths, grow papyrus, protect sources of clean water

**Anathema** Refuse to help a drowning creature, harm a rightful ruler

**Religious Symbol** Uraeus

**Sacred Animal** Uraeus

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
