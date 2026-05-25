---
type: deity
source-type: "Remaster"
domains: "Earth, Family, Protection, Repose"
favored-weapon: "Longspear"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Sleep]], Rank 4: [[Shape Stone]], Rank 7: [[Planar Palace]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

According to the Mizravratta Brahmodya, in the days when Golarion had not yet finished forming, the god Vudravati wandered across the still-changing landscapes, breathing her joy and wonder into creation. Twin brothers, the gods Embaral and Obari, fell in love with her and both wished to please her. She loved them both and rejoiced in their company. But the brothers, unable to understand her boundless generosity, grew jealous, each wanting to control her love. They tried to force Vudravati into choosing between them, but she refused. Turning to violence, each brother then reasoned that, by destroying his twin, he would at last have all of Vudravati's love for himself. An epic battle began that threatened to reshape the nascent world as the brothers toppled mountains, tore open vast canyons, and raised hurricanes, all in the hopes of destroying the other.

**Title** The Peaceful Mother

**Areas of Concern** hospitality, community, nature, diplomatic resolutions

**Edicts** be generous and forgiving, show respect for all beings and for nature, work to build peaceful communities

**Anathema** destroy natural coastlines, sow division through lies or rumors, stoke enmity between rivals

**Religious Symbol** necklace of beads

**Sacred Animal** python

**Sacred Colors** green, blue, brown

**Source:** `= this.source` (`= this.source-type`)
