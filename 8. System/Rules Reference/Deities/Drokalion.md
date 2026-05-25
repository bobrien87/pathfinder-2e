---
type: deity
source-type: "Remaster"
domains: "Family, Indulgence, Nature, Zeal"
favored-weapon: "Jaws, Pick"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Fleet Step]], Rank 2: [[Animal Form]], Rank 5: [[Chameleon Coat]]"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Hero-gods are supposed to have backstories, doctrines, myth-spoken origins, and even intelligible speech. Somehow, the lion known as Drokalion proved an exception. Though smarter than an average animal, Drokalion is nonetheless a fairly mundane lion with fairly mundane motivations, which seemingly includes no self-awareness of his hero-god status. Nevertheless, a hero-god he is. His small cult happily hunts along the periphery of Drokalion's territory and draws spellcasting from him, exulting in the no-nonsense lifestyle their unwitting patron teaches by example. Followers take special joy in Drokalion's attention, even though this attention almost always involves the lion charging at (and sometimes even eating) his faithful.

**Title** The Pridefather

**Areas of Concern** being a lion

**Edicts** embody a lion's hunting strategies, savor meat, be chased or eaten by Drokalion

**Anathema** back down from a fair challenge, cower to avoid harm, ruin Drokalion's hunt

**Religious Symbol** roaring lion

**Sacred Animal** lion

**Sacred Colors** brown, yellow

**Source:** `= this.source` (`= this.source-type`)
