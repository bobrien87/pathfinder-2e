---
type: deity
source-type: "Remaster"
domains: "Duty, Repose, Soul, Vigil"
favored-weapon: "Staff"
divine-font: "Harm, Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Tailwind]], Rank 2: [[Embed Message]], Rank 3: [[Shadow Spy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Within every mortal heart is a rejection of death, an untamable desire to fight and live, and from this desperate impulse, Ceyannan the Shepherd was born. The usher rose from the troubled currents of the River of Souls to gather and guide the souls of the fallen into the afterlife. Fragments of the Shepherd remain in the hearts of all mortals, and for each soul guided across the river a missing piece returns to Ceyannan, bringing them closer to wholeness. They abhor when souls are displaced from the cycle, and whenever great, existential threats emerge against the cosmos, the usher of lost souls is there to contain them.

**Title** The Shepherd

**Areas of Concern** Final words, lost souls, searches

**Edicts** searches Attend the dying and hear their last words, uncover what is hidden or lost, destroy undead

**Anathema** Create undead, destroy or corrupt a soul, forget what you have lost

**Religious Symbol** two concentric circles bisected by a horizontal line

**Sacred Animal** tern

**Sacred Colors** white

**Source:** `= this.source` (`= this.source-type`)
