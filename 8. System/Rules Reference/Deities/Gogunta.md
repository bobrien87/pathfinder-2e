---
type: deity
source-type: "Remaster"
domains: "Indulgence, Might, Tyranny, Water"
favored-weapon: "Whip"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Jump]], Rank 3: [[Aqueous Orb]], Rank 5: [[Slither]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Gogunta, Song of the Swamp, is the demon lord of amphibians, boggards, and swamps. Gogunta is worshipped as a goddess by boggards, who believe her to be an ascended mobogo, though scholars suspect she was a former demon who gained the favor of Dagon. Lending credence to this latter theory, her realm, a stinking salt marsh, is located within Dagon's oceanic realm. Gogunta appears as an enormous, multi-headed frog with dozens of eyes and even more tongues, though boggards typically depict her as a titanic boggard queen.

**Title** Song of the Swamp

**Areas of Concern** Amphibians, boggards, swamps

**Edicts** Sacrifice creatures by drowning them, sing in the swamps, aid amphibians

**Anathema** Grant mercy to boggards who worship other gods

**Religious Symbol** twig fetish of a boggard

**Sacred Animal** frog

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
