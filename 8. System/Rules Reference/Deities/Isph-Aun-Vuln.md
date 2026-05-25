---
type: deity
source-type: "Remaster"
domains: "Air, Delirium, Plague, Trickery"
favored-weapon: "Longbow"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Goblin Pox]], Rank 5: [[Toxic Cloud]], Rank 7: [[Warp Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

When not within a mutated host body, Isph-Aun-Vuln manifests as an incorporeal mass of roiling tentacles arrayed around a toothy maw. However, few see this true form, as the Feaster Within uses subterfuge and other cunning methods to erode the free will of mortals. She works to remove their capacity for sin and, eventually, their lives. Isph-Aun-Vuln has a fascination with mortal religions as she sees many churches as the tools of other gods to control their followers. Unlike most other qlippoth lords, she actively seeks worshippers to exert her influence over.

**Title** The Feaster Within

**Areas of Concern** Infestations of the flesh, poisonous winds, removal of free will

**Edicts** Allow wounds to fester, be as changeable as the winds, present the illusion of choice while imposing your will

**Anathema** Cure someone of a disease, let those under your command make their own choices

**Religious Symbol** cloudy tentacled rune

**Sacred Animal** none

**Sacred Colors** gray

**Source:** `= this.source` (`= this.source-type`)
