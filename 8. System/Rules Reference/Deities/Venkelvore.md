---
type: deity
source-type: "Remaster"
domains: "Indulgence, Pain, Passion, Zeal"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Society"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 2: [[Illusory Disguise]], Rank 6: [[Cursed Metamorphosis]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Among goblins, Venkelvore is considered the most beautiful of gods. Many goblins depict her as a fellow goblin rather than her true form: a barghest with pale blue fur and a trio of tails. Venkelvore has an eternal hunger that's only satiated by consuming her enemies. She prefers to eat her meals while still alive, as she not only feeds on the meat but also the prey's suffering, which Venkelvore considers a fantastic side dish.

**Title** Most Glorious Neverfull

**Areas of Concern** Beauty, gluttony, sadism

**Edicts** Gain beauty through pain and effort, keep a meal within arms length, torment those you eat

**Anathema** Reject a gift of food, neglect your appearance, starve yourself

**Religious Symbol** half-eaten piece of food

**Sacred Animal** crow

**Sacred Colors** gray, green

**Source:** `= this.source` (`= this.source-type`)
