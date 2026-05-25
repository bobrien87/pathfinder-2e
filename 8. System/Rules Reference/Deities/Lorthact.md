---
type: deity
source-type: "Remaster"
domains: "Magic, Time, Trickery, Tyranny"
favored-weapon: "Staff"
divine-font: "Harm"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Force Barrage]], Rank 3: [[Slow]], Rank 6: [[Never Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Lorthact's cult is incredibly small. Even in his reduced state, he can still grant spells to his few remaining clerics. His symbol is a staff wrapped in scrolls.

**Title** The Unraveler

**Areas of Concern** Exiles, scholars, theories

**Edicts** Learn arcane secrets, take from others what you cannot make yourself, rule from the shadows

**Anathema** Reveal your actual identity, share power with the weak

**Religious Symbol** Staff wrapped in scrolls

**Sacred Animal** chameleon

**Sacred Colors** blue, red

**Source:** `= this.source` (`= this.source-type`)
