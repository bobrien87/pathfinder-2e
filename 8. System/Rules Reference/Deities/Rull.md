---
type: deity
source-type: "Remaster"
domains: "Air, Cold, Destruction, Lightning"
favored-weapon: "Falchion"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Thunderstrike]], Rank 3: [[Lightning Bolt]], Rank 6: [[Chain Lightning]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Shortly after orcs arrived on the surface of Golarion, it's said that Rull challenged thunder to a fight. He climbed a mountain peak during a thunderstorm and yelled out his Deathright to a spirit of lightning. He was struck by a tremendous bolt of lightning on the spot and died. During the ensuing Crucible, Rull claims to have won by consuming the lightning spirit he had challenged, and that it now lives within him and is under his control.

**Title** The Thunderer

**Areas of Concern** Lightning, storms, thunder

**Edicts** Create chaos at every opportunity, be loud wherever you go, spread fear and terror in Rull's name

**Anathema** Enforce law and order, show mercy, allow morals to impede the sowing of chaos

**Religious Symbol** thunder cloud and lightning

**Sacred Animal** terror bird

**Sacred Colors** green, yellow

**Source:** `= this.source` (`= this.source-type`)
