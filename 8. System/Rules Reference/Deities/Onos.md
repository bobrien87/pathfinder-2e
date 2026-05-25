---
type: deity
source-type: "Remaster"
domains: "Air, Earth, Fire, Water"
favored-weapon: "Chakram"
divine-font: "Harm, Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 3: [[One With Stone]], Rank 5: [[Elemental Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Onos was the Azlanti deity of elements, embassies, and extraplanar travel. Often difficult for mortals to fully understand, the God of Many Doors exists outside of any personality expected by a deity and speaks with its followers in direct and emotionless ways. Priests of Onos do their best to behave in a similar manner. Slow to anger and mild-mannered, priests of Onos often served as mediators in times of conflict.

**Title** God of Many Doors

**Areas of Concern** Elements, embassies, extraplanar travel

**Edicts** Mediate conflicts, respect each element equally, experience travel as often as possible

**Anathema** Act before weighing both sides, solve problems with aggression before negotiating, play favorites in negotiation

**Religious Symbol** swirling portal made of elements

**Sacred Animal** none

**Sacred Colors** none

**Source:** `= this.source` (`= this.source-type`)
