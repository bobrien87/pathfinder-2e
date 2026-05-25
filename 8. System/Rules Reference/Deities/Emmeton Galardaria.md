---
type: deity
source-type: "Remaster"
domains: "Cities, Duty, Family, Protection"
favored-weapon: "Frying-pan"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 3: [[Cozy Cabin]], Rank 6: [[Wall Of Force]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The halfling Emmeton Galardaria was once a common thief. Missing a hand from birth and abandoned as a child, the young Emmeton pledged to take from others everything they took for granted. He gained a reputation as a notorious highwayman, targeting merchants, nobles, and anyone who had become complacent with the gifts life had bestowed upon them. He often gave what he stole to others, earning fame among the less fortunate. As the legends of Emmeton's deeds continued to grow, the halfling began to take on a fraction of deific power. Some believe that Emmeton even stole the smallest of divine sparks from a god.

**Title** The Shared Hope

**Areas of Concern** community defense, familial bonds, found family, repayment

**Edicts** never betray those you have bonded with, repay favors when you can, stand strong with others

**Anathema** betray a friend or ally, endanger the life of a companion for personal gain, steal from those in need

**Religious Symbol** shield with a house painted on it

**Sacred Animal** pony

**Sacred Colors** gold, forest green, black

**Source:** `= this.source` (`= this.source-type`)
