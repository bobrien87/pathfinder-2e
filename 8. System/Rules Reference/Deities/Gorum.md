---
type: deity
source-type: "Remaster"
domains: "Confidence, Destruction, Might, Zeal"
favored-weapon: "Greatsword"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Enlarge]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Anyone who seeks glory on the battlefield calls out prayers to Our Lord in Iron. Gorum emphasizes might, encouraging his followers to seek out war and combat as the ultimate way to worship him

**Title** Our Lord in Iron

**Areas of Concern** Battle, strength, weapons

**Edicts** Attain victory in fair combat, push your limits, wear armor in combat

**Anathema** Kill prisoners or surrendering foes, prevent conflict through negotiation, win a battle through underhanded tactics or indirect magic

**Religious Symbol** sword in mountain

**Sacred Animal** rhinoceros

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
