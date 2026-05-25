---
type: deity
source-type: "Remaster"
domains: "Death, Duty, Truth, Vigil"
favored-weapon: "Greataxe"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Paralyze]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Weighted Swing

**Areas of Concern** Executions, judiciousness, responsibility

**Edicts** Perform just executions, study local laws, oppose corrupt or bloodthirsty government officials

**Anathema** Kill without thought, execute the innocent, mock the condemned, falsely incriminate another

**Religious Symbol** dove perched on axe

**Sacred Animal** dove

**Sacred Colors** gray, white

**Source:** `= this.source` (`= this.source-type`)
