---
type: deity
source-type: "Remaster"
domains: "Ambition, Cities, Confidence, Might"
favored-weapon: "Warhammer"
divine-font: "Harm, Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Endure]], Rank 3: [[Enthrall]], Rank 7: [[Mask Of Terror]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Few mortals know that Grask was killed by assassins hired by his own faithful majordomo, Ardax the White Hair; fewer still understand that neither party sees this as a betrayal. Grask keenly sought a violent death specifically to swear his Deathright, while Ardax's unusually prophetic powers of foresight saw a future where Grask would swear the orcs to Tar-Baphon when the Whispering Tyrant returned. After being assassinated, Grask challenged the god Zagresh and won, becoming a god

**Title** The Uniter

**Areas of Concern** Discipline, power, prosperity

**Edicts** Improve the orcs' lot in life, obey the orcs above your station, rule the orcs below you with a strong hand

**Anathema** Allow orc-kind to become weak, intentionally make orcs look bad, disrupt your hierarchy without just cause

**Religious Symbol** grasping hand clutching a skull

**Sacred Animal** crocodile

**Sacred Colors** green, purple

**Source:** `= this.source` (`= this.source-type`)
