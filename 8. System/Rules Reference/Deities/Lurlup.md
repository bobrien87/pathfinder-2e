---
type: deity
source-type: "Remaster"
domains: "Destruction, Indulgence, Void, Plague"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Grease]], Rank 3: [[Bottomless Stomach]], Rank 7: [[Planar Palace]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Not much is known of Lurlup but that he has an endless appetite. Big Eater Brother appears as a typical goblin with dark blue skin and multiple mouths all around his body, such as the ones within his palms and on his lower back. He is a goblin hero-god revered by those who adore eating, though not necessarily because they enjoy the taste of food. Lurlup's followers eat because they enjoy the act of eating, and feel the need to be chewing or having something in their mouth. This means that the two main things they value are a food's texture and temperature. They also find purpose in eating unique things, such as parts from hydras or elementals.

**Title** Big Eater Brother

**Areas of Concern** Chefs, feasts, hyperphagia

**Edicts** Feed upon everything in your surroundings

**Anathema** Be fussy with your food, choose one meal over another, waste a meal

**Religious Symbol** dented cleaver

**Sacred Animal** hippopotamus

**Sacred Colors** silver, red

**Source:** `= this.source` (`= this.source-type`)
