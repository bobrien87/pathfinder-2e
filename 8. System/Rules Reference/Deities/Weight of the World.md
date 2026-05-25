---
type: deity
source-type: "Remaster"
domains: "Decay, Lightning, Nature, Water"
favored-weapon: "Javelin"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 5: [[Howling Blizzard]], Rank 6: [[Chain Lightning]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

All things gravitate toward equilibrium, but this is not the same thing as balance. Nature is constantly shifting and changing. When new growth becomes old, it is broken down to become raw materials for new things once more. Those who are closest to the land know this the best. Volcanoes erupt and destroy, but then make the earth on and near their slopes so much more fertile afterward... until they erupt anew.

People who have studied or survived natural disasters or extreme weather events also know this far too well. By making sacrifices and offerings to the deities who embody primal forces and changes, they gain a better understanding of how to harness these energies for themselves. Those who venerate the Weight of the World are usually spellcasters, but sometimes scholars who look for patterns and meaning in the natural world's cycles also seek a bit of divine inspiration in their quest for knowledge.

**Pantheon Members** Chamidu, Embaral, Gozreh, Hei Feng, Keltheald, Mother Vulture, Obari, The Green Mother, Valani, Yamatsumi

**Areas of Concern** aftermath of storms and natural disasters, meteorologists, patterns in natural elements, regeneration

**Edicts** meditate on the cycle of nature, teach others to be prepared for storms and other natural hazards, wield the elements as weapons

**Anathema** destroy nature without an immediate need, pass up an opportunity to watch storms and other natural phenomena

**Religious Symbol** globe covered in swirling clouds

**Source:** `= this.source` (`= this.source-type`)
