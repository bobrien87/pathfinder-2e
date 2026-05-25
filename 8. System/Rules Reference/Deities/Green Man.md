---
type: deity
source-type: "Remaster"
domains: "Healing, Might, Nature, Protection"
favored-weapon: "Club"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 2: [[Entangling Flora]], Rank 6: [[Tangling Creepers]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Individual green men are lesser deities, capable of granting spells to those who worship them. Green men typically only allow intelligent plants—such as leshys—to be their clerics. If another creature proves to be a friend of plants, after a thorough personal vetting, a green man wholeheartedly accepts this strange fleshy worshipper into the fold. While individual green men have different edicts and anathema befitting their personalities, and some neutral good or neutral evil green men might have further changes, the following is a baseline most worshippers of green men follow.

**Title** Guide in the Grass

**Areas of Concern** Growth, nature, intelligent plants

**Edicts** Discover or create new forms of plant life, foster the growth and well-being of flora, preserve areas of natural wilderness

**Anathema** Allow flagrant abuse of plant life to go unpunished, damage natural environments, harm plant life except in the pursuit of saving greater plant life

**Religious Symbol** thick branch with thinner, leafy branches

**Sacred Animal** none

**Sacred Colors** green

**Source:** `= this.source` (`= this.source-type`)
