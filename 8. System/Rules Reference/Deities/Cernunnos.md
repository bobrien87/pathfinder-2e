---
type: deity
source-type: "Remaster"
domains: "Lightning, Nature, Passion, Zeal"
favored-weapon: "Longbow"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Animal Form]], Rank 3: [[Lightning Bolt]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Knowing that he is still one person despite his power, Cernunnos trains commanders and emissaries to fight evil in both the Material Plane and the First World. The faithful of Cernunnos are mainly intelligent plant creatures, fey, and mortal rangers and druids. Elves view him as patron of luck, while others pray to him for strength. Hidden groves, waterfalls and deep forests are sacred to Cernunnos.

**Title** The Horned Lord

**Areas of Concern** Fertility, seasons, wild animals

**Edicts** Protect forests and other natural areas, advocate for animals and plants, take and commit to decisive actions

**Anathema** Fail to strike down evil, enable the destruction of wilderness, needlessly kill animals

**Religious Symbol** stag with jeweled antlers

**Sacred Animal** stag

**Sacred Colors** brown, green

**Source:** `= this.source` (`= this.source-type`)
