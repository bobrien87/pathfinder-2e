---
type: deity
source-type: "Remaster"
domains: "Change, Healing, Nature, Soul"
favored-weapon: "Flail"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Soothe]], Rank 2: [[False Vitality]], Rank 6: [[Tangling Creepers]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Lord of the Living

**Areas of Concern** Afterlife, fertility, rebirth, resurrection

**Edicts** Ensure the health of crops and vegetation, protect the bodies and souls of the worthy dead, avenge the wrongly murdered

**Anathema** Dismember a creature, desecrate a corpse, show ingratitude for a sincere gift

**Religious Symbol** crook and flail

**Sacred Animal** ram

**Sacred Colors** green, white

**Source:** `= this.source` (`= this.source-type`)
