---
type: deity
source-type: "Remaster"
domains: "Cities, Family, Travel"
favored-weapon: "Longbow"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Tailwind]], Rank 3: [[Cozy Cabin]], Rank 7: [[Momentary Recovery]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Elion, the Farseeker, is the Azlanti god of discovery, exploration, and settlers. It's most important to note that while Elion promotes exploration, he only promotes the settlement of unoccupied lands. He takes great offense when explorers destroy or claim inhabited regions in his name.

**Title** The Farseeker

**Areas of Concern** Discovery, exploration, settlers

**Edicts** Explore and seek new locations, respect and learn from new cultures, share and bargain with others

**Anathema** Claim ownership of inhabited land, spread disease and infection, destroy natural habitats

**Religious Symbol** compass

**Sacred Animal** monarch butterfly

**Sacred Colors** sea green and sky blue

**Source:** `= this.source` (`= this.source-type`)
