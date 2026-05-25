---
type: deity
source-type: "Remaster"
domains: "Lightning, Nature, Travel, Water"
favored-weapon: "Bola"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 3: [[Aqueous Orb]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The world flows too quickly, pushed into haste by innovation and technology. Civilizations rise and fall, bloodlines start and end, and even gods ascend and perish over time. The rapidity of life is distasteful to Hataam, who prefers the calmness of stagnant rivers and closed lakes. He often floats along murky waters as a mass of detritus and rotting limbs, leisurely watching for drownings and those who die of thirst.

**Title** The River Eater

**Areas of Concern** Drought, drowning, stagnation

**Edicts** Drown your enemies, refuse to change your mind in the light of new evidence, throw your body in the way of progress

**Anathema** Adopt new societal norms or innovations, save creatures from drowning

**Religious Symbol** driftwood floating on the surface of a stagnant pool

**Sacred Animal** eel

**Sacred Colors** blue, brown

**Source:** `= this.source` (`= this.source-type`)
