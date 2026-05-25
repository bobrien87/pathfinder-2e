---
type: deity
source-type: "Remaster"
domains: "Knowledge, Lightning, Metal, Toil"
favored-weapon: "Flintlock-musket"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Conductive Weapon]], Rank 5: [[Toxic Cloud]], Rank 6: [[Chain Lightning]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Furious Thunder claims purview over electricity, gunpowder, and poisonous metals, all concrete manifestations of a consuming violence that doesn't discriminate. Such engines of destruction can just as easily turn against the hands that wield them. Petitioners of Cixyron are often arms dealers, constructing instruments of war for whomever will buy them. Sometimes such implements are sold to both sides of a conflict, causing battles to drag on longer than they would naturally. Cixyron doesn't care about the results of such conflicts or whether his followers get swept up in the hostilities, only that they leave shattered bodies in their wakes.

**Title** The Furious Thunder

**Areas of Concern** Electricity, gunpowder poisonous metals

**Edicts** Engineer complex acts of vengeance, construct glorious instruments of war, instill terror in your enemies from a distance

**Anathema** Intentionally destroy a weapon that you have crafted, explain your reasoning to someone less knowledgeable than you

**Religious Symbol** explosion of electricity

**Sacred Animal** ant

**Sacred Colors** red, yellow

**Source:** `= this.source` (`= this.source-type`)
