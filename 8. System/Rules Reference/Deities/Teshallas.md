---
type: deity
source-type: "Remaster"
domains: "Death, Decay, Healing, Vigil"
favored-weapon: "Chakram"
divine-font: "Harm, Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Spider Sting]], Rank 3: [[Envenom Companion]], Rank 7: [[Corrosive Body]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

When the Universe was young, Pharasma watched mortals as they lived, and when their day arrived, she saw mortality's love for life push them to defy the cycle and refuse death. Pharasma raised up an asp, reshaping them into a new psychopomp usher whose venom—age—would flow through all mortal veins, draining away their memories, their passions, and their vitality, until, when their time comes to its close, they are ready for death's embrace.

**Title** The Primordial Poison

**Areas of Concern** Aging, poison, venomous creatures

**Edicts** Embrace old age, grow or tend poisonous plants, learn from your experiences, respect the wisdom of the elderly, use poisons

**Anathema** Cling to the past, needlessly kill venomous creatures, poison someone you didn't intend to

**Religious Symbol** circle pierced by two vertical lines

**Sacred Animal** venemous snake

**Sacred Colors** yellow

**Source:** `= this.source` (`= this.source-type`)
