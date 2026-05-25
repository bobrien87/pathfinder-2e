---
type: deity
source-type: "Remaster"
domains: "Change, Healing, Swarm, Water"
favored-weapon: "Trident"
divine-font: "Harm, Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Acidic Burst]], Rank 5: [[Control Water]], Rank 8: [[Monstrosity Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Oaur-Ooung is a massive, pale fungoid creature covered with blisters that endlessly give birth to more qlippoths, fueling their ranks for the war against demons. Some of her spawn drown within her impossibly deep oceanic realm and some she consumes upon birth, but countless others escape to the wider Outer Rifts. The Blistering Womb is also surrounded by smaller leviathans that can survive the toxic waters that protect her from demonic intrusions. Scholars believe that Cyth-V'sug, a qlippoth who became a demon lord, was spawned from one of her blisters. Most recently, she also gave birth to Nyuo-Ogh, one of the most recent qlippoth lords to rise.

**Title** The Blistering Womb

**Areas of Concern** Foul transformations, tainted oceans, vile fecundity

**Edicts** Embrace all manner of change, pollute pristine waters, practice fleshwarping on yourself and others

**Anathema** Allow yourself to remain static through fear of change, engage in efforts to stem overpopulation

**Religious Symbol** jellyfish-shaped rune

**Sacred Animal** none

**Sacred Colors** blue

**Source:** `= this.source` (`= this.source-type`)
