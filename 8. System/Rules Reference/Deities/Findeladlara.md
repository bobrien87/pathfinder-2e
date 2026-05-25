---
type: deity
source-type: "Remaster"
domains: "Cities, Creation, Family, Star"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Temporary Tool]], Rank 4: [[Shape Stone]], Rank 7: [[Planar Palace]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Findeladlara is the ancient elven goddess of art and architecture, who teaches the value of preservation, art, buildings and, most importantly, life. She assumed the twilight portfolio to guide her most fervent worshippers to safety in the wake of Earthfall, after they remained on Golarion to build shelters in her name for the survivors of the cataclysm.

**Title** The Guiding Hand

**Areas of Concern** Architecture, art, twilight

**Edicts** Preserve elven art and architecture, bless and secure households, inspire and aid others with your works

**Anathema** Break the laws of hospitality, allow a guest to bring harm to your family

**Religious Symbol** finger pointing at gold star

**Sacred Animal** stag

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
