---
type: deity
source-type: "Remaster"
domains: "Darkness, Family, Protection, Sorrow"
favored-weapon: "Light-mace"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 2: [[Umbral Extraction]], Rank 4: [[Aerial Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Mistress of the Mansion

**Areas of Concern** Mourning, night, protection of the dead

**Edicts** Mourn the dead and prepare them for burial, protect rightful rulers, assist childbirths, drink beer and celebrate

**Anathema** Mock the grieving, desecrate a corpse, refuse food to a child

**Religious Symbol** basket atop a palace

**Sacred Animal** kite

**Sacred Colors** amber, black

**Source:** `= this.source` (`= this.source-type`)
