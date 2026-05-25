---
type: deity
source-type: "Remaster"
domains: "Change, Destruction, Water, Zeal"
favored-weapon: "Trident"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 3: [[Feet To Fins]], Rank 6: [[Chain Lightning]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Dagon, the Shadow in the Sea, is the demon lord of aberrance, the ocean, and sea monsters. He holds court in an infinite ocean covered in disconcerting islands and deep-sea trenches filled with incomprehensible sunken cities. He appears as a massive creature with the lower body of an eel, a head reminiscent of deep-sea predators, and four thrashing tentacles in place of arms. Dagon began life as a qlippoth, and no mortal understands his transformation into a demon lord, though it earned him the enmity of his former kin. Dagon is primarily worshipped by boggards, sedacthies, and marsh giants, though desperate or depraved coastal villages have been known to pledge themselves to the demon lord.

**Title** The Shadow in the Sea

**Areas of Concern** Abberance, the sea, sea monsters

**Edicts** Swim underwater, improve your own strength, encourage the spread of dangerous sea monsters

**Anathema** Break a sworn oath, settle in a landlocked area, share Dagon's secrets with outsiders

**Religious Symbol** eye surrounded by runes

**Sacred Animal** fish

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
