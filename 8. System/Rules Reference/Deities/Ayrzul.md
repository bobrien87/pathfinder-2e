---
type: deity
source-type: "Remaster"
domains: "Destruction, Earth, Might, Secrecy"
favored-weapon: "Morningstar"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Shockwave]], Rank 2: [[Summon Elemental]], Rank 6: [[Petrify]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Lord of buried secrets, earth, and metal, the Fossilized King Ayrzul is a mystery even on the Plane of Earth. No one has seen the elemental lord of earth outside of his realm, the Blistering Labyrinth, and few know the truth of Ayrzul's nature or the form he takes when he appears. His power, motives, and origins are likewise the subjects of innumerable rumors. This speculation is all inconsequential to the Fossilized King; even the politics of his plane falls outside his notice. Instead, the lord of earth spends his time plotting against his bitter rival, Ymeri, the elemental lord of fire.

**Title** The Fossilized King

**Areas of Concern** Bone, buried secrets, earth, radiation

**Edicts** Obscure your true motives, slowly poison others, use the strength of stone to protect yourself and your secrets

**Anathema** Make fire larger or hotter than necessary, remove a creature's petrified condition

**Religious Symbol** fossilized dinosaur tooth

**Sacred Animal** tyrannosaurus

**Sacred Colors** brown, gray

**Source:** `= this.source` (`= this.source-type`)
