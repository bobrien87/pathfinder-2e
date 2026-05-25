---
type: deity
source-type: "Remaster"
domains: "Creation, Nature, Protection, Wood"
favored-weapon: "Sickle"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Protector Tree]], Rank 2: [[Oaken Resilience]], Rank 6: [[Nature'S Reprisal]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Verilorn, Custodian of Oak and Ash, is the elemental lord of wood, cultivation, and forestry. He tends to his fields and gardens with exact precision, ensuring that every leaf and branch is of perfect size, shape, and position. While he once allowed his creations to grow with more abandon, incursions from the other elemental lords left Verilorn determined to create order and security, abandoning the green flexibility of his youth for the hardened bark of troubled wisdom. His creations now are physically perfect, but ideologically cold.

**Title** Custodian of Oak and Ash

**Areas of Concern** Cultivation, forestry, gardening, security, wood

**Edicts** Patiently plant your seeds, plan for orderly beauty, watch over your sproutlings

**Anathema** Abandon your post, neglect your crops, purposely pervert nature

**Religious Symbol** symmetrical germinating seed

**Sacred Animal** hedgehog

**Sacred Colors** brown, red

**Source:** `= this.source` (`= this.source-type`)
