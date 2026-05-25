---
type: deity
source-type: "Remaster"
domains: "Ambition, Nature, Plague, Tyranny"
favored-weapon: "Sickle"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Animal]], Rank 2: [[Entangling Flora]], Rank 5: [[Toxic Cloud]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Sicva, the Mistress of All, was one of the most vile and destructive gods of ancient Azlanti. Despite being raised by her virtuous parents, the deities Elion and Myr, Sicva grew up resentful of her father's shifting nature and her mother's commitment to charity. She set out to find ways to corrupt goodness and use that corruption for domination. She twisted her father's ability to see all sides of an argument into an affinity for manipulation of the mind, and her mother's penchant for charitable actions into an ability to oppress those of lesser means with a sickening smile. Sicva's cruelty doesn't stop at dominating civilized societies. She charges her followers to spread invasive species by bringing nonnative animals, plants, and viruses into new locations to destroy and corrupt precious ecosystems.

**Title** Mistress of All

**Areas of Concern** Domination, invasive species, oppression

**Edicts** Spread invasive species to new ecosystems, corrupt good ideals to promote domination and oppression, inspire duty and loyalty through coercion and fear

**Anathema** Support a rebellion, give freely expecting nothing in return, aid in ending a plague or infection

**Religious Symbol** virus

**Sacred Animal** beetle

**Sacred Colors** black

**Source:** `= this.source` (`= this.source-type`)
