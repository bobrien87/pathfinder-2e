---
type: deity
source-type: "Remaster"
domains: "Family, Healing, Magic, Passion"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Soothe]], Rank 2: [[Humanoid Form]], Rank 3: [[Animal Vision]], Rank 4: [[Creation]], Rank 5: [[Control Water]], Rank 6: [[Wall Of Force]], Rank 7: [[Planar Palace]], Rank 8: [[Migration]], Rank 9: [[Metamorphosis]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Isis is a member of the pantheon often worshiped in Ancient Osirion.

**Title** Queen of Miracles

**Areas of Concern** Fertility, magic motherhood, rebirth

**Edicts** Provide aid to the sick and wounded, use magic to help others, mourn the cherished dead, ritually purify yourself before entering sacred areas

**Anathema** Educate the uninitiated in sacred rites, betray loved ones or family, discriminate based on social class

**Religious Symbol** knot of Isis

**Sacred Animal** kite

**Sacred Colors** green, white

**Source:** `= this.source` (`= this.source-type`)
