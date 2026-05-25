---
type: deity
source-type: "Remaster"
domains: "Air, Freedom, Lightning, Travel"
favored-weapon: "Whip"
divine-font: "Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Liberating Command]], Rank 4: [[Aerial Form]], Rank 6: [[Chain Lightning]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ranginori, the Zephyrous Prince, is lord of air, welcome breezes, and thunderstorms. When he appears before mortals, Ranginori takes the form of an immense, lion-headed serpent spun from forbidding clouds, with hundreds of clawed feet and a mane that dances with lightning. The Zephyrous Prince has accumulated a small but loyal following in search of liberation, hope, and change for the multiverse. His realm on the Plane of Air is the Roaring Spark, a floating spiral of ruins that branch outward from a central crack of thunder.

**Title** The Zephyrous Prince

**Areas of Concern** Air, thunderstorms, welcome breezes

**Edicts** Open closed areas to fresh air, travel throughout your surroundings daily, fly or make creations that fly

**Anathema** Wrongfully imprison a creature, restrain a creature longer or more tightly than is necessary, suffocate a creature

**Religious Symbol** infinity sign of clouds and claws

**Sacred Animal** storm petral

**Sacred Colors** cyan, white

**Source:** `= this.source` (`= this.source-type`)
