---
type: deity
source-type: "Remaster"
domains: "Might, Nature, Pain, Zeal"
favored-weapon: "Spiked-gauntlet"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Draw Ire]], Rank 2: [[Slough Skin]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Faith in Urazra is relatively new, only coming about within the past few centuries. However, his following has grown rapidly among the young stone and marsh giants of a more violent incline. Even in the short amount of time that he has been a part of the giant pantheon, there have already been countless tales of his barbarity. In all of them, he is described as a blood-splattered stone giant man with a burly build, pauldrons fashioned from deer or moose skulls, and a jagged onyx-black greatsword with a length that rivals his height.

**Title** Breaker of Bones

**Areas of Concern** Battle, brutality, strength

**Edicts** Fight anyone who disrespects you, be in the front line of battle, fight to the death

**Anathema** Flee from battle, show mercy to your enemy, beg for mercy

**Religious Symbol** bear totem

**Sacred Animal** grizzly bear

**Sacred Colors** brown, red

**Source:** `= this.source` (`= this.source-type`)
