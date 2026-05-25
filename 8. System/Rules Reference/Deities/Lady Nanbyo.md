---
type: deity
source-type: "Remaster"
domains: "Destruction, Fire, Plague, Water"
favored-weapon: "Warhammer"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 5: [[Control Water]], Rank 6: [[Phantasmal Calamity]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Widow of Suffering

**Areas of Concern** Earthquakes, plagues, fire, suffering

**Edicts** Revel in destruction, make natural disasters worse, allow natural disasters to take their due

**Anathema** Allow a natural disaster to completely destroy a community or leave a group with no survivors

**Religious Symbol** Flaming rift in the earth

**Sacred Animal** crow

**Sacred Colors** gray, white

**Source:** `= this.source` (`= this.source-type`)
